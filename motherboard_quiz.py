#!/usr/bin/env python2

import time
from PIL import Image
import subprocess

############## QUIZ FUNC ###################################
print "-------------------------------------------------------"
def quiz_me(dictionary):
	# print dictionary
	for question in dictionary:
		print "What is label " + question + "?"
		response = str(raw_input())
		if response == dictionary[question]:
			print "Correct!"
		else:
			print "WRONG. The answer is: " + dictionary[question]
		print "-------------------------------------------------------"
# answer is		
#dictionary[question]

############## MOTHERBOARD #################################

# toms_hardware_motherboard
# https://www.tomshardware.com/reviews/motherboard-parts-explained,5669.html
toms_hardware_motherboard = subprocess.Popen(["display", "./Motherboard/toms_hardware_motherboard.jpeg"])

toms_hardware_motherboard_dictionary = {
	"1": "CPU Socket",
	"2": "Chipset",
	"3": "RAM Slots",
	"4": "PCIe x16 Slot",
	"5": "PCI x1 Slot",
	"6": "M.2 Connector",
	"7": "SATA Ports",
	"8": "Front Panel Connectors",
	"9": "USB 2.0 Header",
	"10": "USB 3.1 Gen1 Header",
	"11": "USB 3.1 Gen2 Header",
	"12": "ATX Power Connector",
	"13": "CPU Power Connector",
	"14": "BIOS Chips",
	"15": "CMOS Battery",
	"16": "Fan Headers",
	"17": "Front Panel Header",
	"18": "VRM Heatsink",
	"19": "COM/Serial Header",
	"20": "TPM Header",
	"21": "RGB Header"	
}
print "toms_hardware_motherboard_dictionary"
quiz_me(toms_hardware_motherboard_dictionary)
#print toms_hardware_motherboard_dictionary
toms_hardware_motherboard.kill()

# build_your_own_computer_motherboard
# https://www.build-your-own-computer.net/motherboard-diagram.html
build_your_own_computer_motherboard = subprocess.Popen(["display", "./Motherboard/build_your_own_computer_motherboard.jpg"])

build_your_own_computer_motherboard_dictionary = {
	"A": "PCI Slot",
	"B": "PCI-E 16x Slot",
	"C": "PCI-E 1x Slot",
	"D": "Northbridge",
	"E": "ATX 12V 2X and 4 Pin Power Connection",
	"F": "CPU Fan",
	"G": "Socket",
	"H": "Memory Slots",
	"I": "ATX Power Connector",
	"J": "IDE Connection",
	"K": "Southbridge",
	"L": "SATA Connections",
	"M": "Front Panel Connections",
	"N": "FDD Connection",
	"O": "External USB Connectors",
	"P": "CMOS Battery"
}
print "build_your_own_computer_motherboard_dictionary"
quiz_me(build_your_own_computer_motherboard_dictionary)
#print build_your_own_computer_motherboard_dictionary
build_your_own_computer_motherboard.kill()

# passCompTIA_motherboard
# http://passcomptia.com/comptia-a-220-901/comptia-a-simulation-3/
passCompTIA_motherboard = subprocess.Popen(["display", "./Motherboard/passCompTIA_motherboard.jpg"])

passCompTIA_motherboard_dict = {
	"A": "Memory Module Connectors",
	"B": "Main Power Connector",
	"C": "Floppy Drive Connector",
	"D": "PCI Express x16 card connector",
	"E": "IDE Drive Connector",
	"F": "Front Panel I/O Connector",
	"G": "SATA Connector",
	"H": "CMOS Battery",
	"I": "PCI Card Connector",
	"J": "PCI Express x4 Connector",
	"K": "PCI Express x1 Connector",
	"L": "CPU Fan Connector",
	"M": "CPU Socket",
	"N": "USB Connector",
	"O": "Processor Power Connector"
}
print "passCompTIA_motherboard_dict"
quiz_me(passCompTIA_motherboard_dict)
#print passCompTIA_motherboard_dict
passCompTIA_motherboard.kill()

############## REAR PORTS ##################################

# support_hp_rear_ports
# https://support.hp.com/us-en/document/c02560084
support_hp_rear_ports = subprocess.Popen(["display", "./Motherboard/support_hp_rear_ports.jpg"])

support_hp_rear_ports_dict = {
	"1": "S/PDIF Output",
	"2": "VGA Port",
	"3": "USB 2.0 Port",
	"4": "RJ45 10/100 Mb/s LAN",
	"5": "Center Subwoofer Out",
	"6": "Rear Speaker Out",
	"7": "Line In",
	"8": "Line Out",
	"9": "Mic In",
	"10": "Side Speaker Out",
	"11": "DVI-D Port"
}
print "support_hp_rear_ports_dict"
quiz_me(support_hp_rear_ports_dict)
# print support_hp_rear_ports_dict
support_hp_rear_ports.kill()

# toms_hardware_rear_ports
# https://www.tomshardware.com/reviews/motherboard-parts-explained,5669.html
toms_hardware_rear_ports = subprocess.Popen(["display", "./Motherboard/toms_hardware_rear_ports.jpeg"])

toms_hardware_rear_ports_dict = {
	"22": "PS/2 Keyboard/Mouse port",
	"23": "USB 3.0/3.1 Gen1 ports",
	"24": "Displayport",
	"25": "HDMI port",
	"26": "USB Type-C",
	"27": "USB 3.1 Gen2",
	"28": "Ethernet Port",
	"29 orange": "center subwoofer out",
	"29 blue": "line in",
	"29 black": "rear speaker out",
	"29 green": "line out", 
	"29 gray": "door S/PDIF Out",
	"29 pink": "mic in"
}
print "toms_hardware_rear_ports_dict"
quiz_me(toms_hardware_rear_ports_dict)
#print(toms_hardware_rear_ports_dict)
toms_hardware_rear_ports.kill()

# bjorn32_rear_ports
# https://www.bjorn3d.com/2008/10/evga-790i-ultra/
bjorn32_rear_ports = subprocess.Popen(["display", "./Motherboard/bjorn32_rear_ports.jpg"])

bjorn32_rear_ports_dict = {
	"1": "PS/2 Mouse Port",
	"2": "PS/2 Keyboard Port",
	"3": "Coaxial SPDIF",
	"4": "SPDIF output",
	"5": "eSATA",
	"6": "USB 2.0 ports",
	"7 1394a": "Firewire Port",
	"8 blue": "line in",
	"8 green": "line out",
	"8 pink": "mic in",
	"8 orange": "center subwoofer",
	"8 black": "rear speaker out",
	"8 grey": "side speaker out",
	"9": "LAN Port"
}
print "bjorn32_rear_ports_dict"
quiz_me(bjorn32_rear_ports_dict)
#print bjorn32_rear_ports_dict
bjorn32_rear_ports.kill()
