#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:20:35 2022

@author: tomasmeade
"""

import pandas as pd
from pathlib import Path

# All data comes from FantasyPros except the average draft position data
# which comes from fantasyData


# read all statistics
all_stats_df = pd.read_csv('data/all_stats/all_stats.csv')

# read snap counts
snap_count_16_20_df = pd.read_csv('data/snap_data/snap_counts_16_20.csv')
snap_count_21_22_df = pd.read_csv('data/snap_data/snap_counts_21_22.csv')

# read target counts
target_count_16_20_df = pd.read_csv('data/target_data/target_counts_16_20.csv')
target_count_21_22_df = pd.read_csv('data/target_data/target_counts_21_22.csv')

# read team target counts
team_target_count_df = pd.read_csv('data/team_target_data/team_target_counts.csv')

# read season ppr points

path = 'data/season_ppr_points'

files = Path(path).glob('*.csv')

points_dfs = list()
for f in files:
    data = pd.read_csv(f)
    # .stem is method for pathlib objects to get the filename w/o the extension
    data['file'] = f.stem
    points_dfs.append(data)

season_ppr_points_df = pd.concat(points_dfs, ignore_index=True)

# read ppr adp
path = 'data/ppr_adp'

files = Path(path).glob('*.csv')

points_dfs = list()
for f in files:
    data = pd.read_csv(f)
    # .stem is method for pathlib objects to get the filename w/o the extension
    data['file'] = f.stem
    points_dfs.append(data)

ppr_adp_df = pd.concat(points_dfs, ignore_index=True)




# read in season schedule data
import nfl_data_py as nfl

years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
schedule = nfl.import_schedules(years)



