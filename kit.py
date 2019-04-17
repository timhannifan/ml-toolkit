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
    'csvreader': reader.CSVReader,
    'parser': parser,
    'explorer': explorer,
    'features': features
}

def demo_small():
    pipel = tools['pipeline']
    csvreader = tools['csvreader']
    
    # data = csvreader.read(fname='/data/credit-data-small.csv')
    csvreader.read()
    # print(data.head())
    # output = readr.output()
    # print(output)

    return 'demo_small ran'


