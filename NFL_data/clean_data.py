#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 16:05:53 2022

@author: tomasmeade
"""

import pandas as pd
import numpy as np
from pathlib import Path


# =============================================================================
#  generate all snapshots
# =============================================================================


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



# all_stats_df = pd.read_csv('data/all_stats/all_stats.csv')

# na = pd.DataFrame(all_stats_df['fpts'].isna())

# indexes = na[na['fpts'] == False].index

# all_stats_df = all_stats_df.iloc[indexes, :]

# all_players_df = all_player_snapshots(all_stats_df)

# all_players_df.to_csv('clean_data/all_players_df.csv')
# all_players_df = pd.read_csv('clean_data/all_players_df.csv')

# =============================================================================
# add snap counts
# =============================================================================

# read snap counts
# need to drop rows with player in snap count columns
# snap_count_16_20_df = pd.read_csv('data/snap_data/snap_counts_16_20.csv')
# snap_count_21_22_df = pd.read_csv('data/snap_data/snap_counts_21_22.csv')

# snap_count_16_20_df = snap_count_16_20_df[pd.to_numeric(snap_count_16_20_df['season'], errors='coerce').notnull()]
# snap_count_21_22_df = snap_count_21_22_df[pd.to_numeric(snap_count_21_22_df['season'], errors='coerce').notnull()]
# snap_count_16_20_df['season'] = pd.to_numeric(snap_count_16_20_df['season'])
# snap_count_21_22_df['season'] = pd.to_numeric(snap_count_21_22_df['season'])

# snap_count_16_20_df = snap_count_16_20_df.drop_duplicates(['player', 'season'])
# snap_count_21_22_df = snap_count_21_22_df.drop_duplicates(['player', 'season'])

# all_players_df1 = all_players_df.merge(snap_count_16_20_df, how='left', on=['player', 'season'])

# all_players_df2 = all_players_df1.merge(snap_count_21_22_df, how='left', on=['player', 'season'])

# # clean snap count columns
# col1 = 'start_week'
# col2 = 'season'
# conditions  = [(all_players_df2[col1] == 1) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 2) & (all_players_df2[col2] <= 2020), 
#                (all_players_df2[col1] == 3) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 4) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 5) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 6) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 7) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 8) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 9) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 10) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 11) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 12) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 13) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 14) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 15) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 16) & (all_players_df2[col2] <= 2020),
#                (all_players_df2[col1] == 17) & (all_players_df2[col2] <= 2020),
               
#                (all_players_df2[col1] == 1) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 2) & (all_players_df2[col2] > 2020), 
#                (all_players_df2[col1] == 3) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 4) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 5) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 6) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 7) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 8) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 9) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 10) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 11) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 12) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 13) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 14) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 15) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 16) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 17) & (all_players_df2[col2] > 2020),
#                (all_players_df2[col1] == 18) & (all_players_df2[col2] > 2020)
#                ]

# choices = list(np.zeros(35))

# for i in range(35):
#     if i+1 <= 17:
#         choices[i] = all_players_df2[f'w{i+1}_x']
#     elif i+1 <= 34:
#         choices[i] = all_players_df2[f'w{i-16}_y']
#     else:
#         choices[i] = all_players_df2[f'w{i-16}']
        

    
# all_players_df2["snap_counts"] = np.select(conditions, choices, default=np.nan)


# # add prior year average snap counts

# prior_snaps_dct = {}
    
# for player in all_players_df2['player'].unique():
    
#     temp = all_players_df2.loc[all_players_df2['player'] == player]
#     temp_sea = {}
    
#     for season in [2016, 2017, 2018, 2019, 2020, 2021, 2022]:
        
#         temp2 = temp.loc[temp['season'] == season-1]
#         if temp2.shape[0] == 0:
#             temp_sea[season] = np.nan
#         else:   
#             temp3 = temp2.iloc[0]
#             if season <= 2020:
#                 temp_sea[season] = temp3['avg_x']
#             else:
#                 temp_sea[season] = temp3['avg_y']
#             del temp3
   
#         del temp2
            
#     prior_snaps_dct[player] = temp_sea
    
#     del temp_sea   
#     del temp

# col1 = 'season'
# col2  = 'player'

# prior_snap_counts = np.zeros(len(all_players_df2)).fill(np.nan)

# for player in all_players_df2['player'].unique(): 
#     conditions  = [(all_players_df2[col1] == 2016) & (all_players_df2[col2] == player),
#                    (all_players_df2[col1] == 2017) & (all_players_df2[col2] == player), 
#                    (all_players_df2[col1] == 2018) & (all_players_df2[col2] == player),
#                    (all_players_df2[col1] == 2019) & (all_players_df2[col2] == player), 
#                    (all_players_df2[col1] == 2020) & (all_players_df2[col2] == player),
#                    (all_players_df2[col1] == 2021) & (all_players_df2[col2] == player),
#                    (all_players_df2[col1] == 2022) & (all_players_df2[col2] == player)
#                     ]
    
#     choices = [prior_snaps_dct[player][2016], 
#                prior_snaps_dct[player][2017],
#                prior_snaps_dct[player][2018], 
#                prior_snaps_dct[player][2019],
#                prior_snaps_dct[player][2020],
#                prior_snaps_dct[player][2021],
#                prior_snaps_dct[player][2022]]
    
#     prior_snap_counts = np.select(conditions, choices, default=prior_snap_counts)
    
# all_players_df2['prior_snap_counts'] = prior_snap_counts

# all_players_df2.to_csv('clean_data/all_players_df2.csv')

# all_players_df2 = pd.read_csv('clean_data/all_players_df2.csv')

# drop columns
# all_players_df2 = all_players_df2[['player',  
#                                   'season', 
#                                   'start_week', 
#                                   'rank', 
#                                   'fpts',
#                                   'rost',
#                                   'delta',
#                                   'pred_fpts',
#                                   'pos_x',
#                                   'team_x',
#                                   'team_y',
#                                   'team',
#                                   'snap_counts',
#                                   'prior_snap_counts'
#                                   ]]

# fix team columns
# all_players_df2['clean_team'] = np.where(all_players_df2['season'] <= 2020, 
#                                          all_players_df2['team_y'], 
#                                          all_players_df2['team'])

# all_players_df2 = all_players_df2.drop(['team_x', 'team_y', 'team',], axis=1)
# all_players_df2 = all_players_df2.rename(columns={'clean_team': 'team', 'pos_x': 'pos'})

# =============================================================================
# add target counts
# =============================================================================

# read target counts
# target_count_16_20_df = pd.read_csv('data/target_data/target_counts_16_20.csv')
# target_count_21_22_df = pd.read_csv('data/target_data/target_counts_21_22.csv')

# target_count_16_20_df = target_count_16_20_df[pd.to_numeric(target_count_16_20_df['season'], errors='coerce').notnull()]
# target_count_21_22_df = target_count_21_22_df[pd.to_numeric(target_count_21_22_df['season'], errors='coerce').notnull()]
# target_count_16_20_df['season'] = pd.to_numeric(target_count_16_20_df['season'])
# target_count_21_22_df['season'] = pd.to_numeric(target_count_21_22_df['season'])

# target_count_16_20_df = target_count_16_20_df.drop_duplicates(['player', 'season'])
# target_count_21_22_df = target_count_21_22_df.drop_duplicates(['player', 'season'])

# all_players_df3 = all_players_df2.merge(target_count_16_20_df, how='left', on=['player', 'season'])

# all_players_df4 = all_players_df3.merge(target_count_21_22_df, how='left', on=['player', 'season'])

# # clean snap count columns
# col1 = 'start_week'
# col2 = 'season'
# conditions  = [(all_players_df4[col1] == 1) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 2) & (all_players_df4[col2] <= 2020), 
#                 (all_players_df4[col1] == 3) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 4) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 5) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 6) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 7) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 8) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 9) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 10) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 11) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 12) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 13) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 14) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 15) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 16) & (all_players_df4[col2] <= 2020),
#                 (all_players_df4[col1] == 17) & (all_players_df4[col2] <= 2020),
               
#                 (all_players_df4[col1] == 1) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 2) & (all_players_df4[col2] > 2020), 
#                 (all_players_df4[col1] == 3) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 4) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 5) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 6) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 7) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 8) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 9) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 10) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 11) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 12) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 13) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 14) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 15) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 16) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 17) & (all_players_df4[col2] > 2020),
#                 (all_players_df4[col1] == 18) & (all_players_df4[col2] > 2020)
#                 ]

# choices = list(np.zeros(35))

# for i in range(35):
#     if i+1 <= 17:
#         choices[i] = all_players_df4[f'w{i+1}_x']
#     elif i+1 <= 34:
#         choices[i] = all_players_df4[f'w{i-16}_y']
#     else:
#         choices[i] = all_players_df4[f'w{i-16}']
        

    
# all_players_df4["target_counts"] = np.select(conditions, choices, default=np.nan)


# # add prior year average snap counts

# prior_target_dct = {}
    
# for player in all_players_df4['player'].unique():
    
#     temp = all_players_df4.loc[all_players_df4['player'] == player]
#     temp_sea = {}
    
#     for season in [2016, 2017, 2018, 2019, 2020, 2021, 2022]:
        
#         temp2 = temp.loc[temp['season'] == season-1]
#         if temp2.shape[0] == 0:
#             temp_sea[season] = np.nan
#         else:   
#             temp3 = temp2.iloc[0]
#             if season <= 2020:
#                 temp_sea[season] = temp3['avg_x']
#             else:
#                 temp_sea[season] = temp3['avg_y']
#             del temp3
   
#         del temp2
            
#     prior_target_dct[player] = temp_sea
    
#     del temp_sea   
#     del temp

# col1 = 'season'
# col2  = 'player'

# prior_target_counts = np.zeros(len(all_players_df4)).fill(np.nan)

# for player in all_players_df4['player'].unique(): 
#     conditions  = [(all_players_df4[col1] == 2016) & (all_players_df4[col2] == player),
#                     (all_players_df4[col1] == 2017) & (all_players_df4[col2] == player), 
#                     (all_players_df4[col1] == 2018) & (all_players_df4[col2] == player),
#                     (all_players_df4[col1] == 2019) & (all_players_df4[col2] == player), 
#                     (all_players_df4[col1] == 2020) & (all_players_df4[col2] == player),
#                     (all_players_df4[col1] == 2021) & (all_players_df4[col2] == player),
#                     (all_players_df4[col1] == 2022) & (all_players_df4[col2] == player)
#                     ]
    
#     choices = [prior_target_dct[player][2016], 
#                 prior_target_dct[player][2017],
#                 prior_target_dct[player][2018], 
#                 prior_target_dct[player][2019],
#                 prior_target_dct[player][2020],
#                 prior_target_dct[player][2021],
#                 prior_target_dct[player][2022]]
    
#     prior_target_counts = np.select(conditions, choices, default=prior_target_counts)
    
# all_players_df4['prior_target_counts'] = prior_target_counts

# all_players_df4.to_csv('clean_data/all_players_df4.csv')
# all_players_df4 = pd.read_csv('clean_data/all_players_df4.csv')


# drop columns
# all_players_df4 = all_players_df4[['player',  
#                                   'season', 
#                                   'start_week', 
#                                   'rank', 
#                                   'fpts',
#                                   'rost',
#                                   'delta',
#                                   'pred_fpts',
#                                   'pos_x',
#                                   'team_x',
#                                   'snap_counts',
#                                   'prior_snap_counts',
#                                   'target_counts',
#                                   'prior_target_counts'
#                                   ]]

# all_players_df4 = all_players_df4.rename(columns={'team_x': 'team', 'pos_x': 'pos'})


# =============================================================================
# add team abbs
# =============================================================================

# abbs_df = pd.read_csv('data/generic/nfl_teams.csv')


# =============================================================================
# add team target counts
# =============================================================================

# read team target counts
# team_target_count_df = pd.read_csv('data/team_target_data/team_target_counts.csv')
# team_target_count_df = team_target_count_df.rename(columns={'team': 'Name'})

# team_target_count_df = team_target_count_df.merge(abbs_df, how='left', on='Name')
# team_target_count_df = team_target_count_df.rename(columns={'Abbreviation': 'team'})
# team_target_count_df = team_target_count_df.drop(columns=['ID', 'end_week'])

# all_players_df5 = all_players_df4.merge(team_target_count_df, how='left', on=['team', 'season', 'start_week'])

# =============================================================================
# add season ppr points
# =============================================================================

# path = 'data/season_ppr_points'

# files = Path(path).glob('*.csv')

# points_dfs = list()
# for f in files:
#     data = pd.read_csv(f)
#     # .stem is method for pathlib objects to get the filename w/o the extension
#     data['file'] = f.stem
#     points_dfs.append(data)

# season_ppr_points_df = pd.concat(points_dfs, ignore_index=True)

# new = season_ppr_points_df['file'].str.split('_', expand = True)
# season_ppr_points_df['cur_season'] = new[new.shape[1]-1]
# season_ppr_points_df['season'] = season_ppr_points_df['cur_season'].astype('int') + 1
# season_ppr_points_df = season_ppr_points_df.rename(columns={'Player': 'player'})
# season_ppr_points_df = season_ppr_points_df[['player', 'season', 'Points', 'Games', 'Avg']]
# season_ppr_points_df = season_ppr_points_df.drop_duplicates(subset=['player', 'season'])

# all_players_df6 = all_players_df5.merge(season_ppr_points_df, how='left', on=['player', 'season'])


# =============================================================================
# add ppr adp
# =============================================================================

# path = 'data/ppr_adp'

# files = Path(path).glob('*.csv')

# points_dfs = list()
# for f in files:
#     data = pd.read_csv(f)
#     # .stem is method for pathlib objects to get the filename w/o the extension
#     data['file'] = f.stem
#     points_dfs.append(data)

# ppr_adp_df = pd.concat(points_dfs, ignore_index=True)
# new = ppr_adp_df['file'].str.split('_', expand = True)
# ppr_adp_df['cur_season'] = new[new.shape[1]-1]
# ppr_adp_df['season'] = ppr_adp_df['cur_season'].astype('int') + 1
# ppr_adp_df = ppr_adp_df.rename(columns={'Name': 'player'})
# ppr_adp_df = ppr_adp_df[['player', 'season', 'Age', 'PositionRank', 'Week1ADP', 'Week2ADP', 'Week3ADP', 'HighestADP', 'LowestADP', 'AverageDraftPositionPPR']]
# ppr_adp_df = ppr_adp_df.drop_duplicates(subset=['player', 'season'])

# all_players_df7 = all_players_df6.merge(ppr_adp_df, how='left', on=['player', 'season'])

# all_players_df7.to_csv('clean_data/all_players_df7.csv')
# all_players_df7 = pd.read_csv('clean_data/all_players_df7.csv', low_memory=False, na_values='nan')


# =============================================================================
# add schedule
# =============================================================================


# read in season schedule data
# import nfl_data_py as nfl

# years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
# schedule = nfl.import_schedules(years)
# schedule = schedule[['season', 'week', 'away_team', 'home_team']]
# schedule['away_team'] = np.where(schedule['away_team']=='LA', 'LAR', schedule['away_team'])
# schedule['home_team'] = np.where(schedule['home_team']=='LA', 'LAR', schedule['home_team'])

# all_players_df7 = all_players_df7.rename(columns={"start_week": "week"})
# schedule = schedule.rename(columns={"away_team": "team"})

# all_players_df8 = all_players_df7.merge(schedule, how='left', on=['season', 'week', 'team'])

# schedule = schedule.rename(columns={"team": "away_team"})
# schedule = schedule.rename(columns={"home_team": "team"})

# all_players_df9 = all_players_df8.merge(schedule, how='left', on=['season', 'week', 'team'])

# all_players_df9['opp_team'] = np.where(all_players_df9['away_team'].isna(), 
#                                         np.array(all_players_df9['home_team']), 
#                                         np.array(all_players_df9['away_team']))


# =============================================================================
# add opp team prior year defense rank
# =============================================================================

# read ppr adp
# path = 'data/ppr_adp'

# files = Path(path).glob('*.csv')

# points_dfs = list()
# for f in files:
#     data = pd.read_csv(f)
#     # .stem is method for pathlib objects to get the filename w/o the extension
#     data['file'] = f.stem
#     points_dfs.append(data)

# ppr_adp_df = pd.concat(points_dfs, ignore_index=True)
# ppr_adp_dst_df = ppr_adp_df.loc[ppr_adp_df['Position']=='DST'].copy()
# new = ppr_adp_dst_df['file'].str.split('_', expand = True)
# ppr_adp_dst_df['cur_season'] = new[new.shape[1]-1]
# ppr_adp_dst_df['season'] = ppr_adp_dst_df['cur_season'].astype('int') + 1
# ppr_adp_dst_df = ppr_adp_dst_df.rename(columns={'Team': 'opp_team', 'PositionRank': 'opp_def_PositionRank', 'Week1ADP': 'opp_def_Week1ADP', 'Week2ADP': 'opp_def_Week2ADP', 'Week3ADP': 'opp_def_Week3ADP', 'HighestADP': 'opp_def_HighestADP', 'LowestADP': 'opp_def_LowestADP', 'AverageDraftPositionPPR': 'opp_def_AverageDraftPositionPPR'})
# ppr_adp_dst_df = ppr_adp_dst_df[['opp_team', 'season', 'opp_def_PositionRank', 'opp_def_Week1ADP', 'opp_def_Week2ADP', 'opp_def_Week3ADP', 'opp_def_HighestADP', 'opp_def_LowestADP', 'opp_def_AverageDraftPositionPPR']]
# ppr_adp_dst_df = ppr_adp_dst_df.drop_duplicates(subset=['opp_team', 'season'])

# all_players_df10 = all_players_df9.merge(ppr_adp_dst_df, how='left', on=['opp_team', 'season'])


# drop 2016 data
# all_players_df10 = all_players_df10.loc[all_players_df10['season']!=2016].copy()

# drop if team is na
# all_players_df10 = all_players_df10.loc[all_players_df10['team'].notna()].copy()


# all_players_df10.to_csv('clean_data/all_players_df10.csv')
all_players_df10 = pd.read_csv('clean_data/all_players_df10.csv')


