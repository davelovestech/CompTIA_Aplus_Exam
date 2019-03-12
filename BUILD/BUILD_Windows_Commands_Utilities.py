#!/usr/bin/env python2

# the code is from https://codereview.stackexchange.com/questions/153495/simple-multiple-choice-quiz
questions = []

correct_choices = []
                   
answers = []


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
"Make the hidden file 'c:\config.sys' visible"		"attrib -h c:\config.sys"
"Make the folder 'c:\windows\system' read only" 	"attrib +r c:\windows\system"
"get help for the 'attrib' command"			"help attrib"
"How do you get, and modify, variables in Windows?"	"set"
"What command will get sp level of windows?"		"ver"
"Display all directories and paths"			"tree"
"list all fils and subdirectories in current directory" "dir"
"pause after each screen of dir info"			"dir /p"
"display who owns each file in the directory"		"dir /q"
"format the g drive for the NTFS file system *quickly*"	"format g: /q /fs:NTFS"
"Make a directory labelled 'pants'"			"md pants"
"Delete the syztem32 folder"				"rd syztem32"
"Remove the syztem32 folder and all subdirectories"	"rd /s syztem32"
"Change folders to the new 'pants' directory"		"cd pants"
"Navigate to root directory"				"cd\"
"Delete pants.rtf"					"del pants.rtf"
"Register a DLL labeled shmedia.dll"			"regsvr32 shmedia.dll"
"Scan the file C:\Windows\System32\iac25_32.ax"		"sfc /scanfile=c:\windows\system32\iac25_32.ax"
"Scan a c drive from another computer"			"sfc /offbootdir=c:\ /offwindir=c:\windows"
"Start a system scan immediately"			"sfc /scannow"
"Scan the system to find issues *without* fixing"	"sfc /verifyonly
"update the active directory policy"			"gpupdate"
"reapply all group policy settings (even unchanged ones)"	"gpupdate /force"
"logoff after group policy settings are updated"		"gpupdate /logoff"
"Restart after group policy settings are updated"	"gpupdate /boot"
"apply the next foreground policy synchronously"	"gpupdate /sync"
"update only this computer group policy settings"	"gpupdate /target:computer"
"update only the group policy settings for current user"	"gpupdate /target:user"
"wait 6 seconds before updating group policy settings"		"gpupdate /wait:6"
"display the group policy settings for the local user"		"gpresult /r"
"Check all drives at boot time with Autochk.exe"		"chkntfs /d"
"Schedule a disk check for drive C: at next reboot"	"chkntfs /C D:"
"Check the system for errors and repair them (NOT sectors)"	"chkdsk /f"
"Locate bad sectors, recover information, and repair system file errors"	"chkdsk /r"
"copy the file 'me.rtf' and name it 'me.txt'"			"copy me.rtf me.txt"
"copy the file 'me.rtf' and overwrite 'me.txt' without prompting"	"copy me.rtf me.txt /y"
"copy the file 'me.rtf', name it 'duck.txt', and verify writing"	"copy me.rtf duck.txt /v"
"Copy the 'pants' directory to 'socks', displaying complete source" 	"xcopy pants socks /f"
"Copy the 'pants' directory to 'socks' *and* include empty folders"	"xcopy pants socks /e"
"Copy 'thing' directory, of archived files, to 'thingy' *and* maintain archive status"	"xcopy thing thingy /a"
"copy encrypted files from 'saw' directory to 'boot', maintaining encryption"	"xcopy saw boot /g"
"copy the 'stuff' directory to 'things', ignoring empty folders"		"xcopy stuff things /s"
"copy directory 'dungeon' to 'dragons', maintaining NTFS permissions"	"robocopy dungeon dragons"
"scan and repair the MBR without overwriting the partition table"	"Bootrec.exe /fixmbr"
"Recreate the boot configuration data store (BCD)"			"Bootrec.exe /rebuildbcd"
"Write a new boot sector to fix the boot volume"			"Bootrec.exe /fixboot"
"Scan all drvie for installations compatible with Windows"		"Bootrec.exe /scanos"
"list currently running processes in the command prompt"		"tasklist"
"terminate the proces with the image name of wordpad.exe"		"taskkill /im wordpad.exe"
"terminate the process with PID of 3684"				"taskkill /PID 3684"
"shutdown the computer in 3 seconds"					"shutdown /s /t 3"
"shutdown the computer with a restart in 5 seconds"			"shutdown /r /t 5"
"uncompress d:\i386\hal.dl_ to c:\windows\system32"	"expand d:\i386\hal.dl_ c:\windows\system32"
"show the files in cabinet d:\i386\driver.cab"		"expand /d d:\i386\driver.cab"
"test reachability of 10.0.2.3"				"ping 10.0.2.3"
"ping 8.8.8.8 until stopped"				"ping -t 8.8.8.8"
"ping 8.8.8.8 and resolve address to hostname"		"ping -a 8.8.8.8"
"send 7 echo requests to 8.8.8.8"			"ping -n 7 8.8.8.8"
"ping, but don't fragment, 8.8.8.8"			"ping -f 8.8.8.8"
"ping 8.8.8.8 with 70 bytes per ping"			"ping -l 70 8.8.8.8"
"get all tcp/ip details"				"ipconfig /all"
"release DHCP lease"					"ipconfig /release"
"renew DHCP lease"					"ipconfig /renew"
"flush the DNS resolver cache"				"ipconfig /flushdns"
"determine the route a packet takes to get to 8.8.8.8"	"tracert 8.8.8.8"
"show active connections"				"netstat -a"
"show binaries (executable programs) involved in creating each connection"	"netstat -b"
"display active TCP connections and port numbers, but don't get names"	"netstat -n"
"list local netbios names"				"nbtstat -n"
"list remote netbios names for ip address 10.0.2.15"		"nbtstat -A 10.0.2.15"
"list remote netbios names for device IE11WIN8_1"	"nbtstat -a IE11WIN8_1"
"map the drive letter S to the share \\tower\movies"	"net use s: \\tower\movies"
"stop the print spooler service"			"net stop spooler"
"start the printer services"				"net start spooler"
"view network resources"				"net view"
"get DNS information for 8.8.8.8"			"nslookup 8.8.8.8"

"What stores information about applications’ file associations and Object Linking and Embedding (OLE)?" 		"HKEY_CLASSES_ROOT"
"What stores settings that concern the currently logged-on user. It is common to make changes in this hive?"			"HKEY_CURRENT_USER"
"What stores hardware and software settings that are specific to the computer, This is where the bulk of a PC technician’s registry edits are made. One example of data stored here are the programs that run when the OS starts?"	"HKEY_LOCAL_MACHINE"
"What stores data corresponding to all users who have ever logged on to the computer?"			"HKEY_USERS"
"What contains information that is gathered every time the computer is started up?"		"HKEY_CURRENT_CONFIG"


"Launch the windows group policy utility"		"gpedit.msc"
"Launch the Windows registry editor"			"regedit.exe"
"Launch the Windows services utility"			"services.msc"
"Launch the microsoft management console utility"	"mmc.exe"
"Launch the microsoft terminal services client (remote desktop)"	"mstsc.exe"
"Launch the Windows system information utility" 	"msinfo32.exe"
"Launch the directx diagnostic tools utility"		"dxdiag.exe"
"Launch the Microsoft Windows Device Manager"		"devmgmt.msc"
"Launch the system startup configuration modes"		"msconfig.exe"



























"Run a cmd prompt-based disk utility"				"diskpart.exe"
"Launch a Windows utility that displays sp level of Windows"	"msinfo32.exe"

