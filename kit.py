import sys
sys.path.append('./lib')
import pipeline
import reader
import dataparser
import features
import classifier
import evaluate
# import explorer

tools = {
    'pipeline': pipeline.Pipeline(),
    'csvreader': reader.CSVReader(),
    'dataparser': dataparser.DataParser(),
    'features': features.FeatureGenerator(),
    'classifier': classifier.Classifier(),
    'evaluate': evaluate.ModelEvaluator()
}

def small_demo():
    '''
    WHY
    '''
    pipe = tools['pipeline']
    read_step = tools['csvreader']
    parse_step = tools['dataparser']
    features_step = tools['features']
    classify_step = tools['classifier']
    evaluate_step = tools['evaluate']
    pipe.clear()
    
    read_step.load('data/credit-data.csv')
    pipe.add(read_step)

    parse_step.configure({
        'fillna': 'mean'
    })
    pipe.add(parse_step)

    features_step.configure({
        'discretize': [('MonthlyIncome', ['low', 'med', 'high'])],
        'dummify': ['discrete_MonthlyIncome', 'SeriousDlqin2yrs']
    })
    pipe.add(features_step)

    classify_step.configure({
        'type': 'DecisionTreeClassifier',
        'target': 'SeriousDlqin2yrs_1'
    })
    pipe.add(classify_step)

    evaluate_step.configure({
        'metrics': ['accuracy_score']
    })
    print('just configured')
    pipe.add(evaluate_step)

    result = pipe.execute()
    print('pipe completed', type(result))
    return result




