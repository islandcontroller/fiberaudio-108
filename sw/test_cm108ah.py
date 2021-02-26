# Copyright 2021, islandcontroller_ and the fiberaudio-108 contributors
# SPDX-License-Identifier: CERN-OHL-P-2.0

# ------------------------------------------------------------------------------
# fiberaudio-108
# https://github.com/islandcontroller/fiberaudio-108
#
#   Unit tests for the CM108AH Configuration Tool
#
# Copyright © 2021 islandcontroller_ and contributors
# Licensed under CERN Open Hardware Licence Version 2 - Permissive
#-------------------------------------------------------------------------------

from cm108ah import *
import unittest

class TestReport(unittest.TestCase):
    def test_GetData(self):
        expect_report_num = 1
        expect_data = [expect_report_num]

        r = Device.Report(expect_report_num)
        self.assertListEqual(r.get_data(), expect_data)

class TestOutReport(unittest.TestCase):
    def test_GetData(self):
        expect_report_num = 1
        expect_data_len = 5
        expect_data = [expect_report_num, 0, 0, 0, 0]

        r = Device.OutReport(expect_report_num)
        self.assertEqual(len(r.get_data()), expect_data_len)
        self.assertListEqual(r.get_data(), expect_data)

    def test_Regs(self):
        expect_hid_or0 = 0
        expect_hid_or1 = 1
        expect_hid_or2 = 2
        expect_hid_or3 = 3

        actual_hid_or0 = Device.OutReport.HidReg.HID_OR0
        actual_hid_or1 = Device.OutReport.HidReg.HID_OR1
        actual_hid_or2 = Device.OutReport.HidReg.HID_OR2
        actual_hid_or3 = Device.OutReport.HidReg.HID_OR3

        self.assertEqual(actual_hid_or0, expect_hid_or0)
        self.assertEqual(actual_hid_or1, expect_hid_or1)
        self.assertEqual(actual_hid_or2, expect_hid_or2)
        self.assertEqual(actual_hid_or3, expect_hid_or3) 

    def test_SetRegValueRange(self):
        expect_pass_value = 0xFF
        expect_fail_value = 0x100

        r = Device.OutReport(0)

        try:
            r.set_reg(Device.OutReport.HidReg.HID_OR0, expect_pass_value)
            r.set_reg(Device.OutReport.HidReg.HID_OR1, expect_pass_value)
            r.set_reg(Device.OutReport.HidReg.HID_OR2, expect_pass_value)
            r.set_reg(Device.OutReport.HidReg.HID_OR3, expect_pass_value)
        except:
            self.fail()

        self.assertRaises(ValueError, r.set_reg, Device.OutReport.HidReg.HID_OR0, expect_fail_value)
        self.assertRaises(ValueError, r.set_reg, Device.OutReport.HidReg.HID_OR1, expect_fail_value)
        self.assertRaises(ValueError, r.set_reg, Device.OutReport.HidReg.HID_OR2, expect_fail_value)
        self.assertRaises(ValueError, r.set_reg, Device.OutReport.HidReg.HID_OR3, expect_fail_value)

    def test_SetRegSelectRange(self):
        expect_pass_value = 3
        expect_fail_value1 = -1
        expect_fail_value2 = 4

        r = Device.OutReport(0)

        try:
            r.set_reg(expect_pass_value, 0)
        except:
            self.fail()

        self.assertRaises(ValueError, r.set_reg, expect_fail_value1, 0)
        self.assertRaises(ValueError, r.set_reg, expect_fail_value2, 0)

    def test_SetRegValuePosition(self):
        reg_select_enum = [
            Device.OutReport.HidReg.HID_OR0,
            Device.OutReport.HidReg.HID_OR1,
            Device.OutReport.HidReg.HID_OR2,
            Device.OutReport.HidReg.HID_OR3
        ]
        reg_select_int = [0, 1, 2, 3]
        reg_value = [1, 2, 3, 4]
        reg_data = [
            [0, 1, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 3, 0],
            [0, 0, 0, 0, 4]
        ]
        
        for i in range(0, 4):
            select_enum = reg_select_enum[i]
            select_int = reg_select_int[i]
            value = reg_value[i]
            expect_data = reg_data[i]

            r_enum = Device.OutReport(0)
            r_enum.set_reg(select_enum, value)
            r_int = Device.OutReport(0)
            r_int.set_reg(select_int, value)
            
            self.assertListEqual(r_enum.get_data(), expect_data)
            self.assertListEqual(r_int.get_data(), expect_data)

    def test_SetRegMultiple(self):
        values = [1, 2, 3, 4]
        expect_data = [0, 1, 2, 3, 4]

        r = Device.OutReport(0)
        for i in range(0, 4):
            r.set_reg(i, values[i])

        self.assertListEqual(r.get_data(), expect_data)

    def test_GetRegSingle(self):
        select_enum = [
            Device.OutReport.HidReg.HID_OR0,
            Device.OutReport.HidReg.HID_OR1,
            Device.OutReport.HidReg.HID_OR2,
            Device.OutReport.HidReg.HID_OR3,
        ]
        expect_values = [1, 2, 3, 4]

        for i in range(0, 4):
            r = Device.OutReport(0)
            r.set_reg(i, expect_values[i])
            
            self.assertEqual(r.get_reg(select_enum[i]), expect_values[i])
            self.assertEqual(r.get_reg(i), expect_values[i])

    def test_GetRegMultiple(self):
        select_enum = [
            Device.OutReport.HidReg.HID_OR0,
            Device.OutReport.HidReg.HID_OR1,
            Device.OutReport.HidReg.HID_OR2,
            Device.OutReport.HidReg.HID_OR3,
        ]
        expect_values = [1, 2, 3, 4]

        r = Device.OutReport(0)
        for i in range(0, 4):
            r.set_reg(i, expect_values[i])

        for k in range(0, 4):
            self.assertEqual(r.get_reg(select_enum[k]), expect_values[k])
            self.assertEqual(r.get_reg(k), expect_values[k])

