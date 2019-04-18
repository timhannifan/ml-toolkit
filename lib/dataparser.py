'''
Class for parsing and cleaning data
'''
import sys
import numpy
import pandas as pd
import parseutil as pu

func_map = {
    'fillna': pu.fillna,
    'categorize': pu.categorize
}

class DataParser:
    '''
    Class for representing a way to read and deread text data.
    '''
    def __init__(self):
        self.load_src = None
        self.config = {}

    def clear(self):
        '''
        Clears the contents of the internal buffer
        '''
        self.load_src = None

    def print(self):
        '''
        Clears the contents of the internal buffer
        '''
        print('Current output is of type:', type(self.load_src))

    def load(self, param):
        '''
        Clears the contents of the internal buffer
        '''
        print('parser loading with ', type(param))
        self.load_src = param

    def configure(self, params):
        '''
        Clears the contents of the internal buffer
        '''
        self.config = params

    def execute(self):
        print('parser execution called')
        for fn, targets in self.config.items():
            func_map[fn](targets)
        
        self.output = 'dataparser output'
        return self.output

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
        return self.load_src