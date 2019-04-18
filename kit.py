import sys
sys.path.append('./lib')
import pipeline
import reader
import dataparser
# import explorer
# import features
# import classifier

tools = {
    'pipeline': pipeline.Pipeline(),
    'csvreader': reader.CSVReader(),
    'dataparser': dataparser.DataParser(),
    # 'explorer': explorer,
    # 'features': features
}

def small_demo():
    '''
    WHY
    '''
    pipe = tools['pipeline']
    read_step = tools['csvreader']
    parse_step = tools['dataparser']

    read_step.load('data/credit-data-small.csv')
    pipe.add(read_step)

    parse_step.configure({
        'fillna': [('col1', 'mean'), ('col2', 'median')],
        'categorize': [('col3', ['low', 'med', 'high'])]
    })
    pipe.add(parse_step)

    result = pipe.execute()
    print('pipe completed', type(result))

    # result = csvreader.execute()
    # print(result)


