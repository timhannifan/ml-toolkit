# ml-toolkit
A reusable group of Python classes and methods to create machine learning pipelines.

## Demo
From ipython3, run the following commands to build a complete pipeline based a modified version of the data from Kaggle's  ["Give Me Some Credit" competition.](https://www.kaggle.com/c/GiveMeSomeCredit). 

```
import kit
res = kit.demo()
```

## Components
### Pipeline
Class to process pipeline queue. Configured components are added to the Pipeline, which, when executed, handles the transfer of data and parameters between the execution of components.
```
import pipeline
pipe = pipeline.Pipeline()
pipe.add(Component)
pipe.execute()
```
### CSVReader
Class to process csv files. Configured with a path. Returns pandas df.
```
import reader

csvreader = reader.CSVReader()
csvreader.load('data/credit-data-small.csv')

pipe.add(csvreader)
```
### DataParser
Class to parse pandas dataframes. Configured with a dict of operations. Currently supports fillna with series mean.
```
import dataparser

datap = dataparser.DataParser()
datap.configure({
    'fillna': 'mean'
})

pipe.add(datap)
```
### DataExplorer
	* Todo
### FeatureGenerator
Class to parse pandas dataframes. Configured with a dict of operations. Currently supports fillna with series mean.
```
import features

fg = features.FeatureGenerator()
fg.configure({
  'discretize': [('MonthlyIncome', ['low', 'med', 'high'])],
  'dummify': ['discrete_MonthlyIncome', 'SeriousDlqin2yrs']
})

pipe.add(fg)
```
### Classifier
Class to create Classifier instance. Configured with a scikit classifier type and a target column to use as dependent variable. trained model is stored in the class instace. Currently supports DecisionTreeClassifier.
```
import classifier

cl = classifier.Classifier()
cl.configure({
    'type': 'DecisionTreeClassifier',
    'target': 'SeriousDlqin2yrs_0'
})

pipe.add(cl)
```

### ModelEvaluator



	⋅⋅* 