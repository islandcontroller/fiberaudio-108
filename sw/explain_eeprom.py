"""
CM108B EEPROM DECODER + USER-FRIENDLY SUMMARY (datasheet-oriented)

EEPROM device : 93C46
Physical size : 64 x 16-bit words
CM108B usage  : 0x00 – 0x32 (51 words) per table; rest reserved/unused

Important quirk:
- String headers store FIRST CHARACTER in [15:8], length in [7:0]
- String data words store characters in "low byte then high byte" order (byte-swapped per 16-bit word)

Missing words in input 'data' are treated as erased EEPROM (0xFFFF).
"""

# ============================================================
# Constants
# ============================================================

MAX_DEFINED_ADDR = 0x32
ERASED_WORD = 0xFFFF


# ============================================================
# Bit helpers
# ============================================================

def bit(val, n):
    return (val >> n) & 1


def bits(val, hi, lo):
    return (val >> lo) & ((1 << (hi - lo + 1)) - 1)


# ============================================================
# Safe EEPROM read
# ============================================================

def get_word(data, addr):
    """Return EEPROM word at addr or ERASED_WORD if not present in input."""
    if addr < len(data):
        return data[addr]
    return ERASED_WORD


# ============================================================
# String decoding (data block only, not header)
# ============================================================

def decode_ascii_string_block(data, start, end):
    """
    Decode ASCII string stored in word array start..end (inclusive).
    CM108B data block byte order: LOW byte first char, HIGH byte second char.
    """
    chars = []
    for addr in range(start, end + 1):
        val = get_word(data, addr)
        if val == ERASED_WORD:
            continue

        lo = bits(val, 7, 0)    # FIRST char
        hi = bits(val, 15, 8)   # SECOND char

        if lo not in (0x00, 0xFF):
            chars.append(chr(lo))
        if hi not in (0x00, 0xFF):
            chars.append(chr(hi))

    return "".join(chars).rstrip("\x00")


def combine_header_char_and_block(first_char, block_string):
    """
    Combine header first_char (may be None) with block_string.
    Avoid double-prefix if block already starts with that char.
    """
    if not first_char:
        return block_string or ""

    if not block_string:
        return first_char

    # If already starts with the same char, don't double it.
    if block_string[0] == first_char:
        return block_string

    return first_char + block_string


# ============================================================
# Global summary state
# ============================================================

SUMMARY = {
    # IDs
    "vid": None,
    "pid": None,

    # 0x00
    "magic": None,
    "config_valid": None,
    "serial_enable": None,
    "reserved2": None,
    "reserved0": None,

    # headers
    "serial_first": None,
    "serial_len": None,
    "product_first": None,
    "product_len": None,
    "manufacturer_first": None,
    "manufacturer_len": None,

    # strings (final combined)
    "serial": None,
    "product": None,
    "manufacturer": None,

    # 0x2A
    "dac_init": None,
    "adc_init": None,
    "dac_limits_valid": None,
    "adc_limits_valid": None,
    "aa_limits_valid": None,

    # 0x2B
    "aa_init": None,
    "boost_mode": None,
    "dac_analog_off": None,
    "total_power_ctrl": None,
    "mic_highpass": None,
    "mic_pll_adjust": None,
    "mic_boost": None,
    "output_terminal": None,
    "hid_enable": None,
    "remote_wakeup": None,

    # limits
    "dac_min": None,
    "dac_max": None,
    "adc_min": None,
    "adc_max": None,
    "aa_min": None,
    "aa_max": None,

    # option2
    "option2": None,
}


# ============================================================
# Register decoders (verbose + fill SUMMARY)
# ============================================================

def decode_0x00(val):
    SUMMARY["magic"] = bits(val, 15, 4)
    SUMMARY["config_valid"] = bool(bit(val, 3))
    SUMMARY["reserved2"] = bit(val, 2)
    SUMMARY["serial_enable"] = bool(bit(val, 1))
    SUMMARY["reserved0"] = bit(val, 0)

    print("  Control / Magic word")
    print(f"    [15:4] Magic word           = 0x{SUMMARY['magic']:03X}")
    print(f"    [3]    Config valid         = {bit(val,3)}")
    print(f"    [2]    Reserved             = {bit(val,2)} (should be 1)")
    print(f"    [1]    Serial number enable = {bit(val,1)}")
    print(f"    [0]    Reserved             = {bit(val,0)} (should be 1)")


