#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:20:35 2022

@author: tomasmeade
"""

import pandas as pd
import os
import pickle

# All data comes from FantasyPros execept the average draft position data
# which comes from fantasyData

def read_data(folder):
    
    entries = os.listdir(folder)
    
    df_dic = {}
    
    for entry in entries:
        name = entry.split('.')[0]
        df_dic[name] = pd.read_csv(folder + entry, encoding= 'unicode_escape')
    
    return df_dic
        

misc_df_dic = read_data('data/misc/')
with open('misc_df_dic.pickle', 'wb') as handle:
    pickle.dump(misc_df_dic, handle, protocol=pickle.HIGHEST_PROTOCOL)


all_stats_df = pd.read_csv('data/all_stats/all_stats.csv')
all_stats_df.to_pickle('all_stats_df.pickle')