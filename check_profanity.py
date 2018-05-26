#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 12:55:19 2018

@author: ksato
"""
import urllib

def read_text():
    quotes = open("/Users/ksato/Desktop/MOOCS Study/OOP-python/movie_quotes.txt")
    contents_of_file = quotes.read()
    formattedfile = contents_of_file.replace(' ', '')
    print (formattedfile)
    quotes.close()
    check_profanity(formattedfile)
    
    
def check_profanity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q="+text_to_check
    print (url)
    
    connection = urllib.request.urlopen(url)
    output = connection.read()
    print(output)
    connection.close()
    
    if b'true' in output:
        print ("profanity alert!!")
    elif b'false' in output:
        print ("this document doesn't have any curse word")
        
    else:
        print ("we didn't recognize the input data, please check the data and try again")
    
    
read_text()