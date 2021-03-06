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
# from sklearn_pandas import DataFrameMapper
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
        pd.set_option('display.width', 100)
        pd.set_option('precision', 3)

        if 'correlations' in reports:
            
            corr_df = df.corr(method='pearson')
            print('-------------Correlation matrix------------')
            print(corr_df)

            target_corr = corr_df.loc[target]
            target_corr.sort_values(inplace=True)
            print('-------------Class/variable correlations------------')
            print(target_corr)

        if 'summary_stats' in reports:
            rpt = df.describe()
            print('-------------Summary Statistics------------')
            print(rpt)

        if 'class_distribution' in reports:
            class_counts = df.groupby(target).size()
            print('-------------Class distribution------------')
            print(class_counts)

        if 'skew' in reports:
            skew = df.skew()
            print('-------------Skew------------')
            print(skew)




        ## Todo: check for null vals in target col. This is breaking 
        ## classifier downstream. 
        # vc = series.isna().value_counts()
        # if True in list(vc.index):
            # if 'fill_target_mean' in self.config:
            #     print('--------filling')
            #     df = utils.fillna(df)

        return self.input
