EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "fiberaudio-108"
Date "2021-02-25"
Rev "5"
Comp "https://github.com/islandcontroller/fiberaudio-108"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:USB_B_Mini J1
U 1 1 5FF94988
P 1900 1750
F 0 "J1" H 1957 2217 50  0000 C CNN
F 1 "USB_B_Mini" H 1957 2126 50  0000 C CNN
F 2 "Connector_USB:USB_Mini-B_Lumberg_2486_01_Horizontal" H 2050 1700 50  0001 C CNN
F 3 "~" H 2050 1700 50  0001 C CNN
F 4 "Manual" H 1900 1750 50  0001 C CNN "Assembly"
	1    1900 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 2150 1900 2150
Connection ~ 1900 2150
$Comp
L power:GND #PWR04
U 1 1 5FF9E348
P 1900 2350
F 0 "#PWR04" H 1900 2100 50  0001 C CNN
F 1 "GND" H 1905 2177 50  0000 C CNN
F 2 "" H 1900 2350 50  0001 C CNN
F 3 "" H 1900 2350 50  0001 C CNN
	1    1900 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 2150 1900 2350
Wire Wire Line
	2350 2250 2350 2350
$Comp
L power:GND #PWR08
U 1 1 5FFA148B
P 2350 2350
F 0 "#PWR08" H 2350 2100 50  0001 C CNN
F 1 "GND" H 2355 2177 50  0000 C CNN
F 2 "" H 2350 2350 50  0001 C CNN
F 3 "" H 2350 2350 50  0001 C CNN
	1    2350 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:C C3
U 1 1 5FFA3368
P 2850 2100
F 0 "C3" H 2965 2146 50  0000 L CNN
F 1 "100nF" H 2965 2055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2888 1950 50  0001 C CNN
F 3 "~" H 2850 2100 50  0001 C CNN
F 4 "C14663" H 2850 2100 50  0001 C CNN "LCSC"
F 5 "Auto" H 2850 2100 50  0001 C CNN "Assembly"
	1    2850 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 2250 2850 2350
$Comp
L power:GND #PWR09
U 1 1 5FFA336F
P 2850 2350
F 0 "#PWR09" H 2850 2100 50  0001 C CNN
F 1 "GND" H 2855 2177 50  0000 C CNN
F 2 "" H 2850 2350 50  0001 C CNN
F 3 "" H 2850 2350 50  0001 C CNN
	1    2850 2350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR012
U 1 1 5FFA54CC
P 3350 2350
F 0 "#PWR012" H 3350 2100 50  0001 C CNN
F 1 "GND" H 3355 2177 50  0000 C CNN
F 2 "" H 3350 2350 50  0001 C CNN
F 3 "" H 3350 2350 50  0001 C CNN
	1    3350 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 2350 3350 2250
Wire Wire Line
	4450 6200 4350 6200
Wire Wire Line
	4350 6200 4350 6000
Wire Wire Line
	3750 6000 3750 6100
Wire Wire Line
	4450 6300 4350 6300
Wire Wire Line
	4350 6300 4350 6500
Wire Wire Line
	3750 6500 3750 6400
$Comp
L Device:C C6
U 1 1 5FFE1556
P 3400 6000
F 0 "C6" V 3148 6000 50  0000 C CNN
F 1 "20pF" V 3239 6000 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3438 5850 50  0001 C CNN
F 3 "~" H 3400 6000 50  0001 C CNN
F 4 "C1648" V 3400 6000 50  0001 C CNN "LCSC"
F 5 "Auto" V 3400 6000 50  0001 C CNN "Assembly"
	1    3400 6000
	0    1    1    0   
$EndComp
$Comp
L Device:C C7
U 1 1 5FFE215A
P 3400 6500
F 0 "C7" V 3148 6500 50  0000 C CNN
F 1 "20pF" V 3239 6500 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3438 6350 50  0001 C CNN
F 3 "~" H 3400 6500 50  0001 C CNN
F 4 "C1648" V 3400 6500 50  0001 C CNN "LCSC"
F 5 "Auto" V 3400 6500 50  0001 C CNN "Assembly"
	1    3400 6500
	0    1    1    0   
$EndComp
Wire Wire Line
	3250 6000 3150 6000
Wire Wire Line
	3150 6000 3150 6250
Wire Wire Line
	3150 6500 3250 6500
Wire Wire Line
	3150 6250 3050 6250
Connection ~ 3150 6250
Wire Wire Line
	3150 6250 3150 6500
$Comp
L power:GND #PWR010
U 1 1 5FFE4CE0
P 3050 6250
F 0 "#PWR010" H 3050 6000 50  0001 C CNN
F 1 "GND" V 3055 6122 50  0000 R CNN
F 2 "" H 3050 6250 50  0001 C CNN
F 3 "" H 3050 6250 50  0001 C CNN
	1    3050 6250
	0    1    1    0   
$EndComp
Connection ~ 3750 6000
Connection ~ 3750 6500
Wire Wire Line
	3550 6000 3750 6000
Wire Wire Line
	3550 6500 3750 6500
Wire Wire Line
	3750 6000 4350 6000
Wire Wire Line
	3750 6500 4350 6500
$Comp
L Device:Crystal_GND24 Y1
U 1 1 5FFEF934
P 3750 6250
F 0 "Y1" V 3704 6494 50  0000 L CNN
F 1 "12MHz" V 3795 6494 50  0000 L CNN
F 2 "Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm" H 3750 6250 50  0001 C CNN
F 3 "~" H 3750 6250 50  0001 C CNN
F 4 "C9002" V 3750 6250 50  0001 C CNN "LCSC"
F 5 "Auto" V 3750 6250 50  0001 C CNN "Assembly"
	1    3750 6250
	0    1    1    0   
$EndComp
Wire Wire Line
	3550 6250 3500 6250
