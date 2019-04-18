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
        self.read_result = None

    def clear(self):
        '''
        Clears the contents of the internal buffer
        '''
        self.source = None
        self.output = None
        self.path = ''

    def print(self):
        '''
        Clears the contents of the internal buffer
        '''
        print('Current output is of type:', type(self.output))
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
        # print('path', self.path)
        # print('self', self)
        
        # print('output',type(self.output))
        self.output = pd.read_csv(self.path)
        print('csvread output', type(self.output))
        return self.output

    def read_path(self):
        '''
        Reads csv, stores result in class instance, returns read data.
        '''
        print('CALLING READpath')
        # try:
        #     data = 
        #     self.output = data
        #     return self.output
        # except:
        #     print('Error reading csv')
        #     return None

    # @property
    # def output(self):
    #     '''
    #     Output:
    #         Pandas dataframe of csv data
    #     '''
    #     return self.output
