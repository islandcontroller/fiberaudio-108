# CM108AH EEPROM Access

The Cmedia `CM108` ASIC offers access to the attached EEPROM via an HID endpoint.
## Report data structure

Descriptions for each data byte of the in/out reports are provided in the [datasheet](cm108ah.pdf). For reference, the HID report number `0` needs to be prepended, for a total of 5 bytes per transfer.

## Read/Write access

Read/Write access modes are configured using the `HID_OR3 / EEPROM_CTRL` register. Command encoding differs from `AT93C46` access commands, as shown below.

| `EEPROM_CTRL` Bit | Descriptions                                                 |
|-------------------|--------------------------------------------------------------|
| [7:6]             | Access mode<br/>`0b10`: Read access<br/>`0b11`: Write access |
| [5:0]             | Word address A<sub>5</sub>-A<sub>0</sub>                     |

**Read access mode** will initiate an SPI transfer to the external EEPROM, containing the `READ` command, followed by 16 clocks for the resulting output word.

    > SB (0x80 + addr)    0x00       0x00
    <                  data[15:8] data[7:0]

**Write access mode** will initially transfer an `EWEN` command to the EEPROM, followed by a `WRITE` transfer for 16 data bits. The CM108 will then toggle the clock line until the EEPROM signals a `READY` state.

    > SB 0x30  //  SB (0x40 + addr) data[15:8] data[7:0] 0x00 ... 0x00
    <                                                    BUSY ... READY

**Other access mode values** seem to have no effect, and do not produce any output on the SPI bus.