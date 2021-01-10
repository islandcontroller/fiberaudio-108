# fiberaudio-108

A low-cost USB audio interface with S/PDIF optical output, based on the Cmedia CM108AH ASIC.

<p align="center"><img src="doc/block-schem.svg" /></p>

View [Schematic &#x1f5ce;](doc/sch_fiberaudio-108_rev3.pdf)

### Key features

* Cmedia CM108AH audio interface ASIC
* Stereo, up to 48 kHz
* USB Micro-B input
* Optical S/PDIF output (JIS F05, e.g. TOSLINK&trade;)
* USB Audio Device Class 1.0, uses generic drivers
* Configuration EEPROM

## Overview

This USB audio interface provides a low-cost S/PDIF optical output for portable computers and tablet devices. Audio tranmission via optical link - as opposed to a wired line-level connection - eliminates hum caused by ground potential differences, and noise feed-through from switched-mode power supplies.

| Design Requirement | Solution Approach |
|--------------------|-------------------|
| Provide electrical isolation between device and audio equipment | Audio signal transmission via optical link (e.g. TOSLINK&trade;) |
| Compatibility for wide range of operating systems, with minimal driver maintenance | USB Audio Device Class using OS-provided generic drivers |
| IP accessibility for PCB design files | Use of free, open-source EDA tooling (e.g. KiCad) |
| Commonly-used, small form-factor USB connector, robust enough to withstand portable use | USB **mini**-B receptacle |
| Option for manual assembly | Passives no smaller than 0603. ICs leaded and no smaller than 0.5mm pin pitch (SSOP) |
| Low PCB production capability requirements | &bullet;&nbsp;FR4 base material<br/>&bullet;&nbsp;2-layer Cu, Top+Bot Mask, Top Overlay<br/>&bullet;&nbsp;&geq;0.25mm trace-to-outline<br/>&bullet;&nbsp;&geq;0.25mm trace width and spacing<br/>&bullet;&nbsp;&geq;0.35mm drill size<br/>&bullet;&nbsp;Gerber, NC Drill and RS274X outputs |

## Licensing

If not stated otherwise within the specific file, the contents of this project are licensed under the CERN Open Hardware Licence Version 2 - Permissive. The full license text is provided in the [`LICENSE`](LICENSE) document.

        SPDX-License-Identifier: CERN-OHL-P-2.0

This licensing model is compliant with the [Open Source Hardware Definition 1.0](https://www.oshwa.org/definition/).