Wire Wire Line
	3500 6250 3500 6200
Wire Wire Line
	3500 6200 3300 6200
Wire Wire Line
	3300 6200 3300 6250
Wire Wire Line
	3300 6250 3150 6250
Wire Wire Line
	3950 6250 3550 6250
Connection ~ 3550 6250
Wire Wire Line
	4450 3350 4350 3350
Wire Wire Line
	4350 3350 4350 3200
$Comp
L Device:C C8
U 1 1 600F9753
P 3800 4100
F 0 "C8" H 3915 4146 50  0000 L CNN
F 1 "100nF" H 3915 4055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3838 3950 50  0001 C CNN
F 3 "~" H 3800 4100 50  0001 C CNN
F 4 "C14663" H 3800 4100 50  0001 C CNN "LCSC"
F 5 "Auto" H 3800 4100 50  0001 C CNN "Assembly"
	1    3800 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 3550 3800 3950
$Comp
L power:+3.3V #PWR013
U 1 1 600FB6B9
P 3350 3200
F 0 "#PWR013" H 3350 3050 50  0001 C CNN
F 1 "+3.3V" H 3365 3373 50  0000 C CNN
F 2 "" H 3350 3200 50  0001 C CNN
F 3 "" H 3350 3200 50  0001 C CNN
	1    3350 3200
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR017
U 1 1 600FC6F9
P 4350 3200
F 0 "#PWR017" H 4350 3050 50  0001 C CNN
F 1 "+5V" H 4365 3373 50  0000 C CNN
F 2 "" H 4350 3200 50  0001 C CNN
F 3 "" H 4350 3200 50  0001 C CNN
	1    4350 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 4350 3350 4250
Wire Wire Line
	3800 4350 3800 4250
$Comp
L power:GND #PWR014
U 1 1 6010D2DF
P 3350 4350
F 0 "#PWR014" H 3350 4100 50  0001 C CNN
F 1 "GND" H 3355 4177 50  0000 C CNN
F 2 "" H 3350 4350 50  0001 C CNN
F 3 "" H 3350 4350 50  0001 C CNN
	1    3350 4350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR016
U 1 1 6010D6A5
P 3800 4350
F 0 "#PWR016" H 3800 4100 50  0001 C CNN
F 1 "GND" H 3805 4177 50  0000 C CNN
F 2 "" H 3800 4350 50  0001 C CNN
F 3 "" H 3800 4350 50  0001 C CNN
	1    3800 4350
	1    0    0    -1  
$EndComp
Connection ~ 3800 3550
Wire Wire Line
	3800 3550 4450 3550
Wire Wire Line
	3350 3200 3350 3550
Wire Wire Line
	3350 3550 3800 3550
Connection ~ 3350 3550
Wire Wire Line
	3350 3550 3350 3950
Wire Bus Line
	4250 4550 4150 4650
Entry Wire Line
	4250 4250 4350 4150
Entry Wire Line
	4250 4350 4350 4250
Entry Wire Line
	4250 4450 4350 4350
Wire Wire Line
	4350 4350 4450 4350
Wire Wire Line
	4350 4250 4450 4250
Wire Wire Line
	4350 4150 4450 4150
Wire Wire Line
	4350 4050 4450 4050
Wire Wire Line
	2850 3400 2750 3400
Wire Wire Line
	2850 3500 2750 3500
Wire Wire Line
	2850 3600 2750 3600
Wire Wire Line
	2850 3700 2750 3700
Text Label 2750 3400 0    25   ~ 0
EECS
Text Label 2750 3500 0    25   ~ 0
EESK
Text Label 2750 3600 0    25   ~ 0
EEMOSI
Text Label 2750 3700 0    25   ~ 0
EEMISO
Text Label 4350 4050 0    25   ~ 0
EECS
Text Label 4350 4150 0    25   ~ 0
EESK
Text Label 4350 4250 0    25   ~ 0
EEMOSI
Text Label 4350 4350 0    25   ~ 0
EEMISO
Wire Wire Line
	2100 3400 2000 3400
Wire Wire Line
	2100 3700 2000 3700
$Comp
L power:+3.3V #PWR05
U 1 1 6016007C
P 2000 3200
F 0 "#PWR05" H 2000 3050 50  0001 C CNN
F 1 "+3.3V" H 2015 3373 50  0000 C CNN
F 2 "" H 2000 3200 50  0001 C CNN
F 3 "" H 2000 3200 50  0001 C CNN
	1    2000 3200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR06
U 1 1 60160392
P 2000 4350
F 0 "#PWR06" H 2000 4100 50  0001 C CNN
F 1 "GND" H 2005 4177 50  0000 C CNN
F 2 "" H 2000 4350 50  0001 C CNN
F 3 "" H 2000 4350 50  0001 C CNN
	1    2000 4350
	1    0    0    -1  
$EndComp
NoConn ~ 4450 4550
Text Label 2200 1550 0    25   ~ 0
VBUS
NoConn ~ 2200 1950
NoConn ~ 4450 5350
NoConn ~ 4450 5250
Wire Wire Line
	4450 5650 4350 5650
Wire Wire Line
	4450 5550 4350 5550
Wire Wire Line
	4450 5850 4350 5850
Wire Wire Line
	4450 5750 4450 5650
$Comp
L power:GND #PWR018
U 1 1 601B62A7
P 4350 5550
F 0 "#PWR018" H 4350 5300 50  0001 C CNN
F 1 "GND" V 4355 5422 50  0000 R CNN
F 2 "" H 4350 5550 50  0001 C CNN
F 3 "" H 4350 5550 50  0001 C CNN
	1    4350 5550
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR020
U 1 1 601B6586
P 4350 5850
F 0 "#PWR020" H 4350 5600 50  0001 C CNN
F 1 "GND" V 4355 5722 50  0000 R CNN
F 2 "" H 4350 5850 50  0001 C CNN
F 3 "" H 4350 5850 50  0001 C CNN
	1    4350 5850
	0    1    1    0   
