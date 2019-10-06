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
train['gnr'] = train['genres'].apply(lambda x: x.replace("'", "\"") if type(x) is str else x)
train['gnr'] = train['gnr'].apply(lambda x : list(map(lambda g: g['name'], json.loads(x))) if type(x) is str else []) 

