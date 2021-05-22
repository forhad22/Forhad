
#/usr/bin/python2

import os
import sys
#This tool is coded in python2 by Forhad Ekbl.

print("\033[93m ")
os.system("clear")
os.system("figlet F.E.E.")
url = raw_input ("[+] Enter Websit : ")
os.system("whois %s" % (url))