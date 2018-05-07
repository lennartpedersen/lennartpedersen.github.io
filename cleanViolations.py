# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 11:06:16 2018

@author: Lennart Pedersen
"""

import numpy as np
import pandas as pd
import re

df = pd.read_csv("Fire_Violations.csv")

df.head()

data = df[['Violation Date','Violation Item Description','Location','Neighborhood  District']]

key1 = "Violation Date"
key2 = "Violation Item Description"

data = data[data.Location.notnull()]
data = data[data[key1].notnull()]
data = data[data[key2].notnull()]

lats = []
lons = []


for d in data.iterrows():   
    lon = d[1][2].split(',')[1]
    lon = lon[1:-1]
    lat = d[1][2].split(',')[0]
    lat = lat[1:]
    lats.append(lat)
    lons.append(lon)


data['Latitudes'] = lats
data['Longitudes'] = lons

data.to_csv('Violations.csv', sep=',')
