#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:04:04 2023

@author: tomasmeade
"""

import pandas as pd

# sample dataset 
# stratified random sample by season and week

df = pd.read_csv('clean_data/all_players_df10.csv')

sample_df = df.groupby(['season', 'week'], group_keys=False).apply(lambda x: x.sample(frac=0.35, random_state=1))
sample_df.to_csv('clean_data/all_players_final_sample.csv')


