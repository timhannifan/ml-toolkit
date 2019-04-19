'''
Class for representing different types of file readers
'''

import pandas as pd


class Reader:
    '''
    Class for representing different types of file readers
    '''
    def __init__(self):
        self.path = None
        self.output = None

    def load(self, path):
        '''
        Handles loading file path
        Input:
            path: directory path
        Returns: nothing
        '''
        self.path = path


class CSVReader(Reader):
    '''
    Child Class for reading CSV files.
    '''
    def __init__(self):
        super().__init__()

    def execute(self):
        '''
        Pipeline execution method. Reads csv file into pandas
        Input: none
        Returns: pandas dataframe
        '''
        print('Executing csvread with path', self.path)
        self.output = pd.read_csv(self.path)
        return self.output