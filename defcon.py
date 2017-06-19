#! /usr/bin/python
import socket
from ping import *

def ping(ip):
	if verbose_ping(ip) == True:
		print ip, 'is Online'
	else:
                print ip, 'is Offline'

print "[!] Defcon : The Old Era IP Scanner"
print "[!] Created By : Sh4d0w-l0rd"
ip = raw_input("Please Enter your IP Address : ")
ipa = ip.split('.')
del ipa[3]
for r in range(1, 244):
	ipa.insert(3, str(r))
	ip_a = ".".join(ipa )
	ping(str(ip_a))
	del ipa[3]
