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

################## Connectors_Page_Blanks.jpg
Connectors_Page_Blanks = subprocess.Popen(["display", "./Connectors/Connectors_Page_Blanks.jpg"])
Connectors_Page_Blanks_dictionary = {
	"A": "USB 1.1/2.0",
	"B": "Standard-A Plug",
	"C": "Standard-B Plug",
	"D": "Mini-B Plug",
	"E": "Micro-B Plug",
	"F": "USB 3.0 Standard-B Plug",
	"G": "USB 3.0 Standard-A Plug",
	"H": "USB 3.0 Micro-B Plug",
	"I": "FireWire",
	"J": "SATA",
	"K": "USB Type A Plug",
	"L": "6-pin Alpha (powered)",
	"M": "4-pin Alpha (unpowered)",
	"N": "9-pin Beta (powered)",
	"O": "SATA Power",
	"P": "SATA Data",
	"Q": "eSATA",
	"R": "SATA Data",
	"S": "VGA",
	"T": "HDMI",
	"U": "miniHDMI",
	"V": "HDMI",
	"X": "DVI",
	"Y": "TOSLINK",
	"Z": "TRS",
	"1": "RJ11",
	"2": "RJ45",
	"3": "DisplayPort",
	"4": "Mini DisplayPort or Thunderbolt",
	"5": "RCA Connectors",
	"6": "BNC Connectors",
	"7": "Mini-DIN-4 (S-Video)",
	"8": "Mini-DIN-6 (Keyboard/Mouse)"
}
print "Connectors_Page_Blanks"
quiz_me(Connectors_Page_Blanks_dictionary)
Connectors_Page_Blanks.kill()
################## Copper_Cable_Connections_Blanks.jpg
Copper_Cable_Connections_Blanks = subprocess.Popen(["display", "./Connectors/Copper_Cable_Connections_Blanks.jpg"])
Copper_Cable_Connections_Blanks_dictionary = {
	"A": "UTP Unshielded Twisted Pair",
	"B": "STP Shielded Twisted Pair",
	"C": "Coaxial Cable"
}
print "Copper_Cable_Connections_Blanks"
quiz_me(Copper_Cable_Connections_Blanks_dictionary)
Copper_Cable_Connections_Blanks.kill()
################## Mobile_Device_Connections_Blanks.jpg
Mobile_Device_Connections_Blanks = subprocess.Popen(["display", "./Connectors/Mobile_Device_Connections_Blanks.jpg"])
Mobile_Device_Connections_Blanks_dictionary = {
	"A": "USB Micro-B",
	"B": "Apple 8-pin Lightning",
	"C": "USB Standard Type A",
	"D": "Apple 30-pin"
}
print "Mobile_Device_Connections_Blanks"
quiz_me(Mobile_Device_Connections_Blanks_dictionary)
Mobile_Device_Connections_Blanks.kill()
################## Network_Connections_Blanks.jpg
Network_Connections_Blanks = subprocess.Popen(["display", "./Connectors/Network_Connections_Blanks.jpg"])
Network_Connections_Blanks_dictionary = {
	"A": "ST Connectors - Straight Tip",
	"B": "SC Connectors",
	"C": "LC Connectors",
	"D": "Fiber Connector",
	"E": "RJ 11 Connector",
	"F": "RJ45 Connector",
	"G": "BNC Connector",
	"H": "F Connector"
}
print "Network_Connections_Blanks"
quiz_me(Network_Connections_Blanks_dictionary)
Network_Connections_Blanks.kill()
################## Power_Connectors_Blanks.jpg
Power_Connectors_Blanks = subprocess.Popen(["display", "./Connectors/Power_Connectors_Blanks.jpg"])
Power_Connectors_Blanks_dictionary = {
	"A": "Molex Connector",
	"B": "4-pin ATX +12V",
	"C": "8-pin EPS +12 V power",
	"D": "SATA power - 15 pins",
	"E": "PCIe 6-pin and 8-pin power",
	"F": "24-pin motherboard power"
}
print "Power_Connectors_Blanks"
quiz_me(Power_Connectors_Blanks_dictionary)
Power_Connectors_Blanks.kill()