class TestEepromOutReport(unittest.TestCase):
    def test_GetData(self):
        expect_mode = 0x80
        expect_report_num = 0
        expect_data = [expect_report_num, expect_mode, 0, 0, 0]

        r = Device.EepromOutReport()
        self.assertListEqual(r.get_data(), expect_data)

    def test_SetCtrlAddressRange(self):
        expect_pass_addr = 0x3F
        expect_fail_addr = 0x40

        r = Device.EepromOutReport()

        try:
            r.set_eeprom_ctrl(expect_pass_addr, False)
        except:
            self.fail()

        self.assertRaises(ValueError, r.set_eeprom_ctrl, expect_fail_addr, False)

    def test_SetCtrlReadAccess(self):
        expect_access = 0x80
        
        r = Device.EepromOutReport()
        r.set_eeprom_ctrl(0, False)

        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR3), expect_access)

    def test_SetCtrlWriteAccess(self):
        expect_access = 0xC0
        
        r = Device.EepromOutReport()
        r.set_eeprom_ctrl(0, True)

        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR3), expect_access)

    def test_SetData16ValueRange(self):
        expect_pass_value = 0xFFFF
        expect_fail_value = 0x10000

        r = Device.EepromOutReport()

        try:
            r.set_eeprom_data16(expect_pass_value)
        except:
            self.fail()

        self.assertRaises(ValueError, r.set_eeprom_data16, expect_fail_value)

    def test_SetData16ValuePosition(self):
        expect_data_high = 0x12
        expect_data_low = 0x34
        expect_data = 0x1234

        r = Device.EepromOutReport()
        r.set_eeprom_data16(expect_data)

        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR1), expect_data_low)
        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR2), expect_data_high)

    def test_SetData8ValueRange(self):
        expect_pass_value = [0xFF, 0xFF]
        expect_fail_value1 = [0xFF]
        expect_fail_value2 = [0xFF, 0xFF, 0xFF]
        expect_fail_value3 = [0x100, 0xFF]
        expect_fail_value4 = [0xFF, 0x100]

        r = Device.EepromOutReport()

        try:
            r.set_eeprom_data8(expect_pass_value)
        except:
            self.fail()

        self.assertRaises(ValueError, r.set_eeprom_data8, expect_fail_value1)
        self.assertRaises(ValueError, r.set_eeprom_data8, expect_fail_value2)
        self.assertRaises(ValueError, r.set_eeprom_data8, expect_fail_value3)
        self.assertRaises(ValueError, r.set_eeprom_data8, expect_fail_value4)

    def test_SetData8ValuePosition(self):
        expect_data_0 = 0x12
        expect_data_1 = 0x34

        r = Device.EepromOutReport()
        r.set_eeprom_data8([expect_data_0, expect_data_1])

        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR1), expect_data_0)
        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR2), expect_data_1)

    def test_GetData16ValueReadback(self):
        expect_value = 0x1234

        r = Device.EepromOutReport()
        r.set_eeprom_data16(expect_value)

        self.assertEqual(r.get_eeprom_data16(), expect_value)

    def test_GetData8ValueReadback(self):
        expect_value = [0x12, 0x34]

        r = Device.EepromOutReport()
        r.set_eeprom_data8(expect_value)

        self.assertListEqual(r.get_eeprom_data8(), expect_value)

