
'''
Class for evaluating trained Classifier model
'''

from sklearn.metrics import accuracy_score

func_map = {
    'accuracy_score': accuracy_score
}

class ModelEvaluator:
    '''
    Class for evaluating trained Classifier model
    '''
    def __init__(self):
        self.input = None
        self.config = {}
        self.output = None

    def load_input(self, trained_classifier):
        '''
        Handles loading of trained classifier
        Input:
            trained_classifier: Classifier instance
        Returns: nothing
        '''
        print('ModelEvaluator loading with ', type(trained_classifier))
        self.input = trained_classifier

    def configure(self, params):
        '''
        Configures metrics used in evaluation type
        Input:
            params: {'metrics': ['accuracy_score']}
        Returns: nothing
        '''
        self.config = params

    def execute(self):
        '''
        Pipeline execution method. Kicks off evaluation process
        Input: none
        Returns: tuple containing trained model and metric dict
        '''
        print('ModelEvaluator execution called')
        
        metrics = {}
        for metric in self.config['metrics']:
            metrics[metric] = func_map[metric](self.input.y_train, 
                                          self.input.y_hats)

        self.output = (self.input.trained_model, metrics)
        return self.output
