#!/usr/bin/env python
# I didn't write this code. I'm just copying it.
# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = ["SDRAM Number of Pins?", "DDR SDRAM Number of Pins?", "DDR2 SDRAM Number of Pins?", "DDR3 SDRAM NUmber of Pins?", "DDR4 SDRAM Number of Pins?", "SODIMM SDRAM Pins?", "SODIMM SDRAM DDR2 Pins?", "SODIMM SDRAM DDR3 Pins?", "SODIMM SDRAM DDR4 Pins?", "MicroDIMM SDRAM DDR Pins?", "MicroDIMM SDRAM DDR2 Pins?", "MicroDIMM SDRAM DDR3 214 Pins?"]

correct_choices = ["168", "184", "240", "240", "288", "200", "200", "204", "260", "172", "214", "214"]
                   
answers = ["168", "184", "240", "240", "288", "200", "200", "204", "260", "172", "214", "214"]


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
