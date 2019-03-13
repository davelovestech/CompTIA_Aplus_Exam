#!/usr/bin/env python2

#print "What Process and Step # is this?"
#print "Answer in this format: "
#print "PROCESS_NAME STEP_NUMBER"

from PIL import Image
import subprocess

laser_printer_image = subprocess.Popen(["display", "./Laser_Printer/Laser_Printer_Process_Blanks.jpg"])

steps_and_layers_dict = {
	"Build the page in memory": "Laser Printing Step 1: Processing",
	"Prepare the Drum with a negative electrostatic charge": "Laser Printing Step 2: Charging",
	"Write the image with the laser": "Laser Printing Step 3: Exposing",
	"Add toner to the charged areas of the drum": "Laser Printing Step 4: Devloping",
	"Move the toner from the drum to the paper": "Laser Printing Step 5: Transferring",
	"The toner is fused to the paper": "Laser Printing Step 6: Fusing",
	"A rubber blade removes excess toner": "Laser Printing Step 7: Cleaning",
	"Data is visualized for the user in the applicaiton layer": "OSI Layer 7",
	"The operating system converts data from one format to another in the session layer": "OSI Layer 6",
	"The session layer sets up, coordinates and terminates conversations": "OSI Layer 5",
	"The transport layer manages packetization of data": "OSI Layer 4",
	"The network layer handles addressing and routing of data": "OSI Layer 3",
	"The data-link layer sets up links across the physical network": "OSI Layer 2",
	"The physical layer conveys the bit stream electrically, mechanically, or by radio": "OSI Layer 1",
	"Identify the problem": "CompTIA Troubleshooting Step 1",
	"Establish a theory of probable cause (question the obvious)": "CompTIA Troubleshooting Step 2",
	"Test the theory to determine the cause": "CompTIA Troubleshooting Step 3",
	"Establish a ploan of action to resolve the problem and implement the solution": "CompTIA Troubleshooting Step 4",
		"Verify full system functionality and, if applicable, imlement preventative measures": "CompTIA Troubleshooting Step 5",
		"Document findings, actions, and outcomes": "CompTIA Troubleshooting Step 6",
	"Identify the malware symptoms": "Malware Removal Step 1",
	"Quarantine the infected system": "Malware Removal Step 2",
	"Disable system restore (in Windows)": "Malware Removal Step 3",
	"Remediate infected systems (update antimalware software, scan)": "Malware Removal Step 4",
	"Schedule scans and run updates": "Malware Removal Step 5",
	"Enable system restore and create a restore point": "Malware Removal Step 6",
	"Educate end user": "Malware Removal Step 7",
	"Laser Printer Step 1": "Processing",
	"Laser Printer Step 2": "Charging",
	"Laser Printer Step 3": "Exposing",
	"Laser Printer Step 4": "Developing",
	"Laser Printer Step 5": "Transferring",
	"Laser Printer Step 6": "Fusing",
	"Laser Printer Step 7": "Cleaning"
}

for item in steps_and_layers_dict:
	print "Identify the process | layer and # of each item"
	print(item)
	answer = raw_input()
	
	if answer == steps_and_layers_dict[item]:	
		print "CORRECT!\n"
	else:
		print "WRONG!"
		print item + " is from " + steps_and_layers_dict[item] + "\n"
	print "============================================================="
laser_printer_image.kill()
