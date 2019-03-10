#!/usr/bin/env python
# I didn't write this code. I'm just copying it.
# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = ["FTP command port", "FTP data port", "SSH", "Telnet", "SMPT usual port is?", "SMTP is usually 25, what is the other?", "DNS", "DHCP destination is?", "DHCP client is?", "HTTP", "POP3", "IMAP", "SNMP", "LDAP", "SLP", "HTTPS", "SMB", "NetBIOS name service", "NetBIOS datagram service", "NetBIOS session service", "AFP can be 548 ... what is the other?", "AFP can be 427 ... what is the other?", "RDP"]

correct_choices = ["20", "21", "22", "23", "25", "587", "53", "67", "68", "80", "110", "143", "161", "389", "427", "443", "445", "137", "138", "139", "427", "548", "3389"]
                   
answers = ["20", "21", "22", "23", "25", "587", "53", "67", "68", "80", "110", "143", "161", "389", "427", "443", "445", "137", "138", "139", "427", "548", "3389"]


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