def decode_vid(val):
    SUMMARY["vid"] = val
    print(f"  USB Vendor ID  = 0x{val:04X}")


def decode_pid(val):
    SUMMARY["pid"] = val
    print(f"  USB Product ID = 0x{val:04X}")


def decode_0x03(val):
    # per table: [15:8] first character, [7:0] length
    SUMMARY["serial_first"] = chr(bits(val, 15, 8)) if bits(val, 15, 8) not in (0x00, 0xFF) else None
    SUMMARY["serial_len"] = bits(val, 7, 0)

    print("  Serial number header")
    print(f"    [15:8] First character = {repr(SUMMARY['serial_first'])}")
    print(f"    [7:0]  Length          = {SUMMARY['serial_len']} bytes")


def decode_0x0A(val):
    SUMMARY["product_first"] = chr(bits(val, 15, 8)) if bits(val, 15, 8) not in (0x00, 0xFF) else None
    SUMMARY["product_len"] = bits(val, 7, 0)

    print("  Product string header")
    print(f"    [15:8] First character = {repr(SUMMARY['product_first'])}")
    print(f"    [7:0]  Length          = {SUMMARY['product_len']} bytes")


def decode_0x1A(val):
    SUMMARY["manufacturer_first"] = chr(bits(val, 15, 8)) if bits(val, 15, 8) not in (0x00, 0xFF) else None
    SUMMARY["manufacturer_len"] = bits(val, 7, 0)

    print("  Manufacturer string header")
    print(f"    [15:8] First character = {repr(SUMMARY['manufacturer_first'])}")
    print(f"    [7:0]  Length          = {SUMMARY['manufacturer_len']} bytes")


def decode_0x2A(val):
    dac = bits(val, 15, 9)
    adc = bits(val, 8, 3)

    SUMMARY["dac_init"] = dac
    SUMMARY["adc_init"] = adc
    SUMMARY["dac_limits_valid"] = bool(bit(val, 2))
    SUMMARY["adc_limits_valid"] = bool(bit(val, 1))
    SUMMARY["aa_limits_valid"] = bool(bit(val, 0))

    print("  Initial volumes")
    print(f"    [15:9] DAC initial volume = {dac}")
    print(f"    [8:3]  ADC initial volume = {adc}")
    print(f"    [2]    DAC EEPROM MAX/MIN valid = {bit(val,2)}")
    print(f"    [1]    ADC EEPROM MAX/MIN valid = {bit(val,1)}")
    print(f"    [0]    AA  EEPROM MAX/MIN valid = {bit(val,0)}")


def decode_0x2B(val):
    SUMMARY["aa_init"] = bits(val, 15, 11)
    SUMMARY["boost_mode"] = "12 dB" if bit(val, 9) else "22 dB"
    SUMMARY["dac_analog_off"] = bool(bit(val, 8))
    SUMMARY["total_power_ctrl"] = bool(bit(val, 7))
    SUMMARY["mic_highpass"] = bool(bit(val, 5))
    SUMMARY["mic_pll_adjust"] = bool(bit(val, 4))
    SUMMARY["mic_boost"] = bool(bit(val, 3))
    SUMMARY["output_terminal"] = "Headset" if bit(val, 2) else "Speaker"
    SUMMARY["hid_enable"] = bool(bit(val, 1))
    SUMMARY["remote_wakeup"] = bool(bit(val, 0))

    print("  Audio / MIC control")
    print(f"    [15:11] AA initial volume = {SUMMARY['aa_init']}")
    print(f"    [9]     Boost mode        = {SUMMARY['boost_mode']}")
    print(f"    [8]     DAC analog off    = {int(SUMMARY['dac_analog_off'])}")
    print(f"    [7]     Total power ctrl  = {int(SUMMARY['total_power_ctrl'])}")
    print(f"    [5]     MIC High Pass     = {int(SUMMARY['mic_highpass'])}")
    print(f"    [4]     MIC PLL adjust    = {int(SUMMARY['mic_pll_adjust'])}")
    print(f"    [3]     MIC Boost         = {int(SUMMARY['mic_boost'])}")
    print(f"    [2]     Output terminal   = {SUMMARY['output_terminal']}")
    print(f"    [1]     HID enable        = {int(SUMMARY['hid_enable'])}")
    print(f"    [0]     Remote wakeup     = {int(SUMMARY['remote_wakeup'])}")


def decode_volume(which, val):
    # Store raw (you can later add formula if you want)
    SUMMARY[which] = val
    print(f"  {which} = 0x{val:04X}")


