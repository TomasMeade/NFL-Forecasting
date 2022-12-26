#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 16:05:53 2022

@author: tomasmeade
"""

import pandas as pd
import numpy as np

# example of generating snapshots for one player for snapshot at week 1 in 2016

all_stats_df = pd.read_pickle('all_stats_df.pickle')

player = all_stats_df['player'][0]

obs = all_stats_df[all_stats_df['player'] == player]

ordered_obs = obs.sort_values(by = ['season', 'start_week'], ascending = [True, True])

ordered_obs['delta'] = np.arange(0, len(ordered_obs))

temp = ordered_obs.copy()

temp['delta'] = temp['delta'].shift(-1)

temp['pred_fpts'] = temp['fpts'].shift(-1)

snap_df = pd.DataFrame(np.repeat(obs.values[:1], len(obs), axis=0), columns=obs.columns)

snap_df['delta'] = temp['delta'].values

snap_df['pred_fpts'] = temp['pred_fpts'].values

obs_new = obs.tail(-1)

# repeat the above