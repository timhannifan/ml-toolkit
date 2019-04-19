'''
Various helper functions for parsing pandas data
'''

def fillna(fill_type, df):
    '''
    Fills all int and float columns in df with fill_type (supports mean only)
    '''
    for col in list(df.columns):
        dtype = df[col].dtype

        if dtype in ['int64', 'float64']:
            if fill_type == 'mean':
                df[col].fillna(df[col].mean(), inplace=True)

    return df

def categorize(targets, df):
    return df