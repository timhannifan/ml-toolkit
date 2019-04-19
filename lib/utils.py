'''
Various helper functions for parsing pandas data
'''

import pandas as pd


def fillna(df, fill_type='mean'):
    '''
    Fills all int and float columns in df with fill_type (supports mean only)
    Input: 
        df: pandas dataframe
        fill_type (str) currentlys supports 'mean'
    Returns: Modified dataframe
    '''
    for col in list(df.columns):
        dtype = df[col].dtype

        if dtype in ['int64', 'float64']:
            if fill_type == 'mean':
                df[col].fillna(df[col].mean(), inplace=True)

    return df


def discretize(df, targets):
    '''
    Converts a continuous variable into a discrete variable
    Input:
        df: pandas dataframe 
        targets=[(target_column_name,[new_label1,...]),..]
    Returns: Modified dataframe
    '''
    for target in targets:
        col, labels = target
        new_col_name = 'discrete_' + col
        df[new_col_name] = pd.cut(df[col], len(labels), labels=labels)

    return df


def dummify(df, targets):
    '''
    Converts a categorical variable into dummy series
    Input: 
        df: pandas dataframe
        targets: (list of column names)
    Returns: Modified dataframe
    '''
    for col in targets:
        df = pd.get_dummies(df, prefix=col, columns=[col]) 

    return df
