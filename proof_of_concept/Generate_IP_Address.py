#!/usr/bin/env python

import random
generate = True

print "Welcome to the IP Address Generator!"

byte_one = 0
byte_two = 0
byte_three = 0
byte_four = 0

def build_IP_address(byte_one, byte_two, byte_three, byte_four):
	ip_address = str(byte_one) + "." + str(byte_two) + "." + str(byte_three) + "." + str(byte_four)
	return ip_address 
	

# class a
# 10.0.0.0 - 10.255.255.255
def generate_class_A():
	print "Class A IP Address:"
	byte_one = 10
	byte_two = random.randint(0,256)
	byte_three = random.randint(0,256)
	byte_four = random.randint(0,256)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

# class b
# 172.16.0.0 - 172.31.255.255
def generate_class_B():
	print "Class B IP Address:"
	byte_one = 172
	byte_two = random.randint(16,32)
	byte_three = random.randint(0,256)
	byte_four = random.randint(0,256)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

# class c
# 192.168.0.0 - 192.168.255.255
def generate_class_C():
	print "Class C IP Address:"
	byte_one = 192
	byte_two = 168
	byte_three = random.randint(0,256)
	byte_four = random.randint(0,256)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

# APIPA
# 169.254.1.0 - 169.254.254.255
def generate_APIPA():
	print "APIPA IP Address:"
	byte_one = 169
	byte_two = 254
	byte_three = random.randint(1,255)
	byte_four = random.randint(0,256)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

while generate == True:
	print "Enter 'QUIT' to exit this program."
	answer = raw_input()
	if answer == "QUIT":
		generate = False
	else:
		random_number = random.randint(1,5)
		# print random_number
		if random_number == 1:
			#print "Class A IP Address:"
			print(generate_class_A())
		elif random_number == 2:
			#print "Class B IP Address:"
			print(generate_class_B())
		elif random_number == 3:
			#print "Class C IP Address:"
			print(generate_class_C())
		# random number must be 4
		else:
			#print "APIPA IP Address:"
			print(generate_APIPA())