$EndComp
$Comp
L power:+3.3V #PWR019
U 1 1 601B6E8D
P 4350 5650
F 0 "#PWR019" H 4350 5500 50  0001 C CNN
F 1 "+3.3V" V 4365 5778 50  0000 L CNN
F 2 "" H 4350 5650 50  0001 C CNN
F 3 "" H 4350 5650 50  0001 C CNN
	1    4350 5650
	0    -1   -1   0   
$EndComp
Text Notes 2650 5350 0    50   ~ 0
PWRSEL=0: Bus-powered\nMODE=1: Headphones\nADSEL=1: I2S ADC\nMSEL=0: Mixer disabled
Wire Notes Line
	2600 5000 3650 5000
Wire Notes Line
	3650 5400 2600 5400
Wire Notes Line
	2600 5400 2600 5000
Wire Notes Line
	3950 5450 4350 5450
Wire Notes Line
	4350 5450 4350 5950
Wire Notes Line
	4350 5950 3950 5950
Wire Notes Line
	3950 5950 3950 5450
Wire Wire Line
	4450 6650 4450 6750
Wire Wire Line
	4450 6750 4350 6750
Wire Wire Line
	4350 6750 4350 6900
$Comp
L power:GND #PWR021
U 1 1 601ECAAF
P 4350 6900
F 0 "#PWR021" H 4350 6650 50  0001 C CNN
F 1 "GND" H 4355 6727 50  0000 C CNN
F 2 "" H 4350 6900 50  0001 C CNN
F 3 "" H 4350 6900 50  0001 C CNN
	1    4350 6900
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 3450 5450 3350
Wire Wire Line
	6850 3350 6850 3200
$Comp
L power:+5V #PWR029
U 1 1 601F7C8D
P 6850 3200
F 0 "#PWR029" H 6850 3050 50  0001 C CNN
F 1 "+5V" H 6865 3373 50  0000 C CNN
F 2 "" H 6850 3200 50  0001 C CNN
F 3 "" H 6850 3200 50  0001 C CNN
	1    6850 3200
	1    0    0    -1  
$EndComp
Text Label 5450 4050 0    25   ~ 0
SPDIF_MOD
Text Label 5450 3850 0    25   ~ 0
SPDIF_PWDN
Wire Wire Line
	5450 4050 5550 4050
Wire Wire Line
	5450 3850 5550 3850
$Comp
L Device:C C5
U 1 1 60214EEA
P 3350 4100
F 0 "C5" H 3465 4146 50  0000 L CNN
F 1 "4.7uF" H 3465 4055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3388 3950 50  0001 C CNN
F 3 "~" H 3350 4100 50  0001 C CNN
F 4 "C19666" H 3350 4100 50  0001 C CNN "LCSC"
F 5 "Auto" H 3350 4100 50  0001 C CNN "Assembly"
	1    3350 4100
	1    0    0    -1  
$EndComp
NoConn ~ 5450 4350
NoConn ~ 5450 4550
NoConn ~ 5450 4650
NoConn ~ 5450 4750
NoConn ~ 5450 4950
NoConn ~ 5450 5050
Wire Wire Line
	5450 6750 5550 6750
Wire Wire Line
	5550 6750 5550 6900
$Comp
L power:GND #PWR024
U 1 1 6024FD52
P 5550 6900
F 0 "#PWR024" H 5550 6650 50  0001 C CNN
F 1 "GND" H 5555 6727 50  0000 C CNN
F 2 "" H 5550 6900 50  0001 C CNN
F 3 "" H 5550 6900 50  0001 C CNN
	1    5550 6900
	1    0    0    -1  
$EndComp
Wire Notes Line
	3650 5400 3650 5000
Wire Notes Line
	3950 5450 3850 5350
$Comp
L custom:AT93C46D U1
U 1 1 5FFAA596
P 2650 3200
F 0 "U1" H 2875 3356 50  0000 C CNN
F 1 "AT93C46D" H 2875 3265 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 2700 3150 50  0001 C CNN
F 3 "" H 2700 3150 50  0001 C CNN
F 4 "C6499" H 2650 3200 50  0001 C CNN "LCSC"
F 5 "Auto, Extended" H 2650 3200 50  0001 C CNN "Assembly"
F 6 "(AT93C46E)" H 2875 3174 50  0000 C CNN "Alternative"
	1    2650 3200
	-1   0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 5FFCDB1A
P 3350 2100
F 0 "C4" H 3465 2146 50  0000 L CNN
F 1 "4.7uF" H 3465 2055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3388 1950 50  0001 C CNN
F 3 "~" H 3350 2100 50  0001 C CNN
F 4 "C19666" H 3350 2100 50  0001 C CNN "LCSC"
F 5 "Auto" H 3350 2100 50  0001 C CNN "Assembly"
	1    3350 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2200 1550 2350 1550
Wire Wire Line
	4450 3850 4350 3850
Wire Wire Line
	4450 3750 4350 3750
Wire Wire Line
	2350 1950 2350 1550
$Comp
L power:+5V #PWR011
U 1 1 600041C3
P 3350 1350
F 0 "#PWR011" H 3350 1200 50  0001 C CNN
F 1 "+5V" H 3365 1523 50  0000 C CNN
F 2 "" H 3350 1350 50  0001 C CNN
F 3 "" H 3350 1350 50  0001 C CNN
	1    3350 1350
	1    0    0    -1  