class TestEepromReadOutReport(unittest.TestCase):
    def test_AddressRange(self):
        expect_pass_addr = 0x3F
        expect_fail_addr = 0x40

        try:
            r = Device.EepromReadOutReport(expect_pass_addr)
        except:
            self.fail()

        self.assertRaises(ValueError, Device.EepromReadOutReport, expect_fail_addr)

    def test_GetData(self):
        expect_addr = 0x12
        expect_access = 0x80
        expect_data = [0, 0x80, 0x00, 0x00, expect_access + expect_addr]

        r = Device.EepromReadOutReport(expect_addr)

        self.assertListEqual(r.get_data(), expect_data)

class TestEepromWrite16OutReport(unittest.TestCase):
    def test_AddressRange(self):
        expect_pass_addr = 0x3F
        expect_fail_addr = 0x40

        try:
            r = Device.EepromWrite16OutReport(expect_pass_addr, 0)
        except:
            self.fail()

        self.assertRaises(ValueError, Device.EepromWrite16OutReport, expect_fail_addr, 0)

    def test_GetData(self):
        expect_addr = 0x12
        expect_access = 0xC0
        expect_value = 0x1234
        expect_data = [0, 0x80, expect_value & 0xFF, expect_value >> 8, expect_access + expect_addr]

        r = Device.EepromWrite16OutReport(expect_addr, expect_value)

        self.assertListEqual(r.get_data(), expect_data)

class TestEepromWrite8OutReport(unittest.TestCase):
    def test_AddressRange(self):
        expect_pass_addr = 0x3F
        expect_fail_addr = 0x40

        try:
            r = Device.EepromWrite8OutReport(expect_pass_addr, [0, 0])
        except:
            self.fail()

        self.assertRaises(ValueError, Device.EepromWrite8OutReport, expect_fail_addr, [0, 0])

    def test_GetData(self):
        expect_addr = 0x12
        expect_access = 0xC0
        expect_value = [0x12, 0x34]
        expect_data = [0, 0x80, expect_value[0], expect_value[1], expect_access + expect_addr]

        r = Device.EepromWrite8OutReport(expect_addr, expect_value)

        self.assertListEqual(r.get_data(), expect_data)

