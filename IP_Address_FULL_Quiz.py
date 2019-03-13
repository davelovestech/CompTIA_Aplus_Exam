#!/usr/bin/env python2

import random
generate = True

print "Welcome to the IP Address Quiz!"

# defining variables
subnet_mask = 0
byte_one = 0
byte_two = 0
byte_three = 0
byte_four = 0

def build_IP_address(byte_one, byte_two, byte_three, byte_four):
	ip_address = str(byte_one) + "." + str(byte_two) + "." + str(byte_three) + "." + str(byte_four)
	return ip_address 
	

# private class a
# 10.0.0.0 - 10.255.255.255
def generate_private_class_A():
	#print "Class A IP Address:"
	byte_one = 10
	byte_two = random.randint(0,255)
	byte_three = random.randint(0,255)
	byte_four = random.randint(0,255)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

# private class b
# 172.16.0.0 - 172.31.255.255
def generate_private_class_B():
	#print "Class B IP Address:"
	byte_one = 172
	byte_two = random.randint(16,32)
	byte_three = random.randint(0,255)
	byte_four = random.randint(0,255)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

# private class c
# 192.168.0.0 - 192.168.255.255
def generate_private_class_C():
	#print "Class C IP Address:"
	byte_one = 192
	byte_two = 168
	byte_three = random.randint(0,255)
	byte_four = random.randint(0,255)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

def generate_class_A():
# private class a
# 10.0.0.0 - 10.255.255.255
	# public class a 1-126.0-255.0-255.0-255
	# before0_or_after1
	# before 0 is 1-9
	# after 0 is 11-126
	if before0_or_after1 == 0:
		byte_one = random.randint(1,9)
	else:
		byte_one = random.randint(11,126)
	byte_two = random.randint(0,255)
	byte_three = random.randint(0,255)
	byte_four = random.randint(0,255)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)
def generate_class_B():
# private class b
# 172.16.0.0 - 172.31.255.255
	# public class b 128-191.0-255.0-255.0-255
	# before0_or_after1
	# before0
	# after1
	byte_one = random.randint(128,191)
	if byte_one == 172:
		if before0_or_after1 == 0:
			byte_two = random.randint(0,15)
		else:
			byte_two = random.randint(32,255)
	else:
		byte_two = random.randint(0,255)
	byte_three = random.randint(0,255)
	byte_four = random.randint(0,255)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)
def generate_class_C():
# private class c
# 192.168.0.0 - 192.168.255.255
	# public class c 192-223.0-255.0-255.0-255
	# before0_or_after1
	# before0
	# after1 
	byte_one = random.randint(192,223)	
	if byte_one == 192:
		if before0_or_after1 == 0:
			byte_two = random.randint(0,167)
		else:
			byte_two = random.randint(169-255)
	else:
		byte_two = random.randint(0,255)
	byte_three = random.randint(0,255)
	byte_four = random.randint(0,255)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)



# APIPA
# 169.254.1.0 - 169.254.254.255
def generate_APIPA():
	#print "APIPA IP Address:"
	byte_one = 169
	byte_two = 254
	byte_three = random.randint(1,254)
	byte_four = random.randint(0,255)
	return build_IP_address(byte_one, byte_two, byte_three, byte_four)

IP_Address_Type = ""
answer = ""
score = 0
number_of_questions = 0
while generate == True:
	print "Enter 'QUIT' to exit this program.\n"
	#if quit_question == "QUIT":
	#	generate = False
	# this random number is for selecting what kind of IP address to make
	random_number = random.randint(1,7)
	# this random number is for generating public IP addresses
	# if it's 0, then public will be before the private.
	# if after 0, public will be after private
	before0_or_after1 = random.randint(0,1)
	#print "What kind of IP address is this?"
	# print random_number
	if random_number == 1:
		#print "Class A IP Address:"
		IP_Address_Type = "Private Class A"
		print(generate_private_class_A())
		#print random_number
	elif random_number == 2:
		#print "Class B IP Address:"
		IP_Address_Type = "Private Class B"
		print(generate_private_class_B())
		#print random_number
	elif random_number == 3:
		#print "Class C IP Address:"
		print(generate_private_class_C())
		IP_Address_Type = "Private Class C"
		#print random_number
	elif random_number == 4:
		print(generate_class_A())
		IP_Address_Type = "Class A"		
	elif random_number == 5:
		print(generate_class_B())
		IP_Address_Type = "Class B"
	elif random_number == 6:
		print(generate_class_C())
		IP_Address_Type = "Class C"
	# random number must be 7
	else:
		#print "APIPA IP Address:"
		print(generate_APIPA())
		IP_Address_Type = "APIPA"
		#print random_number
	
	#####	SUBNET Mask ###########
	if "Class A" in IP_Address_Type:
		subnet_mask = "255.0.0.0"
	elif "Class B" in IP_Address_Type:
		subnet_mask = "255.255.0.0"
	elif "Class C" in IP_Address_Type:
		subnet_mask = "255.255.255.0"
	else:
		subnet_mask = "255.255.0.0"	

	####### QUESTIONS #############
	print "================================"
	answer = raw_input("What is the IP Address type?\n")
	if answer == IP_Address_Type:
		print "Correct! IP Address type was: " + IP_Address_Type
		score += 1
		number_of_questions += 1	
	elif answer == "QUIT":
		generate = False
	else:
		print "WRONG! IP Address Type was: " + IP_Address_Type
		number_of_questions += 1
	print "--------------------------------"
	subnet_mask_guess = raw_input("What is the subnet mask?\n")
	if subnet_mask_guess == subnet_mask:
		print "Correct! Subnet mask was " + str(subnet_mask)
	elif subnet_mask_guess == "QUIT":
		generate = False
	else:
		print "WRONG! Subnet mask was: " + str(subnet_mask)
	print "================================"
score_percentage = score * 100 / number_of_questions
print "You got " + str(score) + " questions correct out of " + str(number_of_questions) + " questions."		
print "Your score is " + str(score_percentage) + " %."








