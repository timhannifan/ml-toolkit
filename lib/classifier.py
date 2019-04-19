'''
Class for generating/training classification models
'''
import pandas as pd
import utils

from sklearn import tree

class Classifier:
    '''
    Class for representing classifier
    '''
    def __init__(self):
        self.input = None
        self.config = {}
        self.output = None

        self.model = None
        self.trained_model = None

    def load_input(self, df_in):
        '''
        Handles loading of dataframe
        Input:
            df_in: pandas dataframe
        Returns: nothing
        '''
        print('classifier loading with ', type(df_in))
        self.input = df_in

    def configure(self, params):
        '''
        Configures classifier type
        Input:
            params: {type: sklearn model}, only supports DecisionTree
        Returns: nothing
        '''
        if params['type'] == 'DecisionTreeClassifier':
            self.model = tree.DecisionTreeClassifier()
        self.config = params

    def generate_yhats(self, x_data):
        '''
        Generates predicted Y value on trained model
        Input:
            x_data: pandas dataframe
        Returns: nothing
        '''
        self.y_hats = self.trained_model.predict(x_data)

    def execute(self):
        '''
        Pipeline execution method. Trains model on input data
        Input: none
        Returns: self with trained_model attribute
        '''
        print('Classifier execution called')
        df = self.input
        target = self.config['target']
        classifier_type = self.config['type']

        # Generate y_train column as df
        self.y_train = df.loc[:, [target]]

        # Generate x_train columns as a set of all cols minus the target_col
        s = set(df.columns)
        s.remove(target)
        self.x_train = df.loc[:, list(s)]

        self.trained_model = self.model.fit(self.x_train, self.y_train)
        self.generate_yhats(self.x_train)

        return self
