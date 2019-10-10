#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 01:50:02 2019

@author: safayat
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# cd ~/Documents/kaggle/tmdb-box-office-prediction/
import pandas as pd
import numpy as np
import json
from nltk import flatten
from itertools import groupby
import re

train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

train['gnr'] = train['genres'].apply(lambda x: x.replace("'", "\"") if type(x) is str else x)
train['gnr'] = train['gnr'].apply(lambda x : list(map(lambda g: g['name'], json.loads(x))) if type(x) is str else []) 

genres_list = list(train['gnr'].values)
count_genres = [ (i, len(list(c))) for i,c in groupby(sorted(flatten(genres_list)))]
sorted_count_genres = sorted(count_genres, key=lambda x: x[1], reverse=1)


for i in range(15):
    train['genre_' + sorted_count_genres[i][0]] = train['gnr'].apply(lambda x: 1 if sorted_count_genres[i][0] in x else 0)


def toJson(col):
    return train[col].apply(lambda x: x.replace("'", "\"").replace("\\x",'') if type(x) is str else x).apply(lambda x: json.loads(x) if type(x) is str else [])

def stringToArray(str):
    p = re.compile('\'name\': \'[^\']+\'')
    names = map(lambda x: x.split(':')[1], p.findall(str))
    return list(map(lambda x: x.strip()[1:len(x.strip())-1] , names))        


