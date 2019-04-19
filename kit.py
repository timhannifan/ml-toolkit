import sys
sys.path.append('./lib')
import pipeline
import reader
import dataparser
import features
import classifier
import evaluate
# import explorer


def build_pipe(path, target_col, dummify_target,
               discretize_cols, dummify_cols):
    '''
    Builds a complete pipeline using ml-toolkit classes
    '''
    pipe = pipeline.Pipeline()
    read_step = reader.CSVReader()
    parse_step = dataparser.DataParser()
    features_step = features.FeatureGenerator()
    classify_step = classifier.Classifier()
    evaluate_step = evaluate.ModelEvaluator()
    pipe.clear()
    
    read_step.load(path)
    pipe.add(read_step)

    parse_step.configure({
        'fillna': 'mean'
    })
    pipe.add(parse_step)


    dum_cols = []
    if dummify_target:
        dum_cols.append(target_col)
    dum_cols.extend(dummify_cols)

    features_step.configure({
        'discretize': discretize_cols,
        'dummify': dum_cols
    })
    pipe.add(features_step)

    classify_step.configure({
        'type': 'DecisionTreeClassifier',
        'target': 'SeriousDlqin2yrs_0'
    })
    pipe.add(classify_step)

    evaluate_step.configure({
        'metrics': ['accuracy_score']
    })
    pipe.add(evaluate_step)

    result = pipe.execute()
    print('Pipe completed with result type:', type(result))
    return result

def demo():
    return build_pipe(path='data/credit-data-small.csv',
                      target_col='SeriousDlqin2yrs_0',
                      dummify_target=False,
                      discretize_cols = [('MonthlyIncome', 
                                         ['low', 'med', 'high'])],
                      dummify_cols = ['discrete_MonthlyIncome',
                                      'SeriousDlqin2yrs'])