class TestGpioOutReport(unittest.TestCase):
    def test_AccessMode(self):
        expect_mode = 0x00
        expect_report_num = 0
        expect_data = [expect_report_num, expect_mode, 0, 0 ,0]

        r = Device.GpioOutReport()
        self.assertListEqual(r.get_data(), expect_data)

    def test_SetSpdifStatusRange(self):
        expect_data_pass = 0x0F
        expect_data_fail = 0x10
        expect_cat_pass = 0xFF
        expect_cat_fail = 0x100

        r = Device.GpioOutReport()

        try:
            r.set_spdif_status(False, expect_data_pass, expect_cat_pass)
        except:
            self.fail()

        self.assertRaises(ValueError, r.set_spdif_status, False, expect_data_pass, expect_cat_fail)
        self.assertRaises(ValueError, r.set_spdif_status, False, expect_data_fail, expect_cat_pass)
        self.assertRaises(ValueError, r.set_spdif_status, False, expect_data_fail, expect_cat_fail)

    def test_SetSpdifStatusPosition(self):
        expect_mode_0 = 0x00
        expect_mode_1 = 0x09
        expect_mode_2 = 0x19

        r0 = Device.GpioOutReport()
        r1 = Device.GpioOutReport()
        r2 = Device.GpioOutReport()

        r0.set_spdif_status(False, 0x00, 0)
        r1.set_spdif_status(False, 0x09, 0)
        r2.set_spdif_status(True, 0x09, 0)

        self.assertEqual(r0.get_reg(Device.OutReport.HidReg.HID_OR0), expect_mode_0)
        self.assertEqual(r1.get_reg(Device.OutReport.HidReg.HID_OR0), expect_mode_1)
        self.assertEqual(r2.get_reg(Device.OutReport.HidReg.HID_OR0), expect_mode_2)

    def test_GetSpdifStatusValid(self):
        expect_valid_0 = False
        expect_valid_1 = True

        r0 = Device.GpioOutReport()
        r1 = Device.GpioOutReport()

        r0.set_spdif_status(expect_valid_0, 0, 0)
        r1.set_spdif_status(expect_valid_1, 0, 0)

        self.assertEqual(r0.get_spdif_status_valid(), expect_valid_0)
        self.assertEqual(r1.get_spdif_status_valid(), expect_valid_1)

    def test_GetSpdifStatusData(self):
        expect_data_0 = 0x00
        expect_data_1 = 0x09

        r0 = Device.GpioOutReport()
        r1 = Device.GpioOutReport()

        r0.set_spdif_status(False, expect_data_0, 0)
        r1.set_spdif_status(False, expect_data_1, 0)

        self.assertEqual(r0.get_spdif_status_data(), expect_data_0)
        self.assertEqual(r1.get_spdif_status_data(), expect_data_1)

    def test_GetSpdifStatusCat(self):
        expect_cat_0 = 0x00
        expect_cat_1 = 0xFF

        r0 = Device.GpioOutReport()
        r1 = Device.GpioOutReport()

        r0.set_spdif_status(False, 0, expect_cat_0)
        r1.set_spdif_status(False, 0, expect_cat_1)

        self.assertEqual(r0.get_spdif_status_cat(), expect_cat_0)
        self.assertEqual(r1.get_spdif_status_cat(), expect_cat_1)

    def test_SetGpioDataRegRange(self):
        expect_value_pass = 0x0F
        expect_value_fail = 0x10

        r = Device.GpioOutReport()

        try:
            r.set_gpio_data_reg(expect_value_pass)
        except ValueError:
            self.fail()

        self.assertRaises(ValueError, r.set_gpio_data_reg, expect_value_fail)

    def test_SetGpioDataRegPosition(self):
        expect_value = 0x09

        r = Device.GpioOutReport()
        r.set_gpio_data_reg(expect_value)

        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR1), expect_value)

    def test_GetGpioDataReg(self):
        expect_value = 0x0F

        r = Device.GpioOutReport()
        r.set_gpio_data_reg(expect_value)

        self.assertEqual(r.get_gpio_data_reg(), expect_value)

    def test_SetGpioDirRegRange(self):
        expect_value_pass = 0x0F
        expect_value_fail = 0x10

        r = Device.GpioOutReport()

        try:
            r.set_gpio_dir_reg(expect_value_pass)
        except ValueError:
            self.fail()

        self.assertRaises(ValueError, r.set_gpio_dir_reg, expect_value_fail)

    def test_SetGpioDirRegPosition(self):
        expect_dir = 0x09

        r = Device.GpioOutReport()
        r.set_gpio_dir_reg(expect_dir)

        self.assertEqual(r.get_reg(Device.OutReport.HidReg.HID_OR2), expect_dir)

    def test_GetGpioDirReg(self):
        expect_dir = 0x0F

        r = Device.GpioOutReport()
        r.set_gpio_dir_reg(expect_dir)

        self.assertEqual(r.get_gpio_dir_reg(), expect_dir)

