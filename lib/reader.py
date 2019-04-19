'''
Class for building and executing a machine learning pipeline
'''
import sys
import numpy
import pandas as pd


class Reader:
    '''
    Class for representing a way to read and deread text data.
    '''
    def __init__(self):
        self.path = None
        self.output = None

    def load(self, param):
        '''
        Clears the contents of the internal buffer
        '''
        print('loading csvreader', param)
        self.path = param

    def output(self):
        '''
        Returns the current stored output (post-read data)
        '''
        return self.output


class CSVReader(Reader):
    '''
    Class for reading CSV files.
    '''
    def __init__(self):
        super().__init__()

    def execute(self):
        '''
        Kicks off read method with loaded src url. Called by pipeline.
        '''
        print('executing csvread with path', self.path)
        self.output = pd.read_csv(self.path)
        return self.output