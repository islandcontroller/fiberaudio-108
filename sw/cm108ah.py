# Copyright 2021, islandcontroller_ and the fiberaudio-108 contributors
# SPDX-License-Identifier: CERN-OHL-P-2.0

# ------------------------------------------------------------------------------
# fiberaudio-108
# https://github.com/islandcontroller/fiberaudio-108
#
#   CM108AH Configuration Tool
#
# Copyright © 2021 islandcontroller_ and contributors
# Licensed under CERN Open Hardware Licence Version 2 - Permissive
#-------------------------------------------------------------------------------

import argparse
from enum import IntEnum
import hexdump
import pywinusb.hid as hid
import time
from typing import *
import warnings
import yaml

class Device:
    """CM108AH USB HID access controls
    """
    _MEMORY_SIZE_WORDS: int = 44
    _VENDOR_ID: int = 0x0D8C
    _PRODUCT_ID: int = 0x013C

    class Report:
        """Generic HID report
        """
        def __init__(self, report_num: int):
            """Instantiate generic HID report

            Args:
                report_num (int): Report number
            """
            self._report_num = report_num

        def get_data(self) -> List[int]:
            """Get raw generic HID report data

            Returns:
                List[int]: Raw HID report data
            """
            return [self._report_num]

    class OutReport(Report):
        """Generic CM108AH HID Out report
        """
        _ACCESS_EEPROM = 0x80
        _ACCESS_GPIO = 0x00

        class HidReg(IntEnum):
            """HID Out register definitions
            """
            HID_OR0 = 0
            HID_OR1 = 1
            HID_OR2 = 2
            HID_OR3 = 3

        def __init__(self, report_num: int):
            """Instantiate new HID Out report

            Args:
                report_num (int): HID report number (0)
            """
            super().__init__(report_num)
            self._regs = [0x00] * 4

        def set_reg(self, reg: HidReg, value: int):
            """Set register content

            Args:
                reg (HidReg): Register selector
                value (int): Register value (byte)

            Raises:
                ValueError: Register selector out of range
                ValueError: Register value out of range
            """
            if reg < 0 or reg > 3:
                raise ValueError('Invalid register selection')
            if value > 0xFF:
                raise ValueError('Value out of range')
            self._regs[reg] = value
        
        def get_reg(self, reg: HidReg) -> int:
            """Get register value

            Args:
                reg (HidReg): Register selector

            Raises:
                ValueError: Register selector out of range

            Returns:
                int: Register value
            """
            if reg < 0 or reg > 3:
                raise ValueError('Invalid register selection')
            return self._regs[reg]

        def get_data(self) -> List[int]:
            """Get raw HID Out report data

            Returns:
                List[int]: Raw HID Out report data
            """
            return [self._report_num] + self._regs

    class EepromOutReport(OutReport):
        """HID Out Report for EEPROM access
        """
        _EEPROM_READ = 0x80
        _EEPROM_WRITE = 0xC0
        _EEPROM_ADDR_MASK = 0x3F

        def __init__(self):
            """Instantiate new HID Out report
            """
            super().__init__(0)
            self.set_reg(self.HidReg.HID_OR0, self._ACCESS_EEPROM)

        def set_eeprom_ctrl(self, addr: int, write_access: bool):
            """Set control byte

            Args:
                addr (int): Word address
                write_access (bool): Select write access

            Raises:
                ValueError: EEPROM address out of range
            """
            if addr > self._EEPROM_ADDR_MASK: 
                raise ValueError('Address out of range')
            access = self._EEPROM_WRITE if write_access else self._EEPROM_READ
            self.set_reg(self.HidReg.HID_OR3, access | addr)

        def set_eeprom_data16(self, value: int):
            """Set data from word

            Args:
                value (int): Data word

            Raises:
                ValueError: Value out of range
            """
            if value > 0xFFFF:
                raise ValueError('Value out of range')
            self.set_reg(self.HidReg.HID_OR2, (value >> 8) & 0xFF)
            self.set_reg(self.HidReg.HID_OR1, value & 0xFF)

        def set_eeprom_data8(self, value: List[int]):
            """Set data from list of bytes

            Args:
                value (List[int]): List of bytes (exactly 2)

            Raises:
                ValueError: List length does not match requirement
            """
            if len(value) != 2:
                raise ValueError('Value must be int[2] list with exactly 2 elements')
            self.set_reg(self.HidReg.HID_OR1, value[0])
            self.set_reg(self.HidReg.HID_OR2, value[1])

        def get_eeprom_data16(self) -> int:
            """Get data as word

            Returns:
                int: Data as word
            """
            return (self.get_reg(self.HidReg.HID_OR2) << 8) + self.get_reg(self.HidReg.HID_OR1)

        def get_eeprom_data8(self) -> List[int]:
            """Get data as list of bytes

            Returns:
                List[int]: Data as list of bytes
            """
            return [self.get_reg(self.HidReg.HID_OR1), self.get_reg(self.HidReg.HID_OR2)]
            
    class EepromReadOutReport(EepromOutReport):
        """HID Out report for data read access
        """
        def __init__(self, addr: int):
            """Instantiate new HID Out report

            Args:
                addr (int): Word address
            """
            super().__init__()
            self.set_eeprom_ctrl(addr, False)

    class EepromWrite16OutReport(EepromOutReport):
        """HID Out report for data word write access
        """
        def __init__(self, addr: int, value: int):
            """Instantiate new HID Out report

            Args:
                addr (int): Word address
                value (int): Data word
            """
            super().__init__()
            self.set_eeprom_ctrl(addr, True)
            self.set_eeprom_data16(value)

    class EepromWrite8OutReport(EepromOutReport):
        """HID Out report for 2 data bytes write access
        """
        def __init__(self, addr: int, value: List[int]):
            """Instantiate new HID Out report

            Args:
                addr (int): Word address
                value (List[int]): Data bytes (exactly 2)
            """
            super().__init__()
            self.set_eeprom_ctrl(addr, True)
            self.set_eeprom_data8(value)

    class GpioOutReport(OutReport):
        """HID Out report for GPIO and SPDIF access
        """
        def __init__(self):
            """Instantiate new GPIO access HID Out report
            """
            super().__init__(0)
            self.set_reg(self.HidReg.HID_OR0, self._ACCESS_GPIO)

        def set_spdif_status(self, valid: bool, data: int, category: int):
            """Set SPDIF status channel values

            Args:
                valid (bool): SPDIF status channel valid flag
                data (int): SPDIF status channel data nibble
                categoriy (int): SPDIF status channel category byte

            Raises:
                ValueError: Value for SPDIF status nibble out of range
                ValueError: Value for SPDIF category byte out of range
            """
            if data > 0x0F:
                raise ValueError('SPDIF status channel nibble out of range')
            if category > 0xFF:
                raise ValueError('SPDIF category byte out of range')
            self.set_reg(self.HidReg.HID_OR0, self._ACCESS_GPIO | data | (valid << 4))
            self.set_reg(self.HidReg.HID_OR3, category)

        def get_spdif_status_valid(self) -> bool:
            """Get SPDIF status channel valid flag from buffer

            Returns:
                bool: Status channel valid flag
            """
            return bool(self.get_reg(self.HidReg.HID_OR0) & 0x10)

        def get_spdif_status_data(self) -> int:
            """Get SPDIF status channel nibble from buffer

            Returns:
                int: SPDIF status channel nibble
            """
            return self.get_reg(self.HidReg.HID_OR0) & 0xF

        def get_spdif_status_cat(self) -> int:
            """Get SPDIF status channel category byte from buffer

            Returns:
                int: SPDIF status channel category byte
            """
            return self.get_reg(self.HidReg.HID_OR3)

        def set_gpio_data_reg(self, value: int):
            """Set GPIO data register

            Args:
                value (int): GPIO data register value (bit-masked output HIGH/LOW states)

            Raises:
                ValueError: GPIO data register value out of range
            """
            if value > 0x0F:
                raise ValueError('GPIO data value out of range')
            self.set_reg(self.HidReg.HID_OR1, value)

        def get_gpio_data_reg(self) -> int:
            """Get GPIO data register from buffer

            Returns:
                int: GPIO data register value
            """
            return self.get_reg(self.HidReg.HID_OR1)

        def set_gpio_dir_reg(self, value: int):
            """Set GPIO direction register value

            Args:
                value (int): GPIO direction register value (bit-masked out/in states)

            Raises:
                ValueError: GPIO direction register value out of range
            """
            if value > 0x0F:
                raise ValueError('GPIO direction value out of range')
            self.set_reg(self.HidReg.HID_OR2, value)

        def get_gpio_dir_reg(self) -> int:
            """Get GPIO direction register value from buffer

            Returns:
                int: GPIO direction register value
            """
            return self.get_reg(self.HidReg.HID_OR2)

    class InReport(Report):
        """Generic CM108AH HID In Report
        """
        class HidReg(IntEnum):
            """HID In register definitions
            """
            HID_IR0 = 0
            HID_IR1 = 1
            HID_IR2 = 2
            HID_IR3 = 3

        def __init__(self, data: List[int]):
            """Create new generic CM108 HID In report from raw data

            Args:
                data (List[int]): Raw HID In report data

            Raises:
                ValueError: Data does not match length requirements
            """
            if len(data) != 5:
                raise ValueError('Register list must contain exactly 5 items')
            
            report_num = data[0]
            regs = data[1:5]

            super().__init__(report_num)
            self._regs = regs

        def get_reg(self, reg: HidReg) -> int:
            """Get register value

            Args:
                reg (HidReg): Register selection

            Raises:
                ValueError: Register selector out of range

            Returns:
                int: Register value
            """
            if reg < 0 or reg > 3:
                raise ValueError('Invalid register selection')
            return self._regs[reg]

        def get_data(self) -> List[int]:
            """Get raw HID In report data

            Returns:
                List[int]: Raw HID In report data
            """
            return [self._report_num] + self._regs

    class EepromInReport(InReport):
        """HID In Report containing EEPROM data
        """
        def __init__(self, data: List[int]):
            """Instantiate EEPROM In Report from raw data

            Args:
                data (List[int]): Raw HID In report data
            """
            super().__init__(data)

        def get_eeprom_data16(self) -> int:
            """Get EEPROM data word

            Returns:
                int: EEPROM data word
            """
            return (self.get_reg(self.HidReg.HID_IR2) << 8) + self.get_reg(self.HidReg.HID_IR1)

        def get_eeprom_data8(self) -> List[int]:
            """Get EEPROM data as bytes list

            Returns:
                List[int]: EEPROM data fields as byte list
            """
            return [self.get_reg(self.HidReg.HID_IR1), self.get_reg(self.HidReg.HID_IR2)]

    class GpioInReport(InReport):
        """HID In report containing GPIO data
        """
        def __init__(self, data: List[int]):
            """Instantiate GPIO In report from raw data

            Args:
                data (List[int]): Raw HID In report data
            """
            super().__init__(data)

        def get_gpio_data_reg(self) -> int:
            """Get GPIO data register from buffer

            Returns:
                int: GPIO data register value
            """
            return self.get_reg(self.HidReg.HID_IR1)

        def get_gpio_buttons(self) -> int:
            """Get button states from buffer

            Returns:
                int: Button states
            """
            return self.get_reg(self.HidReg.HID_IR0) & 0xF

    class Button(IntEnum):
        """CM108 Button definitions
        """
        VOLUME_UP = 0x01
        VOLUME_DOWN = 0x02
        PLAY_MUTE = 0x04
        RECORD_MUTE = 0x08

    @classmethod
    def GetAvailableDevices(cls, vid: int = _VENDOR_ID, pid: int = None) -> List[hid.HidDevice]:
        """List all available devices matching VID/PID

        Args:
            vid: Vendor ID. Defaults to CMedia Vendor ID.
            pid: Product ID. Defaults to None (no filter).

        Returns:
            List[hid.HidDevice]: List of available HIDDevices matching VID/PID
        """
        if not pid: return hid.HidDeviceFilter(vendor_id=vid).get_devices()
        else:       return hid.HidDeviceFilter(vendor_id=vid, product_id=pid).get_devices()

    def __init__(self, device: hid.HidDevice):
        """Instantiate new CM108 Device handler from HIDDevice

        Args:
            device (hid.HidDevice): Underlying HIDDevice
        """
        self._hid_device: hid.HidDevice = device
        self._gpio_buttons: int = 0
        self._gpio_data: int = 0
        self._gpio_dir: int = 0

    def open(self):
        """Open underlying HID and assign HID in/out reports
        """
        self._hid_device.open()
        self._in_report = self._hid_device.find_input_reports()[0]
        self._out_report = self._hid_device.find_output_reports()[0]
        
    def read16(self, addr: int, num_words: int = 1) -> List[int]:
        """Read from EEPROM into list of words

        Args:
            addr (int): Start word address
            num_words (int, optional): Number of words to read. Defaults to 1.

        Raises:
            IOError: Failed to send USB HID out report

        Returns:
            List[int]: EEPROM data as list of words
        """
        data = []
        for offset in range(0, num_words):
            # Generate and send USB HID out report
            read_out_report = self.EepromReadOutReport(addr + offset)
            self._out_report.set_raw_data(read_out_report.get_data())
            
            if not self._out_report.send():
                raise IOError('Failed to send out report')

            # Readback data
            in_data = self._in_report.get()
            read_in_report = self.EepromInReport(in_data)

            # Append to buffer
            data = data + [read_in_report.get_eeprom_data16()]
            
        return data

    def read8(self, addr: int, num_words: int = 1) -> List[int]:
        """Read from EERPOM into list of bytes

        Args:
            addr (int): Start word address
            num_words (int, optional): Number of **words** to read. Defaults to 1.

        Raises:
            IOError: Failed to send USB HID Out report

        Returns:
            List[int]: EEPROM data as list of bytes
        """
        data = []
        for offset in range(0, num_words):
            # Generate and send USB HID out report
            read_out_report = self.EepromReadOutReport(addr + offset)
            self._out_report.set_raw_data(read_out_report.get_data())
            
            if not self._out_report.send():
                raise IOError('Failed to send out report')

            # Readback data
            in_data = self._in_report.get()
            read_in_report = self.EepromInReport(in_data)

            # Append to buffer
            data = data + read_in_report.get_eeprom_data8()

        return data

    def write16(self, addr: int, data: List[int], max_retry: int = 0):
        """Write array of words to EEPROM

        Args:
            addr (int): Start word address
            data (List[int]): List of words
            max_retry (int, optional): Number of write retries per address. Defaults to 0.

        Raises:
            IOError: Failed to send USB OUT report
            IOError: Repeated writes (retries) failed
        """
        for offset in range(0, len(data)):
            fail_count = 0
            success = False
        
            # Generate HID out report
            write_out_report = self.EepromWrite16OutReport(addr + offset, data[offset])
            self._out_report.set_raw_data(write_out_report.get_data())

            # Retry until success or max retries
            while not success:
                # Send HID Out report (optional retry)
                if not self._out_report.send():
                    raise IOError('Failed to send out report')

                # Readback response
                in_data = self._in_report.get()
                write_in_report = self.EepromInReport(in_data)

                # Ctrl bytes must match
                success = write_in_report.get_reg(self.InReport.HidReg.HID_IR3) == write_out_report.get_reg(self.InReport.HidReg.HID_IR3)
                
                if not success:
                    fail_count = fail_count + 1
                    
                    # Crude retry throttling
                    time.sleep(0.1)
                else:
                    fail_count = 0

                # Bail if fail count exceeds limit
                if fail_count > max_retry:
                    raise IOError(f"Repeated writes to address 0x{addr + offset:02X} failed. Sent {write_out_report.get_data()}, got {write_in_report.get_data()}")

    def write8(self, addr: int, data: List[int], max_retry: int = 0):
        """Write array of bytes to EEPROM

        Args:
            addr (int): Start word address
            data (List[int]): List of bytes (multiple of 2!)
            max_retry (int, optional): Number of write retries for each address. Defaults to 0.

        Raises:
            ValueError: Length must be multiple of 2
            IOError: Failed to send USB HID out report
            IOError: Repeated writes (retries) failed
        """
        if len(data) & 0x1:
            raise ValueError('Data length must be multiple of 2')

        num_words = len(data) >> 1
        for offset in range(0, num_words):
            byte_offset = offset << 1
            fail_count = 0
            success = False
            
            # Generate HID Out report
            write_out_report = self.EepromWrite8OutReport(addr + offset, data[byte_offset:byte_offset+2])
            self._out_report.set_raw_data(write_out_report.get_data())

            # Retry until success or max retries
            while not success:
                # Send HID Out report (optional retry)
                if not self._out_report.send():
                    raise IOError('Failed to send out report')

                # Readback response
                in_data = self._in_report.get()
                write_in_report = self.EepromInReport(in_data)

                # Ctrl bytes must match
                success = write_in_report.get_reg(self.InReport.HidReg.HID_IR3) == write_out_report.get_reg(self.InReport.HidReg.HID_IR3)
                
                if not success:
                    fail_count = fail_count + 1

                    # Crude retry throttling
                    time.sleep(0.1)
                else:
                    fail_count = 0

                # Bail if fail count exceeds limit
                if fail_count > max_retry:
                    raise IOError(f"Repeated writes to address 0x{addr + offset:02X} failed. Sent {write_out_report.get_data()}, got {write_in_report.get_data()}")

    def config_gpio(self, modes: int):
        """Configure GPIO in/out modes

        Args:
            modes (int): Output configuration

        Raises:
            ValueError: Configuration value out of range
        """
        if modes > 0x0F:
            raise ValueError('Modes value out of range')
        self._gpio_dir = modes
        self._update_gpio(self._gpio_data)

    def _update_gpio(self, data: int) -> int:
        """Send new GPIO states to the device and update inputs

        Args:
            data (int): New output states

        Raises:
            IOError: Failed to send HID report

        Returns:
            int: Updated input state buffer
        """
        # Generate HID Out report
        write_out_report = self.GpioOutReport()
        write_out_report.set_gpio_dir_reg(self._gpio_dir)
        write_out_report.set_gpio_dir_reg(data)
        self._out_report.set_raw_data(write_out_report.get_data())

        # Send report
        if not self._out_report.send():
            raise IOError('Failed to send out report')

        # Readback response
        in_data = self._in_report.get()
        write_in_report = self.GpioInReport(in_data)

        # Update internal buffers
        self._gpio_data = write_in_report.get_gpio_data_reg()
        self._gpio_buttons = write_in_report.get_gpio_buttons()
        return self._gpio_data

    def write_gpio_pin(self, pin: int, value: bool):
        """Write GPIO pin value

        Args:
            pin (int): GPIO pin number 1..4
            value (bool): Output state

        Raises:
            ValueError: GPIO pin selector out of range
        """
        if pin < 1 or pin > 4:
            raise ValueError('GPIO pin selection out of range')
        mask = 1 << (pin - 1)
        out_states = (self._gpio_data & ~mask) | (mask if value else 0)
        self._update_gpio(out_states)
    
    def write_gpio_reg(self, value: int):
        """Set GPIO data register value

        Args:
            value (int): Data register value

        Raises:
            ValueError: Register value out of range
        """
        if value > 0x0F:
            raise ValueError('GPIO data register value out of range')
        self._update_gpio(value)

    def read_gpio_pin(self, pin: int) -> bool:
        """Update cache and read pin signal state

        Args:
            pin (int): GPIO number (1-4)

        Raises:
            ValueError: GPIO number out of range

        Returns:
            bool: Pin signal state
        """
        if pin < 1 or pin > 4:
            raise ValueError('GPIO pin selection out of range')
        mask = 1 << (pin - 1)
        return bool(self._update_gpio(self._gpio_data) & mask)
        
    def read_gpio_reg(self) -> int:
        """Update chache and read GPIO pin states register

        Returns:
            int: Pin states register (GPIO1..4)
        """
        return self._update_gpio(self._gpio_data)

    def read_button(self, button: Button) -> bool:
        """Read dedicated button state

        Args:
            button (Button): Button selector or bitmask

        Raises:
            ValueError: Invalid button selector

        Returns:
            bool: Button state. ORed button states if bitmask selector is used
        """
        if button > 0x08:
            raise ValueError('Button selector out of range')
        self._update_gpio(self._gpio_data)
        return bool(self._gpio_buttons & button)

    def close(self):
        """Close underlying HID
        """
        self._hid_device.close()

    def __enter__(self):
        """For use with "with()"

        Returns:
            [type]: open()'ed reference to self
        """
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """For use with "with()"

        Args:
            exc_type ([type]): Not used
            exc_val ([type]): Not used
            exc_tb ([type]): Not used
        """
        self.close()

