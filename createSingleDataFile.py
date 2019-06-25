#! /usr/bin/env python3

# script to append all the csv data files into 1
import csv
import os
import sys
import numpy as np
import pandas as pd
from sklearn.utils import shuffle

dataPath = 'CleanedTrafficData'  # use your path
fileNames = ['02-14-2018.csv', '02-15-2018.csv', '02-16-2018.csv',
             '02-22-2018.csv', '02-23-2018.csv', '03-01-2018.csv', '03-02-2018.csv']

df = pd.read_csv(os.path.join(dataPath, fileNames[0]))
print(df.shape)
for name in fileNames[1:]:
    fname = os.path.join(dataPath, name)
    print('appending:', fname)
    df1 = pd.read_csv(fname)
    df = df.append(df1, ignore_index=True)

df = shuffle(df)
print(df.shape)
print('creating multi-class file')
outFile = os.path.join(dataPath, 'IDS-2018-multiclass')
df.to_csv(outFile + '.csv', index=False)
df.to_pickle(outFile + '.pickle')
print('creating binary-class file')
df['Label'] = df['Label'].map(
    {'Benign': 0, 'FTP-BruteForce': 1, 'SSH-Bruteforce': 1, 'DoS attacks-GoldenEye': 1, 'DoS attacks-Slowloris': 1,
     'DoS attacks-SlowHTTPTest': 1, 'DoS attacks-Hulk': 1, 'Brute Force -Web': 1, 'Brute Force -XSS': 1,
     'SQL Injection': 1, 'Infilteration': 1, 'Bot': 1})
print(df['Label'][1:20])
outFile = os.path.join(dataPath, 'IDS-2018-binaryclass')
df.to_csv(outFile + '.csv', index=False)
df.to_pickle(outFile + '.pickle')
print('all done...')