$EndComp
$Comp
L Device:Ferrite_Bead FB1
U 1 1 5FF9D4BA
P 2600 1550
F 0 "FB1" V 2326 1550 50  0000 C CNN
F 1 "100R@100MHz" V 2417 1550 50  0000 C CNN
F 2 "Inductor_SMD:L_0805_2012Metric" V 2530 1550 50  0001 C CNN
F 3 "~" H 2600 1550 50  0001 C CNN
F 4 "C1015" V 2600 1550 50  0001 C CNN "LCSC"
F 5 "Auto" V 2600 1550 50  0001 C CNN "Assembly"
	1    2600 1550
	0    1    1    0   
$EndComp
Wire Wire Line
	2750 1550 2850 1550
Wire Wire Line
	2850 1550 2850 1950
Connection ~ 2350 1550
Wire Wire Line
	2350 1550 2450 1550
Wire Wire Line
	2850 1550 3350 1550
Connection ~ 2850 1550
Wire Wire Line
	3350 1550 3350 1950
Wire Wire Line
	3350 1350 3350 1550
Connection ~ 3350 1550
$Comp
L Device:C C2
U 1 1 5FF9EBBA
P 2350 2100
F 0 "C2" H 2465 2146 50  0000 L CNN
F 1 "10nF" H 2465 2055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 2388 1950 50  0001 C CNN
F 3 "~" H 2350 2100 50  0001 C CNN
F 4 "C57112" H 2350 2100 50  0001 C CNN "LCSC"
F 5 "Auto" H 2350 2100 50  0001 C CNN "Assembly"
	1    2350 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2000 3200 2000 3400
Wire Wire Line
	2000 3700 2000 4350
Wire Bus Line
	3050 4650 2950 4550
Entry Wire Line
	2950 3500 2850 3400
Entry Wire Line
	2950 3600 2850 3500
Entry Wire Line
	2950 3700 2850 3600
Entry Wire Line
	2950 3800 2850 3700
Wire Bus Line
	4150 4650 3050 4650
Entry Wire Line
	4250 3650 4350 3750
Text GLabel 4250 3450 1    25   BiDi ~ 0
USB
Wire Wire Line
	5850 3650 5850 3950
Wire Wire Line
	5850 4250 5850 4350
Entry Wire Line
	4250 3750 4350 3850
Entry Wire Line
	4250 4150 4350 4050
$Comp
L power:GND #PWR025
U 1 1 602D0D88
P 5850 4350
F 0 "#PWR025" H 5850 4100 50  0001 C CNN
F 1 "GND" H 5855 4177 50  0000 C CNN
F 2 "" H 5850 4350 50  0001 C CNN
F 3 "" H 5850 4350 50  0001 C CNN
	1    5850 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 4250 5550 4250
Text Label 5450 4250 0    25   ~ 0
LEDO
Text Label 4350 3750 0    25   ~ 0
USBD_P
Text Label 4350 3850 0    25   ~ 0
USBD_N
Text Label 2200 1750 0    25   ~ 0
USBD_IN_P
Text Label 2200 1850 0    25   ~ 0
USBD_IN_N
$Comp
L Device:C C9
U 1 1 602AF708
P 5850 4100
F 0 "C9" H 5965 4146 50  0000 L CNN
F 1 "4.7uF" H 5965 4055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5888 3950 50  0001 C CNN
F 3 "~" H 5850 4100 50  0001 C CNN
F 4 "C19666" H 5850 4100 50  0001 C CNN "LCSC"
F 5 "Auto" H 5850 4100 50  0001 C CNN "Assembly"
	1    5850 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 3650 5850 3650
$Comp
L Device:R R1
U 1 1 60381F3E
P 1750 3350
F 0 "R1" H 1820 3396 50  0000 L CNN
F 1 "0" H 1820 3305 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 1680 3350 50  0001 C CNN
F 3 "~" H 1750 3350 50  0001 C CNN
F 4 "C21189" H 1750 3350 50  0001 C CNN "LCSC"
F 5 "Auto" H 1750 3350 50  0001 C CNN "Assembly"
	1    1750 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 3600 1750 3600
Wire Wire Line
	1750 3600 1750 3500
$Comp
L power:+3.3V #PWR03
U 1 1 603863D8
P 1750 3200
F 0 "#PWR03" H 1750 3050 50  0001 C CNN
F 1 "+3.3V" H 1765 3373 50  0000 C CNN
F 2 "" H 1750 3200 50  0001 C CNN
F 3 "" H 1750 3200 50  0001 C CNN
	1    1750 3200
	1    0    0    -1  
$EndComp
$Comp
L custom:PLT133_T10W J2
U 1 1 60005290
P 8550 4750
F 0 "J2" H 9078 4388 50  0000 L CNN
F 1 "PLT133/T10W" H 9078 4297 50  0000 L CNN
F 2 "custom:PLT133_T10W" H 8600 4750 50  0001 C CNN
F 3 "" H 8600 4750 50  0001 C CNN
F 4 "Manual" H 8550 4750 50  0001 C CNN "Assembly"
	1    8550 4750
	1    0    0    -1  
$EndComp
$Comp
L Device:C C13
U 1 1 60026FD1
P 8050 5350
F 0 "C13" H 8165 5396 50  0000 L CNN
F 1 "100nF" H 8165 5305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8088 5200 50  0001 C CNN
F 3 "~" H 8050 5350 50  0001 C CNN
F 4 "C14663" H 8050 5350 50  0001 C CNN "LCSC"
F 5 "Auto" H 8050 5350 50  0001 C CNN "Assembly"
	1    8050 5350
	1    0    0    -1  
$EndComp
Wire Wire Line
	8050 5200 8050 4900
Wire Wire Line
	8050 5600 8050 5500
Wire Wire Line
	8450 5300 8450 5600
Wire Wire Line
	8050 4900 8450 4900
Wire Wire Line
	8050 5600 8450 5600
