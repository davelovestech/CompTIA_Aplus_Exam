#!/usr/bin/env python2

# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = []

correct_choices = []
                   
answers = []


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



