#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 12:32:15 2018

@author: ksato
"""

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    
    angie = turtle.Turtle()
    angie.forward(100)
    
    window.exitonclick()

    
draw_square()