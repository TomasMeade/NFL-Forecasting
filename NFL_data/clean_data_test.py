#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:14:30 2023

@author: tomasmeade
"""

import pandas as pd
import numpy as np

# example of generating snapshots for one player for snapshot at week 1 in 2016

all_stats_df = pd.read_csv('data/all_stats/all_stats.csv')

na = pd.DataFrame(all_stats_df['fpts'].isna())

indexes = na[na['fpts'] == False].index

all_stats_df = all_stats_df.iloc[indexes, :]

player = all_stats_df['player'][0]

obs = all_stats_df[all_stats_df['player'] == player]

ordered_obs = obs.sort_values(by = ['season', 'start_week'], ascending = [True, True])

delta = np.arange(1, len(ordered_obs)+1)

pred_fpts = ordered_obs['fpts'].shift(-1)

snap_df = pd.DataFrame(np.repeat(obs.values[:1], len(obs), axis=0), columns=obs.columns)

snap_df['delta'] = delta

snap_df['pred_fpts'] = pred_fpts.values

obs_new = obs.tail(-1)