$Comp
L power:GND #PWR033
U 1 1 6002DD39
P 8050 5700
F 0 "#PWR033" H 8050 5450 50  0001 C CNN
F 1 "GND" H 8055 5527 50  0000 C CNN
F 2 "" H 8050 5700 50  0001 C CNN
F 3 "" H 8050 5700 50  0001 C CNN
	1    8050 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	8050 5700 8050 5600
Connection ~ 8050 5600
Wire Wire Line
	7750 4550 7650 4550
$Comp
L Transistor_FET:DMG2301L Q1
U 1 1 60035325
P 7950 4550
F 0 "Q1" H 8154 4504 50  0000 L CNN
F 1 "SI2301CDS" H 8154 4595 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 8150 4475 50  0001 L CIN
F 3 "https://www.diodes.com/assets/Datasheets/DMG2301L.pdf" H 7950 4550 50  0001 L CNN
F 4 "C10487" H 7950 4550 50  0001 C CNN "LCSC"
F 5 "Auto" H 7950 4550 50  0001 C CNN "Assembly"
	1    7950 4550
	1    0    0    1   
$EndComp
$Comp
L Device:R R6
U 1 1 60037816
P 7650 4300
F 0 "R6" H 7720 4346 50  0000 L CNN
F 1 "560" H 7720 4255 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7580 4300 50  0001 C CNN
F 3 "~" H 7650 4300 50  0001 C CNN
F 4 "C23204" H 7650 4300 50  0001 C CNN "LCSC"
F 5 "Auto" H 7650 4300 50  0001 C CNN "Assembly"
	1    7650 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	7650 4550 7650 4450
Wire Wire Line
	7650 4150 7650 4050
Wire Wire Line
	7650 4050 8050 4050
Wire Wire Line
	8050 4050 8050 4350
$Comp
L power:+5V #PWR032
U 1 1 6007737A
P 8050 3200
F 0 "#PWR032" H 8050 3050 50  0001 C CNN
F 1 "+5V" H 8065 3373 50  0000 C CNN
F 2 "" H 8050 3200 50  0001 C CNN
F 3 "" H 8050 3200 50  0001 C CNN
	1    8050 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	7650 4550 7350 4550
Connection ~ 7650 4550
Text Label 7350 4550 0    25   ~ 0
SPDIF_PWDN
Wire Wire Line
	8450 5100 7350 5100
Text Label 7350 5100 0    25   ~ 0
SPDIF_MOD
$Comp
L Device:R R5
U 1 1 6022D121
P 6600 5100
F 0 "R5" V 6393 5100 50  0000 C CNN
F 1 "330" V 6484 5100 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6530 5100 50  0001 C CNN
F 3 "~" H 6600 5100 50  0001 C CNN
F 4 "C23138" V 6600 5100 50  0001 C CNN "LCSC"
F 5 "Auto" V 6600 5100 50  0001 C CNN "Assembly"
	1    6600 5100
	0    1    1    0   
$EndComp
Wire Wire Line
	6750 5100 6850 5100
Wire Wire Line
	6850 5100 6850 5200
$Comp
L Device:LED LD1
U 1 1 60232A49
P 6850 5350
F 0 "LD1" V 6934 5232 50  0000 R CNN
F 1 "rd" V 6843 5232 50  0000 R CNN
F 2 "LED_SMD:LED_0603_1608Metric" H 6850 5350 50  0001 C CNN
F 3 "~" H 6850 5350 50  0001 C CNN
F 4 "C2286" V 6850 5350 50  0001 C CNN "LCSC"
F 5 "Auto" V 6850 5350 50  0001 C CNN "Assembly"
	1    6850 5350
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR031
U 1 1 60235D68
P 6850 5700
F 0 "#PWR031" H 6850 5450 50  0001 C CNN
F 1 "GND" H 6855 5527 50  0000 C CNN
F 2 "" H 6850 5700 50  0001 C CNN
F 3 "" H 6850 5700 50  0001 C CNN
	1    6850 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6850 5500 6850 5700
Wire Wire Line
	8050 4750 8050 4900
Connection ~ 8050 4900
$Comp
L Device:C C1
U 1 1 60076670
P 1500 4100
F 0 "C1" H 1615 4146 50  0000 L CNN
F 1 "100nF" H 1615 4055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 1538 3950 50  0001 C CNN
F 3 "~" H 1500 4100 50  0001 C CNN
F 4 "C14663" H 1500 4100 50  0001 C CNN "LCSC"
F 5 "Auto" H 1500 4100 50  0001 C CNN "Assembly"
	1    1500 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 4250 1500 4350
Wire Wire Line
	1500 3950 1500 3200
$Comp
L power:GND #PWR02
U 1 1 60085785
P 1500 4350
F 0 "#PWR02" H 1500 4100 50  0001 C CNN
F 1 "GND" H 1505 4177 50  0000 C CNN
F 2 "" H 1500 4350 50  0001 C CNN
F 3 "" H 1500 4350 50  0001 C CNN
	1    1500 4350
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR01
U 1 1 6008667F
P 1500 3200
F 0 "#PWR01" H 1500 3050 50  0001 C CNN
F 1 "+3.3V" H 1515 3373 50  0000 C CNN
F 2 "" H 1500 3200 50  0001 C CNN
F 3 "" H 1500 3200 50  0001 C CNN
	1    1500 3200
	1    0    0    -1  
$EndComp
$Comp
L Device:C C11
U 1 1 600E6DD6
P 6350 4100
F 0 "C11" H 6465 4146 50  0000 L CNN
F 1 "100nF" H 6465 4055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6388 3950 50  0001 C CNN
F 3 "~" H 6350 4100 50  0001 C CNN
F 4 "C14663" H 6350 4100 50  0001 C CNN "LCSC"
F 5 "Auto" H 6350 4100 50  0001 C CNN "Assembly"
	1    6350 4100
	1    0    0    -1  