class Configuration:
    """CM108 Device configuration for download into attached EEPROM
    """
    _MAGIC_NUMBER = 0x6700
    _MAGIC_FLAG_CFG_VALID = 0x08
    _MAGIC_FLAG_MANUF_EN = 0x04
    _MAGIC_FLAG_SERNUM_EN = 0x02
    _MAGIC_FLAG_PROD_EN = 0x01
    _CFG_SHDN_DAC = 0x0100
    _CFG_TPC = 0x0080
    _CFG_MIC_HP = 0x0020
    _CFG_ADC_SYNC = 0x0010
    _CFG_MIC_BOOST = 0x0008
    _CFG_DAC_OUT_HP = 0x0004
    _CFG_HID_EN = 0x0002
    _CFG_REM_WKUP_EN = 0x0001

    def __init__(self):
        """Instantiate new configuration object
        """
        self._magic_flags = None
        self._vid = None
        self._pid = None
        self._sernum = None
        self._prod = None
        self._manuf = None
        self._dac_vol = None
        self._adc_vol = None
        self._cfg_bits = None

    def set_magic_flags(self, cfg_bits_valid: bool = False, use_manuf_str: bool = False, use_serial_num: bool = False, use_product_str: bool = False):
        """Set magic flags (first EEPROM word)

        Args:
            cfg_bits_valid (bool, optional): Configuration bits (see set_config_bits) are valid. Defaults to False.
            use_manuf_str (bool, optional): Use manufacturer string from EEPROM. Defaults to False.
            use_serial_num (bool, optional): Use serial number string from EEPROM. Defaults to False.
            use_product_str (bool, optional): User product name string from EEPROM. Defaults to False.
        """
        config_word = self._MAGIC_NUMBER

        if cfg_bits_valid:
            config_word = config_word | self._MAGIC_FLAG_CFG_VALID
        if use_manuf_str:
            config_word = config_word | self._MAGIC_FLAG_MANUF_EN
        if use_serial_num:
            config_word = config_word | self._MAGIC_FLAG_SERNUM_EN
        if use_product_str:
            config_word = config_word | self._MAGIC_FLAG_PROD_EN

        self._magic_flags = config_word
    
    def get_magic_flags(self) -> int:
        """Get magic flags

        Returns:
            int: Magic flags (First EEPROM word)
        """
        return self._magic_flags

    def clear_magic_flags(self):
        """Clear magic flags
        """
        self._magic_flags = None

    def is_magic_flags_valid(self) -> bool:
        """Check whether magic flags have been set and magic word is valid

        Returns:
            bool: Flags are set and magic word is valid
        """
        return (self._magic_flags is not None) and ((self._magic_flags & 0xFF00) == self._MAGIC_NUMBER) and not (self._magic_flags & 0x0010)

    def set_vendor_id(self, vid: int):
        """Set USB VID

        Args:
            vid (int): USB VID

        Raises:
            ValueError: USB VID outside valid range
        """
        if vid > 0xFFFF:
            raise ValueError('Vendor ID out of range')
        self._vid = vid

    def get_vendor_id(self) -> int:
        """Get USB VID

        Returns:
            int: USB VID
        """
        return self._vid

    def is_vendor_id_valid(self) -> bool:
        """Check whether USB VID has been set
        
        Returns:
            bool: USB VID is set
        """
        return (self._vid is not None) and not (self._vid > 0xFFFF)

    def set_product_id(self, pid: int):
        """Set USB PID

        Args:
            pid (int): USB PID

        Raises:
            ValueError: USB PID outside valid range
        """
        if pid > 0xFFFF:
            raise ValueError('Product ID out of range')
        self._pid = pid

    def get_product_id(self) -> int:
        """Get USB PID

        Returns:
            int: USB PID
        """
        return self._pid

    def is_product_id_valid(self) -> bool:
        """Check if USB PID has been set

        Returns:
            bool: USB is assigned
        """
        return (self._pid is not None) and not (self._pid > 0xFFFF)

    def set_serial_num(self, serial_num: str):
        """Set serial number

        Args:
            serial_num (str): Serial number

        Raises:
            ValueError: Serial number length exceeds allowed range
        """
        if len(serial_num) > 13:
            raise ValueError('Serial number length out of range')
        self._sernum = serial_num

    def get_serial_num(self) -> str:
        """Get serial number

        Returns:
            str: Serial number (String!)
        """
        return self._sernum

    def is_serial_num_valid(self) -> bool:
        """Check whether serial number has been set

        Returns:
            bool: Serial number is assigned
        """
        return (self._sernum is not None) and not (len(self._sernum) > 13)

    def set_product_name(self, name: str):
        """Set product name

        Args:
            name (str): Product name

        Raises:
            ValueError: Product name length exceeds allowed range
        """
        if len(name) > 16:
            raise ValueError('Product name length out of range')
        self._prod = name

    def get_product_name(self) -> str:
        """Get product name

        Returns:
            str: Product name
        """
        return self._prod

    def is_product_name_valid(self) -> bool:
        """Check whether product name has been set

        Returns:
            bool: Product name is assigned
        """
        return (self._prod is not None) and not (len(self._prod) > 16)

    def set_manufacturer_name(self, name: str):
        """Set manufacturer name

        Args:
            name (str): Manufacturer name

        Raises:
            ValueError: Name length exceeds allowed range
        """
        if len(name) > 16:
            raise ValueError('Manufacturer name length out of range')
        self._manuf = name

    def get_manufacturer_name(self) -> str:
        """
        Get manufacturer name

        Returns:
            str: Manufacturer name
        """
        return self._manuf

    def is_manufacturer_name_valid(self) -> bool:
        """Check whether manufacturer name has been set

        Returns:
            bool: Manufacturer name is assigned
        """
        return (self._manuf is not None) and not (len(self._manuf) > 16)

    def set_dac_volume(self, volume: int):
        """Set DAC volume preset

        Args:
            volume (int): DAC volume preset in EEPROM notation

        Raises:
            ValueError: Volume value is out of range
        """
        if volume < 0x02 or volume > 0x4A:
            raise ValueError('Volume out of range')
        self._dac_vol = volume

    def get_dac_volume(self) -> int:
        """Get DAC volume preset

        Returns:
            [type]: DAC volume preset in EEPROM notation
        """
        return self._dac_vol

    def is_dac_volume_valid(self) -> bool:
        """Check whether the DAC volume preset has been set

        Returns:
            bool: DAC volume preset is assigned
        """
        return (self._dac_vol is not None) and not (self._dac_vol < 0x02) and not (self._dac_vol > 0x4A)

    def set_adc_volume(self, volume: int):
        """Set ADC volume preset

        Args:
            volume (int): Volume preset in EEPROM notation

        Raises:
            ValueError: Volume value is out of range
        """
        if volume > 0x78:
            raise ValueError('Volume out of range')
        self._adc_vol = volume

    def get_adc_volume(self) -> int:
        """Get ADC volume preset

        Returns:
            int: Volume preset value in EEPROM notation
        """
        return self._adc_vol

    def is_adc_volume_valid(self) -> bool:
        """Check whether ADC volume preset has been set and is in valid range

        Returns:
            bool: ADC volume preset is assigned
        """
        return (self._adc_vol is not None) and not (self._adc_vol > 0x78)

    def set_config_bits(self, shdn_dac: bool = False, total_pwr_ctl: bool = False, mic_hp: bool = True, 
                              adc_sync: bool = False, mic_boost: bool = True, dac_out_hp: bool = False, 
                              hid_en: bool = True, remote_wkup_en: bool = False):
        """Set configuration bitfield

        Args:
            shdn_dac (bool, optional): Shut down on-chip DAC analog section. Defaults to False.
            total_pwr_ctl (bool, optional): Function unclear, presumably low-power related. Defaults to False.
            mic_hp (bool, optional): Enable microphone high-pass filter. Defaults to True.
            adc_sync (bool, optional): Enable ADC synchronisation mode. Defaults to False.
            mic_boost (bool, optional): Enable microphone boost. Defaults to True.
            dac_out_hp (bool, optional): Set DAC output to headphones mode. Defaults to False.
            hid_en (bool, optional): Enable HID endpoint. WARNING this can brick the device. Defaults to True.
            remote_wkup_en (bool, optional): Enable remote wakeup feature. Defaults to False.
        """
        config_word = 0

        if shdn_dac:
            config_word = config_word | self._CFG_SHDN_DAC
        if total_pwr_ctl:
            config_word = config_word | self._CFG_TPC
        if mic_hp:
            config_word = config_word | self._CFG_MIC_HP
        if adc_sync:
            config_word = config_word | self._CFG_ADC_SYNC
        if mic_boost:
            config_word = config_word | self._CFG_MIC_BOOST
        if dac_out_hp:
            config_word = config_word | self._CFG_DAC_OUT_HP
        if hid_en:
            config_word = config_word | self._CFG_HID_EN
        if remote_wkup_en:
            config_word = config_word | self._CFG_REM_WKUP_EN

        self._cfg_bits = config_word

    def get_config_bits(self) -> int:
        """Get configuration bitfield

        Returns:
            int: Word containing configuration bits
        """
        return self._cfg_bits

    def is_config_bits_valid(self) -> bool:
        """Check whether configuration bits have been set and contain valid data

        Returns:
            bool: Configuration bits are valid
        """
        return (self._cfg_bits is not None) and not (self._cfg_bits & 0xFE40)

