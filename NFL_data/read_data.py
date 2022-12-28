#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:20:35 2022

@author: tomasmeade
"""

import pandas as pd

# All data comes from FantasyPros execept the average draft position data
# which comes from fantasyData


all_stats_df = pd.read_csv('data/all_stats/all_stats.csv')
all_stats_df.to_pickle('all_stats_df.pickle')