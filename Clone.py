#! /usr/bin/python

import requests

""" Cloner Module : A total web page cloning solution """

def rip(url, filename)
    req = requests.get(url) #get webpage
    if len(req.text) > 1: #check if successfully ripped
        source = open(filename, 'w') #opens file for writing
        source.write(req.text) #writes file
        source.close #closes filestream
        return filename #returns the filename
