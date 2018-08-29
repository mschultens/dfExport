# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:55:57 2018

@author: SchultensM
"""

import pandas as pd

pathToFile = 'intentList.csv'
df = pd.read_csv(pathToFile, encoding='utf-8-sig', delimiter=';')


for index, row in df.iterrows():
   name = row['name']
   open('training/trainingInput' + name + '.txt', 'w+').close()
 
 