#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:40:26 2018

@author: ksato
"""

class Parent():
    def __init__(self,last_name, eye_color):
        print ("Parent is called")
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_info(self):
        print ("Last name is "+ self.last_name)
        print ("Eye color is " + self.eye_color )
        
        
        
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print ("Child is called")
        Parent.__init__(self,last_name, eye_color)
        self.number_of_toys = number_of_toys
        
    def show_info(self):
        print ("Last name is "+ self.last_name)
        print ("Eye color is " + self.eye_color )
        print ("Number of toys is " + str(self.number_of_toys))
        
#billy_cyrus.show_info()
#print (billy_cyrus.last_name)

miley_cyrus = Child("Cyrus","Blue",5)
miley_cyrus.show_info()
#print (miley_cyrus.last_name)
#print (miley_cyrus.number_of_toys)
