#!/usr/bin/env python2

# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = ["Give user full priviledges, group read & write, and other read for 'example_python.py' with symbolic notation", "Give user full priviledges, group read & write, and other read for 'example_python.py' with octal permissions notation", "list directory contents in simple format", "list diredtory contents in long format", "create 'duck' directory", "change to 'duck' directory", "go up one directory", "move 'example_python.py' to 'duck' directory", "go to root directory", "print working directory", "copy 'python_test.py' and label it 'dis.k'", "remove the file python_test.py", "remove the duck directory with file removal prompts", "create an exact image of /dev/sda as /dev/sdb", "create a disk image of /dev/sda into /home as duck.img", "restore the duck image back into /dev/sda", "Change ownership of dis.k file from 'david' to 'mysql'", "view user processes", "view user processes as pages", "attempt to install wireshark as regular user", "install wireshark to Ubuntu as root", "become super user until you exit terminal", "print contents of python.py to terminal", "open python.py in a text editor shell", "search python.py for 'test'", "get wired TCP/IP properties of network connections", "get wireless TCP/IP properities of network", "end all VirtualBox instances", "determine packet path to 8.8.8.8", "force disk maintenance", "perform data backup of /home/folder1 into /home/folder2 with verbose, archive mode, compressed, human-readable"]

correct_choices = ["sudo chmod u=r,g=rwx,o=rwx example_python.py", "chmod 477 example_python.py", "ls", "ls -l", "mkdir duck", "cd duck", "cd ../", "mv example_python.py duck", "cd/", "pwd", "cp python_test.py dis.k", "rm python_test.py", "rm duck -r", "dd if=/dev/sda of=/dev/sdb", "dd if=/dev/sda of=/home/duck.img", "dd if/home/duck.img of=/dev/sda", "sudo chown mysql dis.k", "ps -e", "ps -e | more", "apt-get install wireshark", "sudo apt-get install wireshark", "su", "cat python.py", "vi python.py", "grep test python.py", "ifconfig", "iwconfig", "sudo killall VirtualBox", "traceroute 8.8.8.8", "sudo touch /forcefsck", "sudo rsync -azvh /home/folder1 /home/folder2"]
                   
answers = ["sudo chmod u=r,g=rwx,o=rwx example_python.py", "chmod 477 example_python.py", "ls", "ls -l", "mkdir duck", "cd duck", "cd ../", "mv example_python.py duck", "cd/", "pwd", "cp python_test.py dis.k", "rm python_test.py", "rm duck -r", "dd if=/dev/sda of=/dev/sdb", "dd if=/dev/sda of=/home/duck.img", "dd if/home/duck.img of=/dev/sda", "sudo chown mysql dis.k", "ps -e", "ps -e | more", "apt-get install wireshark", "sudo apt-get install wireshark", "su", "cat python.py", "vi python.py", "grep test python.py", "ifconfig", "iwconfig", "sudo killall VirtualBox", "traceroute 8.8.8.8", "sudo touch /forcefsck", "sudo rsync -azvh /home/folder1 /home/folder2"]


def quiz():
    score = 0
    for question, correct_choice, answer in zip(questions, correct_choices, answers):
        print(question)
        user_answer = raw_input().lower()
        if user_answer == correct_choice:
            print("Correct")
            score += 1
        else:
            print("Incorrect", answer)
    print(score, "out of", len(questions))

if __name__ == "__main__":
    quiz()

#################################################################################
"""
"Give user full priviledges, group read & write, and other read for 'example_python.py' with symbolic notation"			"sudo chmod u=r,g=rwx,o=rwx example_python.py" 
"Give user full priviledges, group read & write, and other read for 'example_python.py' with octal permissions notation"	"chmod 477 example_python.py"
"list directory contents in simple format"			"ls"
"list diredtory contents in long format"			"ls -l"
"create 'duck' directory"					"mkdir duck"
"change to 'duck' directory"					"cd duck"
"go up one directory"						"cd ../"
"move 'example_python.py' to 'duck' directory"			"mv example_python.py duck"
"go to root directory"						"cd/"
"print working directory"					"pwd"
"copy 'python_test.py' and label it 'dis.k'"			"cp python_test.py dis.k"
"remove the file python_test.py"				"rm python_test.py"
"remove the duck directory with file removal prompts"			"rm duck -r"
"create an exact image of /dev/sda as /dev/sdb"				"dd if=/dev/sda of=/dev/sdb"
"create a disk image of /dev/sda into /home as duck.img"	"dd if=/dev/sda of=/home/duck.img"
"restore the duck image back into /dev/sda"			"dd if/home/duck.img of=/dev/sda"
"Change ownership of dis.k file from 'david' to 'mysql'" 	"sudo chown mysql dis.k"
"view user processes" 						"ps -e"
"view user processes as pages"					"ps -e | more"
"attempt to install wireshark as regular user"			"apt-get install wireshark"
"install wireshark to Ubuntu as root"				"sudo apt-get install wireshark"
"become super user until you exit terminal"			"su"
"print contents of python.py to terminal"			"cat python.py"
"open python.py in a text editor shell"				"vi python.py"
"search python.py for 'test'"					"grep test python.py"
"get wired TCP/IP properties of network connections"		"ifconfig"
"get wireless TCP/IP properities of network"			"iwconfig"
"end all VirtualBox instances"					"sudo killall VirtualBox"
"determine packet path to 8.8.8.8"				"traceroute 8.8.8.8"
"force disk maintenance"					"sudo touch /forcefsck"
"perform data backup of /home/folder1 into /home/folder2 with verbose, archive mode, compressed, human-readable"					"sudo rsync -azvh /home/folder1 /home/folder2"
"""





