def decode_0x32(val):
    SUMMARY["option2"] = val
    print("  OPTION2 register")
    print(f"    RAW = 0x{val:04X}")
    print(f"    [3] Reserved = {bit(val,3)} (should be 0)")
    print(f"    [2] Reserved = {bit(val,2)} (should be 0)")
    print(f"    [1:0] Value  = {bits(val,1,0)}")


# ============================================================
# dB helpers (keep as “approx” unless you have exact table)
# ============================================================

def approx_dac_db(code):
    # Your earlier mapping idea; mark as approximate
    return -70 + code


def approx_adc_db(code):
    # Your earlier mapping idea; mark as approximate
    return code - 8


# ============================================================
# Main decoder
# ============================================================

def decode_eeprom(data):
    print("CM108B EEPROM decode")
    print("====================")

    for addr in range(0x00, MAX_DEFINED_ADDR + 1):
        val = get_word(data, addr)
        print(f"\nAddress 0x{addr:02X} = 0x{val:04X}")

        # Missing in data => treat as erased/defaults
        if addr >= len(data):
            print("  Not present in data › treated as erased EEPROM (0xFFFF)")
            print("  Meaning: CM108B uses internal default for this field")
            continue

        # String blocks (decoded as one line, but we still print at the block start)
        if addr == 0x04:
            block = decode_ascii_string_block(data, 0x04, 0x09)
            combined = combine_header_char_and_block(SUMMARY["serial_first"], block)
            SUMMARY["serial"] = combined if combined else None
            print(f"  Serial number (combined): \"{combined}\"" if combined else "  Serial number: <not set>")
            continue

        if addr == 0x0B:
            block = decode_ascii_string_block(data, 0x0B, 0x19)
            combined = combine_header_char_and_block(SUMMARY["product_first"], block)
            SUMMARY["product"] = combined if combined else None
            print(f"  Product string (combined): \"{combined}\"" if combined else "  Product string: <not set>")
            continue

        if addr == 0x1B:
            block = decode_ascii_string_block(data, 0x1B, 0x29)
            combined = combine_header_char_and_block(SUMMARY["manufacturer_first"], block)
            SUMMARY["manufacturer"] = combined if combined else None
            print(f"  Manufacturer string (combined): \"{combined}\"" if combined else "  Manufacturer string: <not set>")
            continue

        # Erased but present
        if val == ERASED_WORD:
            print("  Erased EEPROM word › CM108B uses internal default")
            continue

        # Single register decode
        if addr == 0x00:
            decode_0x00(val)
        elif addr == 0x01:
            decode_vid(val)
        elif addr == 0x02:
            decode_pid(val)
        elif addr == 0x03:
            decode_0x03(val)
        elif addr == 0x0A:
            decode_0x0A(val)
        elif addr == 0x1A:
            decode_0x1A(val)
        elif addr == 0x2A:
            decode_0x2A(val)
        elif addr == 0x2B:
            decode_0x2B(val)
        elif addr == 0x2C:
            decode_volume("dac_min", val)
        elif addr == 0x2D:
            decode_volume("dac_max", val)
        elif addr == 0x2E:
            decode_volume("adc_min", val)
        elif addr == 0x2F:
            decode_volume("adc_max", val)
        elif addr == 0x30:
            decode_volume("aa_min", val)
        elif addr == 0x31:
            decode_volume("aa_max", val)
        elif addr == 0x32:
            decode_0x32(val)
        else:
            print("  Reserved / unused")

    print_summary(data)


# ============================================================
# Summary (user-friendly + still byte/bit specific)
# ============================================================

def _present_or_default(addr, data):
    """Helper text for summary: was this word present or missing?"""
    if addr >= len(data):
        return "missing in input › treated as 0xFFFF (defaults)"
    v = data[addr]
    if v == ERASED_WORD:
        return "0xFFFF (erased) › defaults"
    return f"0x{v:04X}"


