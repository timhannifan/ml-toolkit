import sys
sys.path.append('./lib')
import pipeline
import reader
import parser
import explorer
import features
import classifier

tools = {
    'pipeline': pipeline,
    'reader': reader,
    'parser': parser,
    'explorer': explorer,
    'features': features
}

def demo_small():
    pipel = tools['pipeline'].Pipeline
    readr = tools['reader'].CSVReader()
    readr.read('foo bar')
    output = readr.output()
    print(output)

    return 'demo_small ran'


