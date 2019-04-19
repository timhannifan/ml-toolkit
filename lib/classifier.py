'''
Class for generating features/predictors
'''
import pandas as pd
import utils

from sklearn import tree

class Classifier:
    '''
    Class for representing feature generatoion
    '''
    def __init__(self):
        self.input = None
        self.config = {}
        self.output = None

        self.model = None
        self.trained_model = None

    def load_input(self, param):
        '''
        Clears the contents of the internal buffer
        '''
        print('classifier loading with ', type(param))
        self.input = param

    def configure(self, params):
        '''
        Clears the contents of the internal buffer
        '''
        if params['type'] == 'DecisionTreeClassifier':
            self.model = tree.DecisionTreeClassifier()

        self.config = params

    def generate_yhats(self, x_data):
        self.y_hats = self.trained_model.predict(x_data)

    def execute(self):
        print('classifier execution called')
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
