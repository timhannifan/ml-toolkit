'''
Class for parsing and cleaning data
'''
import sys
import numpy
import pandas as pd


class DataParser:
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
        print('parser called with ', type(param))
        self.load_src = param
    def execute(self):
        print('parser execution called')

    def output(self):
        '''
        Returns the current stored output (post-read data)
        '''
        return self.postread