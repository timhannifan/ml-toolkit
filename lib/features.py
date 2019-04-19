'''
Class for generating features/predictors
'''
import pandas as pd
import utils

func_map = {
    'discretize': utils.discretize,
    'dummify': utils.dummify
}

class FeatureGenerator:
    '''
    Class for generating features/predictors
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
        print('FeatureGenerator loading with ', type(df_in))
        self.input = df_in

    def configure(self, params):
        '''
        Configures feature generator with selected methods and cols
        Input:
            params: {'discretize': discretize_cols,
                    'dummify': dum_cols}
        Returns: nothing
        '''
        self.config = params

    def execute(self):
        '''
        Pipeline execution method. Processes dataframe with configuration
        Input: none
        Returns: processed dataframe
        '''
        print('FeatureGenerator execution called')

        df = self.input
        for fn, targets in self.config.items():
            df = func_map[fn](df, targets)

        self.output = df
        return self.output
