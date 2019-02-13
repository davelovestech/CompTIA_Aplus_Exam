#!/usr/bin/env python

print "Welcome to the CompTIA A+ Port Number Quiz!"
quizzing = True
import random
# this is the dictionary of port numbers
# that Professor Messer says to study
# https://www.reddit.com/r/CompTIA/comments/4swx3q/what_port_numbers_do_i_need_to_know_for_a/
# 993 - Secure IMAP
port_dictionary = {
	"DHCP Destination" : 67,
	"DHCP Client" : 68,
	"DNS" : 53,
	"LDAP" : 389,
	"SNMP" : 161,
	"SMB" : 445,
	"CIFS TCP" : 445,
	"SSH" : 22,
	"AFP" : 548,
	"SLP" : 427,
	"FTP Commands" : 21,
	"FTP Data" : 20,
	"Telnet" : 23,
	"SMTP" : 25,
	"HTTP" : 80,
	"POP3" : 110,
	"IMAP4" : 143,
	"Secure IMAP" : 993,
	"Secure POP3" : 995,
	"HTTPS" : 443,
	"RDP" : 3389,
	"NetBIOS Name Service" : 137,
	"NetBIOS Datagram Service" : 138,
	"NetBIOS Session Service" : 139,
	}
# this prints the dictionary
# print port_dictionary

# the dictionary should be 21 characters long
# print len(port_dictionary)
dictionary_length = len(port_dictionary)

# this prints the dictionary line by line
# for item in port_dictionary:
#	print item + " " + str(port_dictionary[item])

# this keeps track of your score and # questions asked
score = 0
questions = 0
answer = ""
answer_number = 0
answer_string = 0

while quizzing:
	random_key = random.choice(port_dictionary.keys()) 		
	#print random_key
	random_key_item = port_dictionary[random_key]
	#print random_key_item

	print "\nEnter 'QUIT' if you would like to quit."
	print "\nWhat is the port number for " + random_key
	answer = raw_input()
	answer_string = str(answer)
	try:
		answer_number = int(answer)
	except: 
		pass
	if answer_string == "QUIT":
		quizzing = False
	else:	
		if answer_number == random_key_item:
			print "\nCorrect! The port number for " + random_key + " is " + str(random_key_item)
			score += 1
			questions += 1
		else:
			print "WRONG! The port number for " + random_key + " is " + str(random_key_item)
			questions += 1
			pass
score_percentage = score * 100 / questions
print "You got " + str(score) + " questions correct out of " + str(questions) + " questions."		
print "Your score is " + str(score_percentage) + " %."


















