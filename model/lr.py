#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 17:43:19 2023

@author: tomasmeade
"""

# %%

# Import the dataset
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/tomasmeade/Documents/NFL-Forecasting/NFL_data/clean_data/all_players_final_sample.csv')


# %%

# Supervised Learning


# %%

# Prepare the data for analysis
Y = df['pred_fpts']
X = df.loc[:,['rank','fpts', 'rost', 'delta', 'pos', 'snap_counts', 
              'prior_snap_counts', 'target_counts', 'prior_target_counts', 
              'wr_targets', 'wr_percent', 'rb_targets', 'rb_percent',
              'te_targets', 'te_percent', 'total_targets', 'Points',
              'Games', 'Avg', 'Age', 'PositionRank', 'Week1ADP', 
              'Week2ADP', 'Week3ADP', 'HighestADP', 'LowestADP', 
              'AverageDraftPositionPPR', 'opp_def_PositionRank', 
              'opp_def_Week1ADP', 'opp_def_Week2ADP', 'opp_def_Week3ADP',
              'opp_def_HighestADP', 'opp_def_LowestADP', 'opp_def_AverageDraftPositionPPR']]


X['rost'] = df['rost'].str.replace('%','')
X = X.drop(columns=['pos'])
X['PositionRank'] = df['PositionRank'].str.replace(r'\D','', regex=True)
X['opp_def_PositionRank'] = df['opp_def_PositionRank'].str.replace(r'\D','', regex=True)


X = pd.concat((X ,pd.get_dummies(df['pos'])), axis=1)

X = X.replace(np.nan, -9999999)

# Split the data into training and test sets
# 70% training and 30% test
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3) 


# %%


# Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import mean_squared_error


# %%

# #### Linear Regression with L2


# %%

from sklearn.linear_model import RidgeCV

a = [.1, .5]

#Define model
lr = RidgeCV(cv=2, alphas=a)
# Train model
lr.fit(X_train, y_train)
print('Train MSE:', mean_squared_error(y_train, lr.predict(X_train)))

# Test performance
y_pred = lr.predict(X_test)
print('Test MSE:', mean_squared_error(y_test, lr.predict(X_test)))
