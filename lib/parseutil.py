'''
Various helper functions for parsing pandas data
'''

def fillna(targets, df):
    for target in targets:
        col, fill_type = target

        if fill_type == 'mean':
            df[col].fillna(df[col].mean(), inplace=True)
    return df

def categorize(targets, df):
    return df