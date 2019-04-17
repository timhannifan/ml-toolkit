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
        self.source = None
        self.postread = None

    def clear(self):
        '''
        Clears the contents of the internal buffer
        '''
        self.source = None
        self.postread = None

    def print(self):
        '''
        Clears the contents of the internal buffer
        '''
        print('Current output is of type:', type(self.postread))
    def load(self, param):
        '''
        Clears the contents of the internal buffer
        '''
        self.load_src = param

    def output(self):
        '''
        Returns the current stored output (post-read data)
        '''
        return self.postread


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
        if self.load_src is not None:
            return self.read(self.load_src)

    def read(self, path):
        '''
        Reads csv, stores result in class instance, returns read data.
        '''
        try:
            data = pd.read_csv(path)
            self.read_result = data
            return data
        except:
            print('Error reading csv')
            return None

    @property
    def output(self):
        '''
        Output:
            Pandas dataframe of csv data
        '''
        return self.postread