class ConfigurationSerializer:
    """Configuration serializer for download into a device
    """
    def __init__(self, config: Configuration):
        """Create new serializer instance

        Args:
            config (Configuration): Source configuration object
        """
        self._config = config

    def serialize(self) -> List[int]:
        """Serialize assigned configuration into binary word array

        Returns:
            List[int]: Array of words for download into the device (=EEPROM image)
        """
        def pack_str(data: str) -> List[int]:
            """Helper function for USB string descriptor packing

            Args:
                data (str): Source string

            Raises:
                ValueError: Maximum of 127 characters can be packed, as field length has byte type

            Returns:
                List[int]: Encoded and packed word array
            """
            length = len(data)
            if length > 0x7F:
                raise ValueError('Can not pack more than 127 bytes')
            bytes_data = data.encode('UTF-8')

            # Buffer area
            words_buffer = [0x0000] * ((length + 2) >> 1) # +1 for length byte, +1 for shift-ceil()

            # Length into low byte of first word
            words_buffer[0] = (words_buffer[0] & 0xFF00) | ((length + 1)<< 1)

            # Pack into words, offset by 1 byte
            for i in range(0, length):
                offset = (i + 1) >> 1 # +1 for length in first low byte

                if not i & 0x01:
                    # Even indices into high bytes
                    words_buffer[offset] = (words_buffer[offset] & 0x00FF) | (bytes_data[i] << 8)
                else:
                    # Odd indices into low bytes
                    words_buffer[offset] = (words_buffer[offset] & 0xFF00) | bytes_data[i]
            
            return words_buffer

        def copy_with_offset(dest: list, src: list, offset: int) -> list:
            """Copy source list values into destination list, starting at destination offset

            Args:
                dest (list): Destination list (reference)
                src (list): Source list
                offset (int): Destination start offset

            Returns:
                list: Destination list reference
            """
            for i in range(0, len(src)):
                dest[offset + i] = src[i]
            return dest

        # Target EEPROM buffer
        memory_buffer = [0xFFFF] * Device._MEMORY_SIZE_WORDS

        # Alias
        c = self._config

        # Conditional assignment of each field - leave unprogrammed (0xFFFF) otherwise
        if c.is_magic_flags_valid(): memory_buffer[0] = c.get_magic_flags()
        if c.is_vendor_id_valid(): memory_buffer[1] = c.get_vendor_id()
        if c.is_product_id_valid(): memory_buffer[2] = c.get_product_id()
        if c.is_serial_num_valid(): copy_with_offset(memory_buffer, pack_str(c.get_serial_num()), 3)            
        if c.is_product_name_valid(): copy_with_offset(memory_buffer, pack_str(c.get_product_name()), 10)
        if c.is_manufacturer_name_valid(): copy_with_offset(memory_buffer, pack_str(c.get_manufacturer_name()), 26)
        if c.is_dac_volume_valid(): memory_buffer[42] = (memory_buffer[42] & 0x00FF) | (c.get_dac_volume() << 8)
        if c.is_adc_volume_valid(): memory_buffer[42] = (memory_buffer[42] & 0xFF00) | c.get_adc_volume()
        if c.is_config_bits_valid(): memory_buffer[43] = c.get_config_bits()

        return memory_buffer