$EndComp
$Comp
L Device:C C12
U 1 1 600E8D65
P 6850 4100
F 0 "C12" H 6965 4146 50  0000 L CNN
F 1 "100nF" H 6965 4055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6888 3950 50  0001 C CNN
F 3 "~" H 6850 4100 50  0001 C CNN
F 4 "C14663" H 6850 4100 50  0001 C CNN "LCSC"
F 5 "Auto" H 6850 4100 50  0001 C CNN "Assembly"
	1    6850 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 3950 6350 3350
Wire Wire Line
	6850 3950 6850 3350
Wire Wire Line
	6350 4250 6350 4350
Wire Wire Line
	6850 4250 6850 4350
Connection ~ 6350 3350
Wire Wire Line
	6350 3350 6850 3350
Connection ~ 6850 3350
Wire Wire Line
	5450 3350 6350 3350
$Comp
L power:GND #PWR028
U 1 1 6011F90E
P 6350 4350
F 0 "#PWR028" H 6350 4100 50  0001 C CNN
F 1 "GND" H 6355 4177 50  0000 C CNN
F 2 "" H 6350 4350 50  0001 C CNN
F 3 "" H 6350 4350 50  0001 C CNN
	1    6350 4350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR030
U 1 1 6011FE73
P 6850 4350
F 0 "#PWR030" H 6850 4100 50  0001 C CNN
F 1 "GND" H 6855 4177 50  0000 C CNN
F 2 "" H 6850 4350 50  0001 C CNN
F 3 "" H 6850 4350 50  0001 C CNN
	1    6850 4350
	1    0    0    -1  
$EndComp
Wire Notes Line
	3850 2150 3750 2050
Wire Notes Line
	3850 2150 3850 2400
Wire Notes Line
	4550 2400 4550 2150
Wire Notes Line
	3850 2400 4550 2400
Text Notes 3900 2350 0    50   ~ 0
Enumeration as\nUSB FS Device
Wire Notes Line
	3750 2050 3750 1800
Wire Notes Line
	3500 1800 3900 1800
Wire Wire Line
	8050 3200 8050 4050
Connection ~ 8050 4050
Text Label 6250 5100 0    25   ~ 0
LEDO
Wire Wire Line
	6250 5100 6450 5100
Connection ~ 3650 1750
Wire Wire Line
	2200 1750 3650 1750
Wire Notes Line
	3900 1100 3900 1800
Wire Notes Line
	3900 1100 3500 1100
Wire Notes Line
	3500 1100 3500 1800
$Comp
L power:+3.3V #PWR015
U 1 1 604766E5
P 3650 1350
F 0 "#PWR015" H 3650 1200 50  0001 C CNN
F 1 "+3.3V" H 3665 1523 50  0000 C CNN
F 2 "" H 3650 1350 50  0001 C CNN
F 3 "" H 3650 1350 50  0001 C CNN
	1    3650 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 1650 3650 1750
Wire Notes Line
	4550 2150 3850 2150
$Comp
L Mechanical:MountingHole_Pad H1
U 1 1 603A953B
P 1600 5000
F 0 "H1" V 1554 5150 50  0000 L CNN
F 1 "MountingHole_Pad" V 1645 5150 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5_DIN965_Pad" H 1600 5000 50  0001 C CNN
F 3 "~" H 1600 5000 50  0001 C CNN
	1    1600 5000
	0    1    1    0   
$EndComp
$Comp
L Mechanical:MountingHole_Pad H2
U 1 1 603AA239
P 1600 5200
F 0 "H2" V 1554 5350 50  0000 L CNN
F 1 "MountingHole_Pad" V 1645 5350 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5_DIN965_Pad" H 1600 5200 50  0001 C CNN
F 3 "~" H 1600 5200 50  0001 C CNN
	1    1600 5200
	0    1    1    0   
$EndComp
$Comp
L Mechanical:MountingHole_Pad H3
U 1 1 603AA61B
P 1600 5400
F 0 "H3" V 1554 5550 50  0000 L CNN
F 1 "MountingHole_Pad" V 1645 5550 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5_DIN965_Pad" H 1600 5400 50  0001 C CNN
F 3 "~" H 1600 5400 50  0001 C CNN
	1    1600 5400
	0    1    1    0   
$EndComp
Wire Wire Line
	1500 5000 1500 5200
Wire Wire Line
	1500 5200 1500 5400
Connection ~ 1500 5200
Wire Wire Line
	1500 5400 1500 5500
Connection ~ 1500 5400
$Comp
L power:GND #PWR034
U 1 1 603B83BF
P 1500 5500
F 0 "#PWR034" H 1500 5250 50  0001 C CNN
F 1 "GND" H 1505 5327 50  0000 C CNN
F 2 "" H 1500 5500 50  0001 C CNN
F 3 "" H 1500 5500 50  0001 C CNN
	1    1500 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 4950 4350 4950
$Comp
L power:+3.3V #PWR0101
U 1 1 5FFD9868
P 4350 4950
F 0 "#PWR0101" H 4350 4800 50  0001 C CNN
F 1 "+3.3V" V 4365 5078 50  0000 L CNN
F 2 "" H 4350 4950 50  0001 C CNN
F 3 "" H 4350 4950 50  0001 C CNN
	1    4350 4950
	0    -1   -1   0   
$EndComp
Wire Notes Line
	3850 5350 3650 5350
Wire Notes Line
	3950 4850 3950 5000
Wire Notes Line
	3950 5000 4850 5000
Wire Notes Line
	4850 5000 4850 4850
Wire Notes Line
	4850 4850 3950 4850
Text Notes 2650 4800 0    50   ~ 0
For +3.3V power routing
Wire Notes Line
	2600 4850 3650 4850
Wire Notes Line
	3650 4850 3650 4700
Wire Notes Line
	3650 4700 2600 4700
Wire Notes Line
	2600 4700 2600 4850
