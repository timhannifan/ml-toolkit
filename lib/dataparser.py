'''
Class for parsing and cleaning data
'''
import sys
import numpy
import pandas as pd
import utils

func_map = {
    'fillna': utils.fillna,
    'categorize': utils.categorize
}

class DataParser:
    '''
    Class for representing a way to read and deread text data.
    '''
    def __init__(self):
        self.input = None
        self.config = {}
        self.output = None

    def clear(self):
        '''
        Clears the contents of the internal buffer
        '''
        self.input = None

    def print(self):
        '''
        Clears the contents of the internal buffer
        '''
        print('Current output is of type:', type(self.input))

    def load_input(self, param):
        '''
        Clears the contents of the internal buffer
        '''
        print('parser loading with ', type(param))
        self.input = param

    def configure(self, params):
        '''
        Clears the contents of the internal buffer
        '''
        self.config = params

    def execute(self):
        print('parser execution called')
        df = self.input
        for fn, targets in self.config.items():
            df = func_map[fn](targets, df)
        
        self.output = df
        return self.output

        # self.output = 'dataparser output'
        # return self.output

    def fillna(self, col_types):
        for col in coltypes:
            print('filling col '+str(col))

    def categorize(self, col_buckets):
        for col in col_buckets:
            print('should be categorizing', col)

    def output(self):
        '''
        Returns the current stored output (post-read data)
        '''
        return self.output

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