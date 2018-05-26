#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:21:02 2018

@author: ksato
"""

import webbrowser
import time
import datetime

for times in range(0,3): 
    time.sleep(1)
    webbrowser.open('https://www.youtube.com/watch?v=s_o1Wj-hS3s')
    print ("this application was casued at " + str(datetime.datetime.now()))