class ConfigurationReader:
    """Utility for reading configurations from a YAML file
    """
    def __init__(self, path: str, enable_usb_ids: bool = False, enable_hid_bit: bool = False):
        """Instantiate new configuration reader

        Args:
            path (str): File path
            enable_usb_ids (bool, optional): Enable USB VID/PID configuration. Defaults to False.
            enable_hid_bit (bool, optional): Enable HID_EN bit configuration. Defaults to False.
        """
        self._path = path
        self._enable_usb_ids = enable_usb_ids
        self._enable_hid_bit = enable_hid_bit

    def read(self) -> Configuration:
        """Read configuration from a YAML file

        Raises:
            ValueError: Configuration file was empty

        Returns:
            Configuration: Parsed configuration
        """
        with open(self._path, 'r') as file:
            data = yaml.safe_load(file)

        if not data:
            raise ValueError('Configuration file empty')

        c = Configuration()

        # Process serial number
        has_serial = 'serial' in data
        if has_serial:
            c.set_serial_num(data['serial'])

        # Process manufacturer name
        has_manuf_name = 'manufacturer' in data
        if has_manuf_name: 
            c.set_manufacturer_name(data['manufacturer'])

        # Process product name
        has_product_name = 'product' in data
        if has_product_name:
            c.set_product_name(data['product'])        
            
        # Process configuation bits, retaining default values for unset fields
        has_config_bits = 'config' in data
        if has_config_bits:
            config_data = data['config']
            shdn_dac = config_data['SHDN_DAC'] if 'SHDN_DAC' in config_data else False
            total_pwr_ctl = config_data['TOTAL_PWR_CTL'] if 'TOTAL_PWR_CTL' in config_data else False
            mic_hp = config_data['MIC_HP'] if 'MIC_HP' in config_data else True
            adc_sync = config_data['ADC_SYNC'] if 'ADC_SYNC' in config_data else False
            mic_boost = config_data['MIC_BOOST'] if 'MIC_BOOST' in config_data else True
            dac_out_hp = config_data['DAC_OUT_HP'] if 'DAC_OUT_HP' in config_data else False
            hid_en = True
            if 'HID_EN' in config_data:
                if self._enable_hid_bit:
                    hid_en = config_data['HID_EN']
                else:
                    warnings.warn(f"Setting of HID bit disabled - overriding with default (enabled)")
            remote_wkup_en = config_data['REMOTE_WKUP_EN'] if 'REMOTE_WKUP_EN' in config_data else False
            c.set_config_bits(shdn_dac, total_pwr_ctl, mic_hp, adc_sync, mic_boost, dac_out_hp, hid_en, remote_wkup_en)

        # Apply magic flags
        c.set_magic_flags(has_config_bits, has_manuf_name, has_serial, has_product_name)

        # Pre-Set default vendor and product IDs
        c.set_vendor_id(Device._VENDOR_ID)
        c.set_product_id(Device._PRODUCT_ID)
        
        # Process USB ID fields
        if 'usb' in data:
            usb_data = data['usb']
            if self._enable_usb_ids:
                if 'vid' in usb_data: c.set_vendor_id(usb_data['vid'])
                if 'pid' in usb_data: c.set_product_id(usb_data['pid'])
            else:
                warnings.warn('Setting of USB IDs disabled - overriding with default (Cmedia CM108AH VID/PID)')

        # Process volume presets
        if 'presets' in data:
            presets_data = data['presets']
            if 'adc' in presets_data: c.set_adc_volume(presets_data['adc'])
            if 'dac' in presets_data: c.set_dac_volume(presets_data['dac'])

        return c

    def __enter__(self) -> Configuration:
        return self.read()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class Programmer:
    """Handler for configuration download into EEPROM
    """
    _THROTTLE_DELAY: float = 0.1

    def __init__(self, device: Device):
        """Instantiate new programmer

        Args:
            device (Device): Target device reference
        """
        self._device = device

    def download(self, config: Configuration, print_progress: bool = False):
        """Download configuration into assigned device EEPROM

        Args:
            config (Configuration): Source configuration object
            print_progress (bool, optional): Print ASCII progress bar. Defaults to False.

        Raises:
            ValueError: Configuration data does not match EEPROM 
        """
        serializer = ConfigurationSerializer(config)
        data = serializer.serialize()

        if len(data) != Device._MEMORY_SIZE_WORDS:
            raise ValueError('Configuration data length does not match device requirement')
        
        for i in range(len(data)):
            self._device.write16(i, data[i:i+1], 10)

            if print_progress:
                print('#', end='', flush=True)
            
            # Crude data rate throttling
            time.sleep(self._THROTTLE_DELAY)

        if print_progress:
                print()

    def verify(self, config: Configuration, num_retry: int = 3) -> bool:
        """Compare EEPROM content with reference configuration

        Args:
            config (Configuration): Reference configuration
            print_progress (bool, optional): Print ASCII progress bar. Defaults to False.
            num_retry (int, optional). Number of re-reads in case of failure. Defaults to 3

        Returns:
            bool: EEPROM content matches configuration
        """

        serializer = ConfigurationSerializer(config)
        compare = serializer.serialize()

        for i in range(0, num_retry + 1):
            readback = self._device.read16(0, len(compare))
            if compare == readback:
                # Early exit from loop
                return True

        # All tries exhausted
        return False

    def empty_check(self, num_retry: int = 3) -> bool:
        """Check if configuration EEPROM is erased

        Args:
            config (Configuration): Reference configuration
            print_progress (bool, optional): Print ASCII progress bar. Defaults to False.
            num_retry (int, optional). Number of re-reads in case of failure. Defaults to 3

        Returns:
            bool: EEPROM is erased
        """
        compare = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        
        for i in range(0, num_retry + 1):
            readback = self._device.read16(0, len(compare))
            if compare == readback:
                # Early exit from loop
                return True

        # All tries exhausted
        return False

    def erase(self, print_progress: bool = False):
        """Erases the assigned device's EEPROM contents

        Args:
            print_progress (bool, optional): Print ASCII progress bar. Defaults to False.
        """
        for i in range(0, Device._MEMORY_SIZE_WORDS):
            self._device.write16(i, [0xFFFF], 10)

            if print_progress:
                print('#', end='', flush=True)

            # Crude data rate throttling
            time.sleep(self._THROTTLE_DELAY)
        
        if print_progress:
                print()