class TestInReport(unittest.TestCase):
    def test_GetData(self):
        expect_report_num = 1
        expect_data_len = 5
        expect_data = [expect_report_num, 0, 0, 0, 0]

        r = Device.InReport(expect_data)
        self.assertEqual(len(r.get_data()), expect_data_len)
        self.assertListEqual(r.get_data(), expect_data)

    def test_Regs(self):
        expect_hid_ir0 = 0
        expect_hid_ir1 = 1
        expect_hid_ir2 = 2
        expect_hid_ir3 = 3

        actual_hid_ir0 = Device.InReport.HidReg.HID_IR0
        actual_hid_ir1 = Device.InReport.HidReg.HID_IR1
        actual_hid_ir2 = Device.InReport.HidReg.HID_IR2
        actual_hid_ir3 = Device.InReport.HidReg.HID_IR3

        self.assertEqual(actual_hid_ir0, expect_hid_ir0)
        self.assertEqual(actual_hid_ir1, expect_hid_ir1)
        self.assertEqual(actual_hid_ir2, expect_hid_ir2)
        self.assertEqual(actual_hid_ir3, expect_hid_ir3)

    def test_GetReg(self):
        select_enum = [
            Device.InReport.HidReg.HID_IR0,
            Device.InReport.HidReg.HID_IR1,
            Device.InReport.HidReg.HID_IR2,
            Device.InReport.HidReg.HID_IR3,
        ]
        expect_values = [1, 2, 3, 4]
        expect_data = [0] + expect_values

        for i in range(0, 4):
            r = Device.InReport(expect_data)
            
            self.assertEqual(r.get_reg(select_enum[i]), expect_values[i])
            self.assertEqual(r.get_reg(i), expect_values[i])

class TestEepromInReport(unittest.TestCase):
    def test_GetData16(self):
        expected_data = 0x1234
        raw_report = [0, 0, expected_data & 0xFF, expected_data >> 8, 0]

        r = Device.EepromInReport(raw_report)

        self.assertEqual(r.get_eeprom_data16(), expected_data)

    def test_GetData8(self):
        expected_data = [0x12, 0x34]
        raw_report = [0, 0] + expected_data + [0]

        r = Device.EepromInReport(raw_report)

        self.assertListEqual(r.get_eeprom_data8(), expected_data)

class TestGpioInReport(unittest.TestCase):
    def test_GetButtons(self):
        expected_buttons = 0x09
        raw_data = [0, expected_buttons, 0, 0, 0]

        r = Device.GpioInReport(raw_data)

        self.assertEqual(r.get_gpio_buttons(), expected_buttons)

    def test_GetGpioDataReg(self):
        expected_data = 0x5A
        raw_data = [0, 0, expected_data, 0, 0]

        r = Device.GpioInReport(raw_data)

        self.assertEqual(r.get_gpio_data_reg(), expected_data)

