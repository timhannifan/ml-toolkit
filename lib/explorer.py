'''
Class for parsing, cleaning, and filling data
'''
import pandas as pd
import utils


import pandas as pd
import numpy as np
import sklearn.preprocessing, sklearn.decomposition, \
         sklearn.linear_model, sklearn.pipeline, sklearn.metrics
#from sklearn.feature_extraction.text
from sklearn_pandas import DataFrameMapper
# import CountVectorizer

func_map = {
    'fillna': utils.fillna
}

class DataExplorer:
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
        print('DataExplorer loading with ', type(df_in))
        self.input = df_in

    def configure(self, params):
        '''
        Configures DataExplorer instance
        Input:
            params: dict
        Returns: nothing
        '''
        self.config = params

    def get_correlations(self, df):
        return df.corr

    def execute(self):
        '''
        Pipeline execution method. Runs DataExplorer on dataframe
        Input: none
        Returns: 
        '''
        print('DataExplorer execution called')
        df = self.input
        target =self.config['target']
        reports = self.config['reports']
        path =self.config['output_path']
        series = df[target]

        if 'correlations' in reports:
            corr_df = df.corr(method='pearson')

            target_corr = corr_df.loc[target]
            target_corr.sort_values(inplace=True)
            print(target_corr)

        if 'distributions' in reports:
        ## Todo: check for null vals in target col. This is breaking 
        ## classifier downstream. 
        # vc = series.isna().value_counts()
        # if True in list(vc.index):
            # if 'fill_target_mean' in self.config:
            #     print('--------filling')
            #     df = utils.fillna(df)

        if 'correlations' in reports:
            print('lets write some reports!')

        # # if 'correlations' in reports
        # for fn, targets in self.config.items():
        #     df = func_map[fn](df, targets)

        self.output = df
        return self.output
