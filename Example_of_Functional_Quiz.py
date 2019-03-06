#!/usr/bin/env python
# I didn't write this code. I'm just copying it.
# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = ["What is 1 + 1",
             "Who is the 45th president of the United States?",
             "True or False... The Toronto Maple Leafs have won 13 Stanley   Cups?",
             "What was the last year the Toronto Maple Leafs won the Stanley   Cup?",
             "True or False... The current Prime Minister of Canada is Pierre Elliot Tredeau?"]
answer_choices = ["a)1\nb)2\nc)3\nd)4\n:",
                  "a)Barack Obama\nb)Hillary Clinton\nc)Donald Trump\nd)Tom Brady\n:",
                  ":",
                  "a)1967\nb)1955\nc)1987\nd)1994\n:",
                  ":"]
correct_choices = [{"b", "2"},
                   {"c", "donald trump"},
                   {"true", "t"},
                   {"a", "1967"},
                   {"false", "f"}]
answers = ["1 + 1 is 2",
           "The 45th president is Donald Trump",
           "",
           "The last time the Toronto Maple Leafs won the Stanley Cup was 1967",
           "The current Prime Minster of Canada is Justin Tredeau"]


def quiz():
    score = 0
    for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")

if __name__ == "__main__":
    quiz()
