#!/usr/bin/env python
# I didn't write this code. I'm just copying it.
# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = ["Convert *DDR1 100 MHz* Memory Clock Speed to I/O Bus Clock Speed", "Convert *DDR1 100 MHz* I/O Bus Clock Speed to DDR Speed", "Convert *DDR-200 DDR1* Speed to Transfer per Second", "Convert *DDR1 200 Million* Transfers per Second to Transfer Rate", "Convert *DDR1 1,600 MB/s* Transfer Rate to Module Name", "Convert *DDR1 PC1-1600* Module Name to Transfer Rate", "Convert *DDR1 1,600 MB/s* Transfer Rate to Transfers per Second", "Convert *DDR1 200 Million* Transfers per Second to DDR Speed", "Convert *DDR1-200 DDR* Speed to I/O Bus Clock Speed", "Convert *DDR1 100 MHz* I/O Bus Clock Speed to Memory Clock Speed", "Convert *DDR2 100 MHz* Memory Clock Speed to I/O Bus Clock Speed"	"200 MHz", "Convert *DDR2 200 MHz* I/O Bus Clock Speed to DDR Speed", "Convert *DDR2-400 DDR2* Speed to Transfer per Second", "Convert *DDR2 400 Million* Transfers per Second to Transfer Rate", "Convert *DDR2 3,200 MB/s* Transfer Rate to Module Name", "Convert *DDR2 PC2-3200* Module Name to Transfer Rate", "Convert *DDR2 3,200 MB/s* Transfer Rate to Transfers per Second", "Convert *DDR2 400 Million* Transfers per Second to DDR Speed", "Convert *DDR2-400 DDR* Speed to I/O Bus Clock Speed", "Convert *DDR2 200 MHz* I/O Bus Clock Speed to Memory Clock Speed", "Convert *100 MHz DDR3* Memory Clock Speed to I/O Bus Clock Speed", "Convert *DDR3 400 MHz* I/O Bus Clock Speed to DDR Speed", "Convert *DDR-800 DDR3* Speed to Transfer per Second", "Convert *DDR3 800 Million* Transfers per Second to Transfer Rate", "Convert *DDR3 6,400 MB/s* Transfer Rate to Module Name", "Convert *DDR3 PC3-6400* Module Name to Transfer Rate", "Convert *DDR3 6,400 MB/s* Transfer Rate to Transfers per Second"	"800 Million", "Convert *DDR3 800 Million* Transfers per Second to DDR Speed", "Convert *DDR3-800 DDR* Speed to I/O Bus Clock Speed", "Convert *DDR3 400 MHz* I/O Bus Clock Speed to Memory Clock Speed"]

correct_choices = ["100 MHz", "DDR1-200", "200 Million", "1,600 MB/s", "PC1600", "1,600 MB/s", "200 Million", "DDR1-200", "100 MHz", "100 MHz", "200 MHz", "DDR2-400", "400 Million", "3,200 MB/s", "PC2-3200", "3,200 MB/s", "400 Million", "DDR2-400", "200 MHz", "100 MHz", "400 MHz", "DDR3-800", "800 Million", "6,400 MB/s", "PC3-6400", "6,400 MB/s", "800 Million", "DDR3-800", "400 MHz", "100 MHz"]
                   
answers = ["100 MHz", "DDR1-200", "200 Million", "1,600 MB/s", "PC1600", "1,600 MB/s", "200 Million", "DDR1-200", "100 MHz", "100 MHz", "200 MHz", "DDR2-400", "400 Million", "3,200 MB/s", "PC2-3200", "3,200 MB/s", "400 Million", "DDR2-400", "200 MHz", "100 MHz", "400 MHz", "DDR3-800", "800 Million", "6,400 MB/s", "PC3-6400", "6,400 MB/s", "800 Million", "DDR3-800", "400 MHz", "100 MHz"]


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
"""
# Here are all the quesitons and answers
#######################################################################################
"Convert *DDR1 100 MHz* Memory Clock Speed to I/O Bus Clock Speed"	"100 MHz"
"Convert *DDR1 100 MHz* I/O Bus Clock Speed to DDR Speed"		"DDR1-200"
"Convert *DDR-200 DDR1* Speed to Transfer per Second"			"200 Million"
"Convert *DDR1 200 Million* Transfers per Second to Transfer Rate" 	"1,600 MB/s"
"Convert *DDR1 1,600 MB/s* Transfer Rate to Module Name"		"PC1600"
--------------------------------------------------------------------------------------
"Convert *DDR1 PC1-1600* Module Name to Transfer Rate"			"1,600 MB/s"
"Convert *DDR1 1,600 MB/s* Transfer Rate to Transfers per Second"	"200 Million"
"Convert *DDR1 200 Million* Transfers per Second to DDR Speed"		"DDR1-200"
"Convert *DDR1-200 DDR* Speed to I/O Bus Clock Speed"			"100 MHz"
"Convert *DDR1 100 MHz* I/O Bus Clock Speed to Memory Clock Speed"	"100 MHz"
#######################################################################################
"Convert *DDR2 100 MHz* Memory Clock Speed to I/O Bus Clock Speed"	"200 MHz"
"Convert *DDR2 200 MHz* I/O Bus Clock Speed to DDR Speed"		"DDR2-400"
"Convert *DDR2-400 DDR2* Speed to Transfer per Second"			"400 Million"
"Convert *DDR2 400 Million* Transfers per Second to Transfer Rate" 	"3,200 MB/s"
"Convert *DDR2 3,200 MB/s* Transfer Rate to Module Name"		"PC2-3200"
--------------------------------------------------------------------------------------
"Convert *DDR2 PC2-3200* Module Name to Transfer Rate"			"3,200 MB/s"
"Convert *DDR2 3,200 MB/s* Transfer Rate to Transfers per Second"	"400 Million"
"Convert *DDR2 400 Million* Transfers per Second to DDR Speed"		"DDR2-400"
"Convert *DDR2-400 DDR* Speed to I/O Bus Clock Speed"			"200 MHz"
"Convert *DDR2 200 MHz* I/O Bus Clock Speed to Memory Clock Speed"	"100 MHz"
#######################################################################################
"Convert *100 MHz DDR3* Memory Clock Speed to I/O Bus Clock Speed"	"400 MHz"
"Convert *DDR3 400 MHz* I/O Bus Clock Speed to DDR Speed"		"DDR3-800"
"Convert *DDR-800 DDR3* Speed to Transfer per Second"			"800 Million"
"Convert *DDR3 800 Million* Transfers per Second to Transfer Rate" 	"6,400 MB/s"
"Convert *DDR3 6,400 MB/s* Transfer Rate to Module Name"		"PC3-6400"
--------------------------------------------------------------------------------------
"Convert *DDR3 PC3-6400* Module Name to Transfer Rate"			"6,400 MB/s"
"Convert *DDR3 6,400 MB/s* Transfer Rate to Transfers per Second"	"800 Million"
"Convert *DDR3 800 Million* Transfers per Second to DDR Speed"		"DDR3-800"
"Convert *DDR3-800 DDR* Speed to I/O Bus Clock Speed"			"400 MHz"
"Convert *DDR3 400 MHz* I/O Bus Clock Speed to Memory Clock Speed"	"100 MHz"
"""
