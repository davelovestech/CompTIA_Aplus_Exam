#!/usr/bin/env python
# I didn't write this code. I'm just copying it.
# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz

"""
these are the answers in an order that is easily typable. see below for the code
"USB version 1.1 low speed? (megabits/s)" 					"1.5"
"USB version 1.1 low speed distance in meters?"					"3" 
"USB 1.1 full speed? (megabits/s) 						"12"
"USB 1.1 full speed distance in meters?"					"5"
"USB 2.0 speed in megabits/s?"							"480"
"USB 2.0 distance in meters?"							"5"
"USB 3.0 SuperSpeed speed in gigabits/s?" 					"5"
"USB 3.0 SuperSpeed distance in meters?"					"3"
"USB 3.1 SuperSpeed+ speed in Gb/s?"						"10"
"Thunderbolt max copper distance?"						"3"
"Thunderbolt max distance optical?" 						"60"
"Thunderbolt v1 single channel speed in gbit/s?"				"10"
"Thunderbolt v1 total thorughput in gbit/s?"					"20"
"Thunderbolt v1 connector?" 							"displayport"
"Thunderbolt v2 aggregated channel speed in gbit/s?" 				"20"
"Thunderbolt v2 connector?"							"displayport"
"Thunderbolt v3 speed in gbit/s?"						"40"
"Thunderbolt v3 connector type?" 						"USB type c"
"Firewire 400 IEEE 1394a speeds in Mbit/s? 					"100, 200, 400"
"firewire 400 IEEE 1394a max distance in meters?"				"72"
"firewire 400 IEEE1394a connection types?" 					"4-conductor and 6-conductor"
"Firewire 800 beta mode IEEE 1394b speed in mb/s?" 				"800"
"firewire 800 beta mode ieee 1394b optical connection distance (meters)?"	"100"
"firewire 800 category 5e cable max distance?" 					"100 meters"
"IrDA Speed in Mbit/s?" 							"4"
"IrDa distance in meters?" 							"1"
"sata 1 speed in Gbit/s?" 							"1.5"
"sata 1 distance in meters?"							"1"
"sata 2 speed in Gb/s?" 							"3"
"sata 2 distance in meters?"							"1"
"SATA 3 SPEED in gbit/s? 							"6"
"SATA 3 DISTANCE in meters?"							"1"
"SATA 3.2 SPEED sata express in Gb/s?" 						"16"
"ESATA DISTANCE?" 								"2"
"""
questions = [
"USB version 1.1 low speed? (megabits/s)", "USB version 1.1 low speed distance in meters?", "USB 1.1 full speed? (megabits/s)", "USB 1.1 full speed distance in meters?", "USB 2.0 speed in megabits/s?", "USB 2.0 distance in meters?", "USB 3.0 SuperSpeed speed in gigabits/s?", "USB 3.0 SuperSpeed distance in meters?", "USB 3.1 SuperSpeed+ speed in Gb/s?", "Thunderbolt max copper distance?", "Thunderbolt max distance optical?", "Thunderbolt v1 single channel speed in gbit/s?", "Thunderbolt v1 total thorughput in gbit/s?", "Thunderbolt v1 connector?", "Thunderbolt v2 aggregated channel speed in gbit/s?", "Thunderbolt v2 connector?", "Thunderbolt v3 speed in gbit/s?", "Thunderbolt v3 connector type?", "Firewire 400 IEEE 1394a speeds in Mbit/s?", "firewire 400 IEEE 1394a max distance in meters?", "firewire 400 IEEE1394a connection types?", "Firewire 800 beta mode IEEE 1394b speed in mb/s?", "firewire 800 beta mode ieee 1394b optical connection distance (meters)?", "firewire 800 category 5e cable max distance?", "IrDA Speed in Mbit/s?", "IrDa distance in meters?", "sata 1 speed in Gbit/s?", "sata 1 distance in meters?", "sata 2 speed in Gb/s?", "sata 2 distance in meters?", "SATA 3 SPEED in gbit/s?", "SATA 3 DISTANCE in meters?", "SATA 3.2 SPEED sata express in Gb/s?", "ESATA DISTANCE?"]

correct_choices = ["1.5", "3", "12", "5", "480", "5", "5", "3", "10", "3", "60", "10", "20", "displayport", "20", "displayport", "40", "USB type c", "100, 200, 400", "72", "4-conductor and 6-conductor", "800", "100", "100 meters", "4", "1", "1.5", "1", "3", "1", "6", "1", "16", "2"]
                   
answers = ["1.5", "3", "12", "5", "480", "5", "5", "3", "10", "3", "60", "10", "20", "displayport", "20", "displayport", "40", "USB type c", "100, 200, 400", "72", "4-conductor and 6-conductor", "800", "100", "100", "4", "1", "1.5", "1", "3", "1", "6", "1", "16", "2"]


def quiz():
    score = 0
    for question, correct_choice, answer in zip(questions, correct_choices, answers):
        print(question)
        user_answer = raw_input()
        if user_answer == correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions))

if __name__ == "__main__":
    quiz()
