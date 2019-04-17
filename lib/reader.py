'''
Class for building and executing a machine learning pipeline
'''

import csv


class Reader:
    '''
    Class for representing a way to read and deread text data.
    '''
    def __init__(self):
        self._buffer = ''
        self.read_output = ''

    def read(self, input_data):
        '''
        Reads in the input_data into the buffer of the deReader.

        Input:
        input_data (string): the data into insert into the buffer

        '''
        self._buffer = self._buffer + input_data

    def clear(self):
        '''
        Clears the contents of the internal buffer
        '''
        self._buffer = ''
        self.read_output = ''

    def print(self):
        '''
        Clears the contents of the internal buffer
        '''
        print(self.read_output)

    def output(self):
        '''
        Returns the current stored output (post-read data)
        '''
        return self.read_output


class CSVReader(Reader):
    '''
    Class for reading CSV files.
    '''
    def __init__(self):
        '''
        Constructs
        '''
        super().__init__()

    def read(self, input_data):
        '''
        Output:
            A string of the readed data
        '''
        self._buffer = self._buffer + input_data
        self.read_output = 'read data'
