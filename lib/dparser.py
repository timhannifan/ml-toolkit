'''
Class for parsing, cleaning, and filling data
'''
import pandas as pd
import utils

func_map = {
    'fillna': utils.fillna
}

class DataParser:
    '''
    Class for parsing, cleaning, and filling data
    '''
    def __init__(self):
        self.input = None
        self.config = {}
        self.output = None

    def load_input(self, df_in):
        '''
        Handles loading of dataframe
        Input:
            df_in: pandas dataframe
        Returns: nothing
        '''
        print('Parser loading with ', type(df_in))
        self.input = df_in

    def configure(self, params):
        '''
        Configures dataparser
        Input:
            params: dict
        Returns: nothing
        '''
        self.config = params

    def execute(self):
        '''
        Pipeline execution method. Runs parser on dataframe
        Input: none
        Returns: parsed/cleaned dataframe
        '''
        print('Parser execution called')
        df = self.input
        for fn, targets in self.config.items():
            df = func_map[fn](df, targets)

        self.output = df
        return self.output
