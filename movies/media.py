#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 11:49:41 2018

@author: ksato
"""
import webbrowser

class Movie():
    """ This class helps to store movie related information """
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        