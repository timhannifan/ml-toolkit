import sys
sys.path.append('./lib')
import pipeline
import reader
import parser
import explorer
import features
import classifier

tools = {
    'pipeline': pipeline.Pipeline,
    'csvreader': reader.CSVReader(),
    'parser': parser,
    'explorer': explorer,
    'features': features
}

def small_demo():
    pipel = tools['pipeline']
    csvreader = tools['csvreader']
    
    data = csvreader.load('data/credit-data-small.csv')

    result = csvreader.execute()
    print(result)