class TestConfiguration(unittest.TestCase):
    def test_InitialValidStates(self):
        c = Configuration()

        self.assertFalse(c.is_magic_flags_valid())
        self.assertFalse(c.is_product_id_valid())
        self.assertFalse(c.is_vendor_id_valid())
        self.assertFalse(c.is_serial_num_valid())
        self.assertFalse(c.is_product_name_valid())
        self.assertFalse(c.is_manufacturer_name_valid())
        self.assertFalse(c.is_dac_volume_valid())
        self.assertFalse(c.is_adc_volume_valid())
        self.assertFalse(c.is_config_bits_valid())

    def test_SetGetMagicFlags(self):
        data_matrix = [
            # Cfg,  Manuf, Ser,   Prod,  Result
            [False, False, False, False, 0x6700],
            [False, False, False, True,  0x6701],
            [False, False, True,  False, 0x6702],
            [False, False, True,  True,  0x6703],
            [False, True,  False, False, 0x6704],
            [False, True,  False, True,  0x6705],
            [False, True,  True,  False, 0x6706],
            [False, True,  True,  True,  0x6707],
            [True,  False, False, False, 0x6708],
            [True,  False, False, True,  0x6709],
            [True,  False, True,  False, 0x670A],
            [True,  False, True,  True,  0x670B],
            [True,  True,  False, False, 0x670C],
            [True,  True,  False, True,  0x670D],
            [True,  True,  True,  False, 0x670E],
            [True,  True,  True,  True,  0x670F],
        ]

        for d in data_matrix:
            expected = d[4]

            c = Configuration()
            c.set_magic_flags(d[0], d[1], d[2], d[3])
            actual = c.get_magic_flags()
            
            self.assertTrue(c.is_magic_flags_valid())
            self.assertEqual(actual, expected)

    def test_ClearMagicFlags(self):
        c = Configuration()

        c.set_magic_flags(True, True, True, True)
        self.assertTrue(c.is_magic_flags_valid())
        c.clear_magic_flags()
        self.assertFalse(c.is_magic_flags_valid())

    def test_SetVendorIdRange(self):
        expect_vid_fail = 0x10000
        expect_vid_pass = 0xFFFF

        c1 = Configuration()
        try:
            c1.set_vendor_id(expect_vid_pass)
        except ValueError:
            self.fail()

        c2 = Configuration()
        self.assertRaises(ValueError, c2.set_vendor_id, expect_vid_fail)

    def test_SetGetVendorId(self):
        for i in range(0, 0x10000):
            c = Configuration()
            c.set_vendor_id(i)

            self.assertTrue(c.is_vendor_id_valid())
            self.assertEqual(c.get_vendor_id(), i)

    def test_SetProductIdRange(self):
        expect_pid_fail = 0x10000
        expect_pid_pass = 0xFFFF

        c1 = Configuration()
        try:
            c1.set_product_id(expect_pid_pass)
        except ValueError:
            self.fail()

        c2 = Configuration()
        self.assertRaises(ValueError, c2.set_product_id, expect_pid_fail)

    def test_SetGetProductId(self):
        for i in range(0, 0x10000):
            c = Configuration()
            c.set_product_id(i)

            self.assertTrue(c.is_product_id_valid())
            self.assertEqual(c.get_product_id(), i)

    def test_SetSerialNumLengthRange(self):
        expect_serial_pass = 'p' * 13
        expect_serial_fail = 'f' * 14

        c1 = Configuration()
        try:
            c1.set_serial_num(expect_serial_pass)
        except ValueError:
            self.fail()

        c2 = Configuration()
        self.assertRaises(ValueError, c2.set_serial_num, expect_serial_fail)

    def test_SetGetSerialNum(self):
        expect = 'Test1234'

        c = Configuration()
        c.set_serial_num(expect)
        actual = c.get_serial_num()

        self.assertTrue(c.is_serial_num_valid())
        self.assertEqual(actual, expect)

    def test_SetProductNameLengthRange(self):
        expect_name_pass = 'p' * 16
        expect_name_fail = 'f' * 17

        c1 = Configuration()
        try:
            c1.set_product_name(expect_name_pass)
        except ValueError:
            self.fail()

        c2 = Configuration()
        self.assertRaises(ValueError, c2.set_product_name, expect_name_fail)

    def test_SetGetProductName(self):
        expect = 'Test1234'

        c = Configuration()
        c.set_product_name(expect)
        actual = c.get_product_name()

        self.assertTrue(c.is_product_name_valid())
        self.assertEqual(actual, expect)

    def test_SetManufNameLengthRange(self):
        expect_name_pass = 'p' * 16
        expect_name_fail = 'f' * 17

        c1 = Configuration()
        try:
            c1.set_manufacturer_name(expect_name_pass)
        except ValueError:
            self.fail()

        c2 = Configuration()
        self.assertRaises(ValueError, c2.set_manufacturer_name, expect_name_fail)

    def test_SetGetManufName(self):
        expect = 'Test1234'

        c = Configuration()
        c.set_manufacturer_name(expect)
        actual = c.get_manufacturer_name()

        self.assertTrue(c.is_manufacturer_name_valid())
        self.assertEqual(actual, expect)

    def test_SetDacVolumeRange(self):
        expect_value_fail1 = 0x01
        expect_value_pass1 = 0x02
        expect_value_pass2 = 0x4A
        expect_value_fail2 = 0x4B

        for expect_value_pass in [expect_value_pass1, expect_value_pass2]:
            c_pass = Configuration()
            try:
                c_pass.set_dac_volume(expect_value_pass)
            except ValueError:
                self.fail()

        for expect_value_fail in [expect_value_fail1, expect_value_fail2]:
            c_fail = Configuration()
            self.assertRaises(ValueError, c_fail.set_dac_volume, expect_value_fail)

    def test_SetGetDacVolume(self):
        for expect in range(0x02, 0x4A + 1):
            c = Configuration()
            c.set_dac_volume(expect)
            actual = c.get_dac_volume()

            self.assertTrue(c.is_dac_volume_valid())
            self.assertEqual(actual, expect)

    def test_SetAdcVolumeRange(self):
        expect_value_pass = 0x78
        expect_value_fail = 0x79

        c1 = Configuration()
        try:
            c1.set_adc_volume(expect_value_pass)
        except ValueError:
            self.fail()

        c2 = Configuration()
        self.assertRaises(ValueError, c2.set_adc_volume, expect_value_fail)

    def test_SetGetAdcVolume(self):
        for expect in range(0, 0x78 + 1):
            c = Configuration()
            c.set_adc_volume(expect)
            actual = c.get_adc_volume()

            self.assertTrue(c.is_adc_volume_valid())
            self.assertEqual(actual, expect)

    def test_SetGetConfigBits(self):
        data_matrix = []

        for i in range(0, 2**8):
            shdn_dac: bool = bool(i & (1 << 7))
            total_pwr_ctl: bool = bool(i & (1 << 6))
            mic_hp: bool = bool(i & (1 << 5))
            adc_sync: bool = bool(i & (1 << 4))
            mic_boost: bool = bool(i & (1 << 3))
            dac_out_hp: bool = bool(i & (1 << 2))
            hid_en: bool = bool(i & (1 << 1))
            remote_wkup_en: bool = bool(i & (1 << 0))
            
            result = (shdn_dac << 8) | (total_pwr_ctl << 7) | (mic_hp << 5) | (adc_sync << 4) | (mic_boost << 3) | (dac_out_hp << 2) | (hid_en << 1) | (remote_wkup_en << 0)

            data_matrix = data_matrix + [[shdn_dac, total_pwr_ctl, mic_hp, adc_sync, mic_boost, dac_out_hp, hid_en, remote_wkup_en, result]]

        for d in data_matrix:
            shdn_dac = d[0]
            total_pwr_ctl = d[1]
            mic_hp = d[2]
            adc_sync = d[3]
            mic_boost = d[4]
            dac_out_hp = d[5]
            hid_en = d[6]
            remote_wkup_en = d[7]
            expect = d[8]

            c = Configuration()
            c.set_config_bits(shdn_dac, total_pwr_ctl, mic_hp, adc_sync, mic_boost, dac_out_hp, hid_en, remote_wkup_en)
            actual = c.get_config_bits()

            self.assertTrue(c.is_config_bits_valid())
            self.assertEqual(actual, expect)