def print_summary(data):
    print("\n")
    print("========== EEPROM SUMMARY ==========")

    # Strings (combined with header first char)
    manu = SUMMARY["manufacturer"] or ""
    prod = SUMMARY["product"] or ""
    ser  = SUMMARY["serial"] or ""

    print(f"Manufacturer : {repr(manu) if manu else '<not set>'}  (header 0x1A={_present_or_default(0x1A, data)}, block 0x1B..0x29)")
    print(f"Product      : {repr(prod) if prod else '<not set>'}  (header 0x0A={_present_or_default(0x0A, data)}, block 0x0B..0x19)")
    print(f"Serial       : {repr(ser)  if ser  else 'not set'}    (header 0x03={_present_or_default(0x03, data)}, block 0x04..0x09)")

    # IDs
    vid = SUMMARY["vid"]
    pid = SUMMARY["pid"]
    print(f"VID/PID      : {('0x%04X' % vid) if vid is not None else '<default/unknown>'} / {('0x%04X' % pid) if pid is not None else '<default/unknown>'}")

    # 0x00 interpretation
    if SUMMARY["magic"] is None and 0x00 < len(data) and data[0x00] == ERASED_WORD:
        print("Config word  : 0xFFFF (erased) › CM108B defaults")
    else:
        cv = SUMMARY["config_valid"]
        se = SUMMARY["serial_enable"]
        magic = SUMMARY["magic"]
        r2 = SUMMARY["reserved2"]
        r0 = SUMMARY["reserved0"]
        print(f"0x00 Control : magic=0x{magic:03X}  config_valid={int(bool(cv))}  serial_enable={int(bool(se))}  reserved2={r2}  reserved0={r0}")
        if cv:
            print("Config state : EEPROM marked as VALID custom configuration (bit3=1)")
        else:
            print("Config state : EEPROM NOT marked valid (bit3=0) › device may prefer defaults for tuning fields")

    # Volumes 0x2A
    if SUMMARY["dac_init"] is None and (0x2A >= len(data) or get_word(data, 0x2A) == ERASED_WORD):
        print(f"0x2A Volumes : {_present_or_default(0x2A, data)}")
    else:
        dac = SUMMARY["dac_init"]
        adc = SUMMARY["adc_init"]
        print("0x2A Volumes :")
        print(f"  DAC initial volume = {dac} (? {approx_dac_db(dac)} dB, approx)")
        print(f"  ADC initial volume = {adc} (? {approx_adc_db(adc)} dB, approx)")
        print(f"  Limits valid flags : DAC={int(bool(SUMMARY['dac_limits_valid']))}  ADC={int(bool(SUMMARY['adc_limits_valid']))}  AA={int(bool(SUMMARY['aa_limits_valid']))}")

    # Audio/MIC 0x2B
    if SUMMARY["aa_init"] is None and (0x2B >= len(data) or get_word(data, 0x2B) == ERASED_WORD):
        print(f"0x2B Audio   : {_present_or_default(0x2B, data)}")
    else:
        print("0x2B Audio/MIC :")
        print(f"  AA initial volume = {SUMMARY['aa_init']}")
        print(f"  Boost mode        = {SUMMARY['boost_mode']}")
        print(f"  DAC analog off    = {int(bool(SUMMARY['dac_analog_off']))}")
        print(f"  Total power ctrl  = {int(bool(SUMMARY['total_power_ctrl']))}")
        print(f"  MIC high-pass     = {int(bool(SUMMARY['mic_highpass']))}")
        print(f"  MIC PLL adjust    = {int(bool(SUMMARY['mic_pll_adjust']))}")
        print(f"  MIC boost         = {int(bool(SUMMARY['mic_boost']))}")
        print(f"  Output terminal   = {SUMMARY['output_terminal']}")
        print(f"  HID enable        = {int(bool(SUMMARY['hid_enable']))}")
        print(f"  Remote wakeup     = {int(bool(SUMMARY['remote_wakeup']))}")

    # Limits 0x2C..0x31
    print("Volume limits (if programmed):")
    for addr, name in [
        (0x2C, "DAC MIN"), (0x2D, "DAC MAX"),
        (0x2E, "ADC MIN"), (0x2F, "ADC MAX"),
        (0x30, "AA  MIN"), (0x31, "AA  MAX"),
    ]:
        print(f"  0x{addr:02X} {name}: {_present_or_default(addr, data)}")

    # OPTION2 0x32
    print(f"0x32 OPTION2 : {_present_or_default(0x32, data)}")

    # Friendly “one-liner” interpretation
    # (Strings are the biggest user-facing part)
    friendly_name = ""
    if manu and prod:
        friendly_name = f"{manu} / {prod}"
    elif manu:
        friendly_name = manu
    elif prod:
        friendly_name = prod

    if friendly_name:
        print(f"Device ID    : {friendly_name}")

    if not ser:
        print("Serial       : not set (device will report no custom serial)")

    print("====================================")
