#!/usr/bin/env python
# I didn't write this code. I'm just copying it.
# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = ["802.11a frequency (GHz)?", "802.11a speed/channel (Mbit/s)?", "802.11a channels?", "802.11a max throughput (Mbit/s)?", "802.11a max range (meters)?", "802.11b frequency (GHz)?", "802.11b speed/channel (Mbit/s)?", "802.11b channels?", "802.11b max throughput (Mbit/s)?", "802.11b max range (meters)?", "802.11g frequency (GHz)?", "802.11g speed/channel (Mbit/s)?", "802.11g channels?", "802.11g max throughput (Mbit/s)?", "802.11g max range (meters)?", "802.11n frequency (GHz)?", "802.11n speed/channel (Mbit/s)?", "802.11n channels?", "802.11n max throughput (Mbit/s)?", "802.11n max range (meters)?", "802.11ac frequency (GHz)?"	, "802.11ac speed/channel (Mbit/s)?", "802.11ac channels?", "802.11ac max throughput (Mbit/s)?", "802.11ac max range (meters)?"]

correct_choices = ["5", "54", "1", "54", "120", "2.4", "11", "1", "11", "140", 
"2.4", "54", "1", "54", "140", "5 and 2.4", "150", "4", "600", "250", "5", "866.7", 
"8", "6,934", "250"]
                   
answers = ["5", "54", "1", "54", "120", "2.4", "11", "1", "11", "140", 
"2.4", "54", "1", "54", "140", "5 and 2.4", "150", "4", "600", "250", "5", "866.7", 
"8", "6,934", "250"]


def quiz():
    score = 0
    for question, correct_choice, answer in zip(questions, correct_choices, answers):
        print(question)
        user_answer = str(input())
        if user_answer == correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions))

if __name__ == "__main__":
    quiz()
"""
"802.11a frequency (GHz)?" 			"5" 
"802.11a speed/channel (Mbit/s)?" 		"54" 
"802.11a channels?"				"1"
"802.11a max throughput (Mbit/s)?"		"54"
"802.11a max range (meters)?"			"120"

"802.11b frequency (GHz)?"			"2.4"
"802.11b speed/channel (Mbit/s)?" 		"11"
"802.11b channels?"		"1"
"802.11b max throughput (Mbit/s)?"		"11"
"802.11b max range (meters)?"			"140" 

"802.11g frequency (GHz)?"			"2.4"
"802.11g speed/channel (Mbit/s)?" 		"54"
"802.11g channels?"				"1"
"802.11g max throughput (Mbit/s)?"		"54" 
"802.11g max range (meters)?"			"140" 

"802.11n frequency (GHz)?"			"5 and 2.4"
"802.11n speed/channel (Mbit/s)?" 		"150"
"802.11n channels?"				"4"
"802.11n max throughput (Mbit/s)?"		"600"
"802.11n max range (meters)?"			"250"

"802.11ac frequency (GHz)?"			"5"
"802.11ac speed/channel (Mbit/s)?" 		"866.7"
"802.11ac channels?"				"8"
"802.11ac max throughput (Mbit/s)?"		"6,934"
"802.11ac max range (meters)?"			"250" 
"""
