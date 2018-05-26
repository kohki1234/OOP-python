#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:43:20 2018

@author: ksato
"""

import os
from string import digits

def rename_files():
    file_list = os.listdir("/Users/ksato/Desktop/MOOCS Study/OOP-python/prank")
    print(file_list)
    
    saved_path = os.getcwd()
    print ("current working directory :" + saved_path)
    os.chdir("/Users/ksato/Desktop/MOOCS Study/OOP-python/prank")
    
    for filename in file_list:
        remove_digits = str.maketrans('', '', digits)
        os.rename(filename,filename.translate(remove_digits))
    
rename_files()