class TestConfigurationSerializer(unittest.TestCase):
    def test_SerializeDefault(self):
        c = Configuration()
        s = ConfigurationSerializer(c)

        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS 
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeMagicFlags(self):
        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[0] = 0x6700
        
        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_magic_flags()
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeVendorId(self):
        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[1] = 0x1234

        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_vendor_id(0x1234)
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeProductId(self):
        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[2] = 0x1234

        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_product_id(0x1234)
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeSerialNum(self):
        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[3] = 10        | (ord(b'T') << 8)
        expect[4] = ord(b'e') | (ord(b's') << 8)
        expect[5] = ord(b't') | (0 << 8)

        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_serial_num('Test')
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeProductName(self):
        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[10] = 10        | (ord(b'T') << 8)
        expect[11] = ord(b'e') | (ord(b's') << 8)
        expect[12] = ord(b't') | (0 << 8)

        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_product_name('Test')
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeManufName(self):
        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[26] = 10        | (ord(b'T') << 8)
        expect[27] = ord(b'e') | (ord(b's') << 8)
        expect[28] = ord(b't') | (0 << 8)

        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_manufacturer_name('Test')
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeAdcDacVolume(self):
        adc_volume = 0x12
        dac_volume = 0x34

        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[42] = adc_volume | (dac_volume << 8)

        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_adc_volume(adc_volume)
        c.set_dac_volume(dac_volume)
        actual = s.serialize()

        self.assertListEqual(actual, expect)

    def test_SerializeConfigBits(self):
        expect = [0xFFFF] * Device._MEMORY_SIZE_WORDS
        expect[43] = 0x002A

        c = Configuration()
        s = ConfigurationSerializer(c)

        c.set_config_bits()
        actual = s.serialize()

        self.assertListEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()