if __name__ == '__main__':
    _VERSION_STR="(not set)"

    # Helper function for device selection
    def get_device(vid: int, pid: int, index: int) -> Device:
        available = Device.GetAvailableDevices(vid, pid)
        if not available:
            print('No devices found.')
            return None
        if index >= len(available):
            print('Device index out of range.')
            return None
        print(f"Selected device index {index}.")
        return available[index]

    parser = argparse.ArgumentParser(description='CM108AH configuration tool')
    subparsers = parser.add_subparsers(dest='mode')

    # Hex string input for VID/PID
    _hex = lambda x: int(x, base=16)

    # List
    list_parser = subparsers.add_parser('list', help='List available devices')
    list_parser.add_argument('--vid', help='USB Vendor ID', type=_hex, default=Device._VENDOR_ID)
    list_parser.add_argument('--pid', help='USB Product ID', type=_hex, default=None)

    # Read
    readout_parser = subparsers.add_parser('read', help='Read EEPROM contents')
    readout_parser.add_argument('--vid', help='USB Vendor ID', type=_hex, default=Device._VENDOR_ID)
    readout_parser.add_argument('--pid', help='USB Product ID', type=_hex, default=None)
    readout_parser.add_argument('--device', help='Device index', type=int, default=0)

    # Erase mode
    erase_parser = subparsers.add_parser('erase', help='Erase EEPROM')
    erase_parser.add_argument('--vid', help='USB Vendor ID', type=_hex, default=Device._VENDOR_ID)
    erase_parser.add_argument('--pid', help='USB Product ID', type=_hex, default=None)
    erase_parser.add_argument('--device', help='Device index', type=int, default=0)
    
    # Program mode
    program_parser = subparsers.add_parser('program', help='Program EEPROM from config file')
    program_parser.add_argument('file', help='configuration file', type=str)
    program_parser.add_argument('--vid', help='USB Vendor ID', type=_hex, default=Device._VENDOR_ID)
    program_parser.add_argument('--pid', help='USB Product ID', type=_hex, default=None)
    program_parser.add_argument('--device', help='device index', type=int, default=0)
    program_parser.add_argument('--enable-hid-bit', help='enable HID_EN bit configuration', type=bool, default=False)
    program_parser.add_argument('--enable-usb-ids', help='enable USB VID/PID configuration', type=bool, default=False)
    
    # Version information
    parser.add_argument('--version', action='version', version='%(prog)s Version '+_VERSION_STR)

    # Process input
    args = parser.parse_args()

    if args.mode == 'list':
        # List available devices
        print('Searching for available devices...')

        # Search for devices matching VID (and PID if specified)
        found = Device.GetAvailableDevices(vid=args.vid, pid=args.pid)
        if not found:
            print('No devices found.')
            exit(1)
        
        # Print info for each device
        for i in range(len(found)):
            print(f"[{i}] {found[i].vendor_id:04x}:{found[i].product_id:04x} {found[i].vendor_name} - {found[i].product_name} (SN '{found[i].serial_number}')")
        
        print(f"{len(found)} device(s) found.")
        exit(0)

    elif args.mode == 'read':
        # Handle read mode
        print('Entering READ mode.')

        # Select device from list of available devices
        device = get_device(args.vid, args.pid, args.device)
        if not device:
            exit(1)

        # Read EEPROM content and print hexdump
        with Device(device) as device:
            print('Reading EEPROM...')
            data = device.read8(0, Device._MEMORY_SIZE_WORDS)
            hexdump.hexdump(bytes(data))
            print('Done.')
            exit(0)

    elif args.mode == 'erase':
        # Handle erase mode
        print('Entering ERASE mode.')

        # Select device from list of available devices
        device = get_device(args.vid, args.pid, args.device)
        if not device:
            exit(1)
    
        # Open device and erase contents
        with Device(device) as device:
            print('Erasing EEPROM...')
            programmer = Programmer(device)
            programmer.erase(print_progress='True')
            
            print('Performing empty-check...')
            verify_result = programmer.empty_check()
            if verify_result:
                print('Success.')
                exit(0)
            else:
                print('Check failed. Device is not empty.')
                exit(1)

    elif args.mode == 'program':
        # Handle program mode
        print('Entering PROGRAM mode.')

        # Select device from list of available devices
        device = get_device(args.vid, args.pid, args.device)
        if not device:
            exit(1)

        # Display warnings
        if args.enable_usb_ids:
            print('WARNING: USB VID/PID configuration enabled!')
        if args.enable_hid_bit:
            print('WARNING: HID_EN bit configuration enabled!')

        # Read configuration from file
        print('Parsing configuration file.')
        with ConfigurationReader(args.file, args.enable_usb_ids, args.enable_hid_bit) as config:
            # Serialize configuration and download to device
            with Device(device) as device:
                print('Programming EEPROM...')
                programmer = Programmer(device)
                programmer.download(config, True)

                # Verify contents
                print('Verifying EEPROM content...')
                verify_result = programmer.verify(config)
                if verify_result:
                    print('Success.')
                    exit(0)
                else:
                    print('Verification failed.')
                    exit(1)

    else:
        # Invalid mode
        parser.error('Invalid mode selection')

    # Other errors
    exit(1)

