
'''
Class for generating features/predictors
'''

from sklearn.metrics import accuracy_score

func_map = {
    'accuracy_score': accuracy_score
}

class ModelEvaluator:
    '''
    Class for representing model evaluation
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
        print('ModelEvaluator loading with ', type(param))
        self.input = param

    def configure(self, params):
        '''
        Clears the contents of the internal buffer
        '''
        self.config = params

    def execute(self):
        print('ModelEvaluator execution called')
        
        metrics = {}
        for metric in self.config['metrics']:
            metrics[metric] = func_map[metric](self.input.y_train, 
                                          self.input.y_hats)

        return (self.input.trained_model, metrics)
