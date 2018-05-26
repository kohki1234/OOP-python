#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 12:14:31 2018

@author: ksato
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "story of boy and toys which got life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "strange avatar character from CG moves in fake world",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

pulp_fiction = media.Movie("Pulp Fiction",
                           "The film tells a few stories of criminal Los Angeles. The film's title refers to the pulp magazines and hardboiled crime novels popular during the mid-20th century, known for their graphic violence and punchy dialogue.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg")


school_of_rock = media.Movie("School of rock",
                             "the story about rock love teacher",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

buffalo66 = media.Movie("Buffalo '66",
                        "Buffalo '66 is a 1998 comedy-drama film that is writer-director Vincent Gallo's full-length motion picture debut.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Buffalo_sixty_six_ver1.jpg/220px-Buffalo_sixty_six_ver1.jpg",
                        "https://www.youtube.com/watch?v=1duitd-N1Us")

rashomon = media.Movie("Rashomon",
                       "The film is known for a plot device that involves various characters providing subjective, alternative, self-serving and contradictory versions of the same incident.",
                       "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Rashomon_poster_2.jpg/220px-Rashomon_poster_2.jpg",
                       "https://www.youtube.com/watch?v=xCZ9TguVOIA")



#print (toy_story.storyline)
#print (avatar.storyline)
#avatar.show_trailer()

#pulp_fiction.show_trailer()
#print (pulp_fiction.poster_image_url)
#movies = [toy_story,avatar,pulp_fiction,school_of_rock,buffalo66,rashomon]
#fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
print (media.Movie.__module__)