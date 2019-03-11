# CompTIA_Aplus_Exam
These are programs that I have written to test myself on essential concepts for the A+ Certification exam.

### Dictionary-Based Quizzes
I like dictionaries cause they're easy to randomize w/o fear of losing order ... I'm not a good enough coder to confidently not lose order w/ lists ... I might convert everything over to dicitonaries to add randomness ... is there a limit to the length of dictionary and key text?
stackoverflow says dictionary keys can be as long as the memory can support! both my systems have 16 GB of ram, so I'm sure it'll be fine https://stackoverflow.com/questions/22464900/do-dictionaries-have-a-key-length-limit

* Ports_Dictionary_Print.py IS NOT a quiz ... I need to fix this. It was an early iteration that just lists the dictionary and keys of the port dictionary. 

### List-Based Quizes
The issue with all of these is program failure when unexpected input is entered. They tell you the right answer when you're wrong, but it's in order ... that doesn't force the kind of learning I want for the exams ... I'll need to build these out w/ randomness ... How?
* Interface_List_Quiz.py is a list quiz that asks interface types, speeds and max distance questions in order. It tells you the right answer when you're wrong.
* Ports_List_Quiz.py asks the port questions in order and tells you the right answer when you're wrong. 
* RAM_Pin_List_Quiz.py asks the RAM pin questions in order and tells you when you're wrong. 
* WIFI_Channel_List_Quiz.py 

All of the list quizes have this basic structure:
```python
#!/usr/bin/env python
# I didn't write this code. I'm just copying it.
# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = ["question 1", question 2", "question 3"]

correct_choices = ["correct choice 1", "correct choice 2", "correct choice 3"]
                   
answers = ["correct answer 1", correct answer 2", "correct answer 3"]

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
```
### IP Address Quiz
* Generate_IP_Address.py was an early iteration that only makes simple IP addresses (no private vs public addresses). It does not ask questions. 
* IP_Address_Quiz.py generates IP addresses and asks what kind they are. I need to add private and subnet masks to this ... it also tells you when you're wrong, BUT not what the right answer is :(
### 

### Code I Need to Write
* laser printer steps
* malware steps
* troubleshooting steps
* device manager symbols
* windows commands
* linux commands
* locations of system files
* picture identifying motherboard parts
* picture identifying connectors 
* CAT 5 cable questions
* what utility does what?
* RAM math
* OSI layers
* windows registry and contents
* windows system utilities
* windows minimum requirements
* private vs public IP addresses. How many hosts vs machine IPs can this address have?
* what wireless security type is this?
* port triggering vs port forwarding
* virtualization tech vs. no execute tech


shadow copy volume snapshot service volume shadow copy service
NX bit for intel is XD bit no execute

virtualizaiton for intel is VT-x. amd-v is amd.










































