'''
Class for parsing and cleaning data
'''
import sys
import numpy
import pandas as pd
import utils

func_map = {
    'fillna': utils.fillna
}

class DataParser:
    '''
    Class for representing a way to read and deread text data.
    '''
    def __init__(self):
        self.input = None
        self.config = {}
        self.output = None

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
            df = func_map[fn](df, targets)
        
        self.output = df
        return self.output

    def output(self):
        '''
        Returns the current stored output (post-read data)
        '''
        return self.output