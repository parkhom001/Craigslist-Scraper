#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 07:53:50 2019

@author: parsakon
"""

import gmplot
import pandas as pd

df = pd.read_csv('sampler.csv')

print(df.columns.values)

lat_list = df['Latitude']
long_list = df['Longitude']
print(lat_list[0])
print(long_list[0])

gmap = gmplot.GoogleMapPlotter(lat_list[0],long_list[0],15)
gmap.apikey ='API_KEY_HERE'
gmap.scatter(lat_list,long_list, '#FF0000', size =40, marker=True)
gmap.draw('/home/parsakon/Desktop/mapprac1.html')