Wire Notes Line
	3650 4750 3850 4750
Wire Notes Line
	3850 4750 3950 4850
$Comp
L Connector:TestPoint TP1
U 1 1 5FFC2B70
P 5450 5250
F 0 "TP1" V 5404 5438 50  0001 L CNN
F 1 "SDIN" V 5450 5438 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 5250 50  0001 C CNN
F 3 "~" H 5650 5250 50  0001 C CNN
	1    5450 5250
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP2
U 1 1 5FFCA10C
P 5450 5350
F 0 "TP2" V 5404 5538 50  0001 L CNN
F 1 "ADSCLK" V 5450 5538 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 5350 50  0001 C CNN
F 3 "~" H 5650 5350 50  0001 C CNN
	1    5450 5350
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP3
U 1 1 5FFCA415
P 5450 5450
F 0 "TP3" V 5404 5638 50  0001 L CNN
F 1 "ADLRCK" V 5450 5638 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 5450 50  0001 C CNN
F 3 "~" H 5650 5450 50  0001 C CNN
	1    5450 5450
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP4
U 1 1 5FFCA6A3
P 5450 5550
F 0 "TP4" V 5404 5738 50  0001 L CNN
F 1 "ADMCLK" V 5450 5738 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 5550 50  0001 C CNN
F 3 "~" H 5650 5550 50  0001 C CNN
	1    5450 5550
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP5
U 1 1 5FFCBBF0
P 5450 5750
F 0 "TP5" V 5404 5938 50  0001 L CNN
F 1 "SDOUT" V 5450 5938 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 5750 50  0001 C CNN
F 3 "~" H 5650 5750 50  0001 C CNN
	1    5450 5750
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP6
U 1 1 5FFCBF14
P 5450 5850
F 0 "TP6" V 5404 6038 50  0001 L CNN
F 1 "DAMCLK" V 5450 6038 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 5850 50  0001 C CNN
F 3 "~" H 5650 5850 50  0001 C CNN
	1    5450 5850
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP7
U 1 1 5FFCC14C
P 5450 5950
F 0 "TP7" V 5404 6138 50  0001 L CNN
F 1 "DALRCK" V 5450 6138 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 5950 50  0001 C CNN
F 3 "~" H 5650 5950 50  0001 C CNN
	1    5450 5950
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint TP8
U 1 1 5FFCC361
P 5450 6050
F 0 "TP8" V 5404 6238 50  0001 L CNN
F 1 "DASCLK" V 5450 6238 50  0000 L CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 5650 6050 50  0001 C CNN
F 3 "~" H 5650 6050 50  0001 C CNN
	1    5450 6050
	0    1    1    0   
$EndComp
Connection ~ 4450 6750
Connection ~ 5450 6750
Connection ~ 5450 3350
Wire Wire Line
	5450 6650 5450 6750
Wire Wire Line
	5450 6450 5450 6650
Connection ~ 5450 6650
Connection ~ 4450 5650
$Comp
L custom:CM108AH U2
U 1 1 600A391D
P 4950 4950
F 0 "U2" H 4950 6815 50  0000 C CNN
F 1 "CM108AH" H 4950 6724 50  0000 C CNN
F 2 "Package_QFP:LQFP-48_7x7mm_P0.5mm" H 4950 6700 50  0001 C CNN
F 3 "" H 4600 6700 50  0001 C CNN
F 4 "C371346" H 4950 4950 50  0001 C CNN "LCSC"
F 5 "Auto, Extended" H 4950 4950 50  0001 C CNN "Assembly"
	1    4950 4950
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint TP10
U 1 1 6002C48A
P 4450 4750
F 0 "TP10" V 4404 4938 50  0001 L CNN
F 1 "GPIO4" V 4450 5050 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 4650 4750 50  0001 C CNN
F 3 "~" H 4650 4750 50  0001 C CNN
	1    4450 4750
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint TP9
U 1 1 6002D332
P 4450 4650
F 0 "TP9" V 4404 4838 50  0001 L CNN
F 1 "GPIO3" V 4450 4950 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.0mm" H 4650 4650 50  0001 C CNN
F 3 "~" H 4650 4650 50  0001 C CNN
	1    4450 4650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4100 1850 2200 1850
$Comp
L Device:R R3
U 1 1 602BE466
P 4250 1850
F 0 "R3" V 4350 1750 50  0000 C CNN
F 1 "22" V 4350 1900 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4180 1850 50  0001 C CNN
F 3 "~" H 4250 1850 50  0001 C CNN
F 4 "C23345" V 4250 1850 50  0001 C CNN "LCSC"
F 5 "Auto" V 4250 1850 50  0001 C CNN "Assembly"
	1    4250 1850
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 602BEBEC
P 4250 1750
F 0 "R4" V 4150 1650 50  0000 C CNN
F 1 "22" V 4150 1800 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4365 1750 50  0001 C CNN
F 3 "~" H 4250 1750 50  0001 C CNN
F 4 "C23345" V 4250 1750 50  0001 C CNN "LCSC"
F 5 "Auto" V 4250 1750 50  0001 C CNN "Assembly"
	1    4250 1750
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR023
U 1 1 601C6C71
P 6050 2350
F 0 "#PWR023" H 6050 2100 50  0001 C CNN
F 1 "GND" H 6055 2177 50  0000 C CNN
F 2 "" H 6050 2350 50  0001 C CNN
F 3 "" H 6050 2350 50  0001 C CNN
	1    6050 2350
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR022
U 1 1 601CAE21
P 5050 1350
F 0 "#PWR022" H 5050 1200 50  0001 C CNN
F 1 "+5V" H 5065 1523 50  0000 C CNN
F 2 "" H 5050 1350 50  0001 C CNN
F 3 "" H 5050 1350 50  0001 C CNN
	1    5050 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 2350 6600 2250
