#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path
from sqlite3 import connect
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient,DESCENDING
from wordcloud import WordCloud
from stop_words import get_stop_words
import json
import time 


start_time = time.time()
colors = []
#base_path = "/var/www/html/esperanza/public/img/home"
base_path = ""

def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return(colors[np.random.randint(0,len(colors))])

def get_word_image(text,stopwords,country):
    try:
        mask = np.array(Image.open(path.join(d, base_path+"sudamerica/"+country+"_mask.png")))
        stopwords = set(stop_words)
        wc = WordCloud(background_color="white", max_words=1500, mask=mask,
                    stopwords=stopwords, contour_width=2, contour_color='rgb(73, 70, 108)')
        wc.generate(text)
        wc.recolor(color_func = grey_color_func)
        wc.to_file(path.join(d, base_path+"sudamerica_word/"+country+"_words.png"))
    except:
        pass
MONGODB_AUTHSOURCE= 'admin'
MONGODB_HOST = '172.17.0.1'
MONGODB_PORT = 27017
DB_NAME = 'sudamerica_libre'
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
    # {
    # # 'name':'chile',
    # 'colors':[
    #     "rgb(0,56,165)",
    #     "rgb(204,204,204)",
    #     "rgb(213,43,30)"
    # ],
    # 'language': 'spanish'
    # },{
    # 'name':'argentina',
    # 'colors':[
    #     "rgb(115,172,222)",
    #     "rgb(213,211,13)",
    #     "rgb(204,204,204)"
    # ],
    # 'language': 'spanish'
    # },{
    # 'name':'venezuela',
    # 'colors':[
    #     "rgb(213,43,30)",
    #     "rgb(253,204,0)",
    #     "rgb(0,36,124)"
    # ],
    # 'language': 'spanish'
    # },
    # {
    # 'name':'brazil',
    # 'colors':[],
    # 'language': 'spanish'
    # },
]

connection = MongoClient(host=MONGODB_HOST,port=MONGODB_PORT, username=os.getenv('USER_DB_OS'), password=os.getenv('PASSWORD_DB_OS'),authSource=MONGODB_AUTHSOURCE)
db = connection[DB_NAME]
stop_words = get_stop_words('spanish')
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

for country in countries:
    collection = db[country['name']]
    text = ''
    data_collection = collection.find({}).sort([( '$natural', -1 )]).limit(1000)
    for document in data_collection:
        #text = text + document['message']
        text = text + document['message']+'\n'
    colors = country['colors']
    get_word_image(text, stop_words, country['name'])    
print("%s seconds" % (time.time() - start_time))
