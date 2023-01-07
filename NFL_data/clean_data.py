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

# repeat the above

# generate all snapshots

def player_snapshot(obs):

    
    df = pd.DataFrame(columns=obs.columns)
    
    snaps = len(obs)-1
    
    for i in range(1, snaps+1):
        
        ordered_obs = obs.sort_values(by = ['season', 'start_week'], ascending = [True, True])
        
        delta = np.arange(1, len(ordered_obs))
        
        pred_fpts = ordered_obs['fpts'].shift(-1).dropna()
        
        snap_df = pd.DataFrame(np.repeat(obs.values[:1], len(obs)-1, axis=0), columns=obs.columns)
        
        snap_df['delta'] = delta
        
        snap_df['pred_fpts'] = pred_fpts.values
        
        df = pd.concat([df, snap_df])
        
        obs = obs.tail(-1)
    
    return df


player_df = player_snapshot(obs)


def all_player_snapshots(all_stats_df):
    
    df = pd.DataFrame(columns=all_stats_df.columns)
    
    players = all_stats_df['player'].unique()
    
    count = 0
    
    for player in players:
        
        count += 1

        obs = all_stats_df[all_stats_df['player'] == player]
        
        player_df = player_snapshot(obs)
        
        df = pd.concat([df, player_df])
        
    return df

players = all_stats_df['player'].unique()

all_players_df = all_player_snapshots(all_stats_df)


# pickle file is too large to push to github
# takes approx 5 min
all_players_df.to_pickle('all_players_df.pickle')