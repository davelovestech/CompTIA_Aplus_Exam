#!/usr/bin/env python

print "Welcome to the CompTIA A+ Port Number Quiz!"

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
	"NetBIOS name service" : 137,
	"NetBIOS Datagram Service" : 138,
	"NetBIOS Session Service" : 139,
	}
# this prints the dictionary
print port_dictionary

# the dictionary should be 21 characters long
print len(port_dictionary)

# this prints the dictionary line by line
for item in port_dictionary:
	print item + " " + str(port_dictionary[item])
