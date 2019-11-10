#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient
from wordcloud import WordCloud
from stop_words import get_stop_words
import json

colors = []
#base_path = "/home/cr0wg4n/Escritorio/Work/sudamerica-wordcloud"
base_path = "."

def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    global colors  
    colors = [
        "rgb(236,46,46)",
        "rgb(48,173,31)",
        "rgb(213,211,13)"
    ]
    return(colors[np.random.randint(0,len(colors))])

def get_word_image(text,stopwords,country):
    try:
        mask = np.array(Image.open(path.join(d, base_path+"/sudamerica/"+country+"_mask.png")))
        stopwords = set(stop_words)
        wc = WordCloud(background_color="white", max_words=2000, mask=mask,
                    stopwords=stopwords, contour_width=3, contour_color='rgb(73, 70, 108)')
        wc.generate(text)
        wc.recolor(color_func = grey_color_func)
        wc.to_file(path.join(d, base_path+"/sudamerica_word/"+country+"_words.png"))
    except:
        pass
    


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'bolivia_libre'
countries = [
    {
    'name':'bolivia',
    'colors':[
        "rgb(236,46,46)",
        "rgb(48,173,31)",
        "rgb(213,211,13)"
    ],
    'language': 'spanish'
    },
    {
    'name':'chile',
    'colors':[],
    'language': 'spanish'
    },{
    'name':'argentina',
    'colors':[],
    'language': 'spanish'
    },{
    'name':'venezuela',
    'colors':[],
    'language': 'spanish'
    },{
    'name':'brazil',
    'colors':[],
    'language': 'spanish'
    },
]

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = connection[DB_NAME]
stop_words = get_stop_words('spanish')
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

for country in countries:
    print(country['name'])



collection = db["feedbacks"]
for document in collection.find():
    print (document)

get_word_image('mauricio matias conde',stop_words,'bolivia')
