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

train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

train['gnr'] = train['genres'].apply(lambda x: x.replace("'", "\"") if type(x) is str else x)
train['gnr'] = train['gnr'].apply(lambda x : list(map(lambda g: g['name'], json.loads(x))) if type(x) is str else []) 

genres_list = list(train['gnr'].values)
count_genres = [ (i, len(list(c))) for i,c in groupby(sorted(flatten(genres_list)))]
sorted_count_genres = sorted(count_genres, key=lambda x: x[1], reverse=1)