Wire Wire Line
	6600 1350 6600 1950
$Comp
L power:+5V #PWR026
U 1 1 6005DBE3
P 6600 1350
F 0 "#PWR026" H 6600 1200 50  0001 C CNN
F 1 "+5V" H 6615 1523 50  0000 C CNN
F 2 "" H 6600 1350 50  0001 C CNN
F 3 "" H 6600 1350 50  0001 C CNN
	1    6600 1350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR027
U 1 1 6005E2F0
P 6600 2350
F 0 "#PWR027" H 6600 2100 50  0001 C CNN
F 1 "GND" H 6605 2177 50  0000 C CNN
F 2 "" H 6600 2350 50  0001 C CNN
F 3 "" H 6600 2350 50  0001 C CNN
	1    6600 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:C C10
U 1 1 60049F86
P 6600 2100
F 0 "C10" H 6715 2146 50  0000 L CNN
F 1 "100nF" H 6715 2055 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6638 1950 50  0001 C CNN
F 3 "~" H 6600 2100 50  0001 C CNN
F 4 "C14663" H 6600 2100 50  0001 C CNN "LCSC"
F 5 "Auto" H 6600 2100 50  0001 C CNN "Assembly"
	1    6600 2100
	1    0    0    -1  
$EndComp
Text GLabel 4700 2150 3    25   BiDi ~ 0
USB
Entry Wire Line
	4700 1850 4600 1750
Entry Wire Line
	4700 1950 4600 1850
Wire Wire Line
	4400 1850 4600 1850
Wire Wire Line
	3650 1750 4100 1750
Wire Wire Line
	4600 1750 4400 1750
Text Label 4450 1750 0    25   ~ 0
USBD_P
Text Label 4450 1850 0    25   ~ 0
USBD_N
Wire Wire Line
	5050 1350 5050 1850
Wire Wire Line
	6050 1850 6050 2350
Wire Notes Line
	1650 3200 1950 3200
Wire Notes Line
	1950 3200 1950 3500
Wire Notes Line
	1950 3500 1650 3500
Wire Notes Line
	1650 3500 1650 3200
Wire Notes Line
	1650 3500 1550 3600
Wire Notes Line
	1550 3600 1350 3600
Text Notes 950  3700 0    50   ~ 0
DNP for\nAT93C46E
Wire Notes Line
	900  3500 1350 3500
Wire Notes Line
	1350 3500 1350 3750
Wire Notes Line
	1350 3750 900  3750
Wire Notes Line
	900  3750 900  3500
Wire Wire Line
	4450 5050 4350 5050
Text Label 4350 5050 0    25   ~ 0
MUTE
$Comp
L Switch:SW_Push SW1
U 1 1 601FE0B9
P 2000 6500
F 0 "SW1" V 2046 6452 50  0000 R CNN
F 1 "MUTE" V 1955 6452 50  0000 R CNN
F 2 "Button_Switch_SMD:SW_SPST_PTS645" H 2000 6700 50  0001 C CNN
F 3 "~" H 2000 6700 50  0001 C CNN
F 4 "Manual" V 2000 6500 50  0001 C CNN "Assembly"
	1    2000 6500
	0    -1   -1   0   
$EndComp
Text Label 1800 6000 0    25   ~ 0
MUTE
$Comp
L power:GND #PWR07
U 1 1 6020FF87
P 2000 6900
F 0 "#PWR07" H 2000 6650 50  0001 C CNN
F 1 "GND" H 2005 6727 50  0000 C CNN
F 2 "" H 2000 6900 50  0001 C CNN
F 3 "" H 2000 6900 50  0001 C CNN
	1    2000 6900
	1    0    0    -1  
$EndComp
Wire Wire Line
	1800 6000 2000 6000
Wire Wire Line
	2000 6000 2000 6300
Wire Wire Line
	2000 6700 2000 6900
$Comp
L Power_Protection:SRV05-4 U3
U 1 1 6011013F
P 5550 1850
F 0 "U3" V 5596 1306 50  0000 R CNN
F 1 "SRV05-4" V 5505 1306 50  0000 R CNN
F 2 "Package_TO_SOT_SMD:SOT-23-6" H 6250 1400 50  0001 C CNN
F 3 "http://www.onsemi.com/pub/Collateral/SRV05-4-D.PDF" H 5550 1850 50  0001 C CNN
F 4 "(NUP2201)" V 5414 1306 50  0000 R CNN "Alternative"
	1    5550 1850
	0    -1   -1   0   
$EndComp
Text Label 5450 2450 1    25   ~ 0
USBD_N
Wire Wire Line
	5450 2350 5450 2450
Text Label 5650 1350 1    25   ~ 0
USBD_P
Wire Wire Line
	5650 1350 5650 1250
$Comp
L Device:R R2
U 1 1 604728F9
P 3650 1500
F 0 "R2" H 3720 1566 50  0000 L CNN
F 1 "1k5" H 3720 1435 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 3580 1500 50  0001 C CNN
F 3 "~" H 3650 1500 50  0001 C CNN
F 4 "C22843" H 3650 1500 50  0001 C CNN "LCSC"
F 5 "Auto" H 3650 1500 50  0001 C CNN "Assembly"
F 6 "5%" H 3720 1500 50  0000 L CNN "Tolerance"
	1    3650 1500
	1    0    0    -1  
$EndComp
Text Notes 7000 6750 0    50   ~ 0
Compatible alternative P/N in round brackets.\nRES tolerance 10% unless otherwise noted.
NoConn ~ 5450 1350
NoConn ~ 5650 2350
Wire Bus Line
	4700 1850 4700 2150
Wire Bus Line
	4250 3450 4250 3750
Wire Bus Line
	2950 3500 2950 4550
Wire Bus Line
	4250 4150 4250 4550
$EndSCHEMATC
