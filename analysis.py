# Code originally written by Rayid Ghani. https://github.com/rayidghani/magicloops
# Repurposed and ammended here for a different dataset

from __future__ import division
import pandas as pd
import numpy as np
import os
import sys
import matplotlib
import matplotlib.pyplot as plt
import pylab as pl
from datetime import timedelta
from datetime import datetime
import random
from scipy import optimize
import time
import seaborn as sns
import csv

from mlfunctions import *
# %matplotlib inline

def main(inp, outp, mod, gsize):

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    # parse input parameters

    # csv df file to be used as input
    infile = inp

    # the filename we want to write results to
    outfile = outp

    # which model(s) to run
    model = mod

    # which parameter grid do we want to use (test, small, large)
    grid_size = gsize

    #read the csv df
    df = pd.read_csv(infile)

    # setting variables
        # which variable to use for prediction_time
    prediction_length = 60
    prediction_time = 'date_posted'
    timestamp_prediction_time = 'tmstmp_date_posted'
    raw_outcome_col = 'datefullyfunded'
    timestamp_raw_outcome = 'tmstmp_datefullyfunded'
    binary_outcome_col = 'not_funded_within_60'

    # convert dates, create timedelta column
    df[timestamp_raw_outcome] = pd.to_datetime(df[raw_outcome_col])
    df[timestamp_prediction_time] = pd.to_datetime(df[prediction_time], format='%m/%d/%y')
    df['diff'] = df[timestamp_raw_outcome] - df[timestamp_prediction_time]
    df['diff'] = df['diff'].apply(lambda x: x.days)

    # generate binary outcome
    df.loc[df['diff'] > prediction_length, 'not_funded_within_60'] = 1
    df.loc[df['diff'] <= prediction_length, 'not_funded_within_60'] = 0

    # define outcomes to classify
    outcomes = ['not_funded_within_60']

    # generate some dummies manually
    df['school_charter'] = np.where(df['school_charter']=="t", 1, 0)
    df['school_magnet'] = np.where(df['school_magnet']=="t", 1, 0)
    df['eligible_double_your_impact_match'] = np.where(
        df['eligible_double_your_impact_match']=="t", 1, 0)

    # generate some dummies for categorical variables
    cols_to_transform = ['primary_focus_area',
                     'poverty_level', 'teacher_prefix', 'resource_type',
                     'grade_level']
    df = pd.get_dummies( df, dummy_na=True, columns = cols_to_transform )

    selected_features = ['school_latitude', 'school_longitude', 
       'school_charter','school_magnet', 
       'total_price_including_optional_support','students_reached',
       'not_funded_within_60', 'primary_focus_area_Applied Learning',
       'primary_focus_area_Health & Sports',
       'primary_focus_area_History & Civics',
       'primary_focus_area_Literacy & Language',
       'primary_focus_area_Math & Science',
       'primary_focus_area_Music & The Arts',
       'primary_focus_area_Special Needs', 'primary_focus_area_nan',
       'poverty_level_high poverty', 'poverty_level_highest poverty',
       'poverty_level_low poverty', 'poverty_level_moderate poverty',
       'poverty_level_nan', 'teacher_prefix_Mr.', 'teacher_prefix_Mrs.',
       'teacher_prefix_Ms.', 'teacher_prefix_nan', 'resource_type_Books',
       'resource_type_Other', 'resource_type_Supplies',
       'resource_type_Technology', 'resource_type_Trips', 'resource_type_nan',
       'grade_level_Grades 3-5', 'grade_level_Grades 6-8',
       'grade_level_Grades 9-12', 'grade_level_Grades PreK-2',
       'grade_level_nan']

    # validation dates we want to loop over
    validation_dates = ['2012-07-01', '2013-01-01', '2013-07-01']

    # models_to_run=['RF','DT','KNN', 'ET', 'AB', 'GB', 'LR', 'NB']
    if (model == 'all'):
        models_to_run=['RF','LR','DT', 'KNN']
    else:
        models_to_run = []
        models_to_run.append(model)

    clfs, grid = define_clfs_params(grid_size)

    # which feature/predictor sets do we want to use in our analysis
    predictor_sets = [selected_features]

    # generate all possible subsets of the feature/predictor groups
    predictor_subsets = get_subsets(predictor_sets)

    all_predictors=[]
    for p in predictor_subsets:
        merged = list(itertools.chain.from_iterable(p))
        all_predictors.append(merged)

    # write header for the csv
    with open(outfile, "w") as myfile:
        myfile.write("model_type ,clf, parameters, outcome, validation_date, group,train_set_size, validation_set_size,predictors,baseline,precision_at_5,precision_at_10,precision_at_20,precision_at_30,precision_at_40,precision_at_50,recall_at_5,recall_at_10,recall_at_20,recall_at_30,recall_at_40, ecall_at_50,auc-roc")

    # define dfframe to write results to
    results_df =  pd.DataFrame(columns=('model_type','clf', 'parameters', 'outcome', 
                                        'validation_date', 'group',
                                        'train_set_size', 'validation_set_size',
                                        'predictors', 'baseline','precision_at_5',
                                        'precision_at_10','precision_at_20',
                                        'precision_at_30','precision_at_40',
                                        'precision_at_50','recall_at_5',
                                        'recall_at_10','recall_at_20','recall_at_30',
                                        'recall_at_40', 'recall_at_50','auc-roc'))

    # the magic loop starts here
    # we will loop over models, parameters, outcomes, validation_Dates
    # and store several evaluation metrics
    group = 0
    for index,clf in enumerate([clfs[x] for x in models_to_run]):
        print('-------------------starting a new model=---------------')
        group += 1
        parameter_values = grid[models_to_run[index]]
        for p in ParameterGrid(parameter_values):
            print('-----current p ', p)
            for current_outcome in outcomes:
                for predictor in all_predictors:
                    print('---------predictor', predictor)
                    for validation_date in validation_dates:
                        print('---------validationdate', validation_date)
                        try:
                            print(models_to_run[index])
                            clf.set_params(**p)

                            train_set = df[df[timestamp_prediction_time] <= \
                                        datetime.strptime(validation_date, '%Y-%m-%d') \
                                        - timedelta(days=prediction_length)]
                            # fill in missing values for train set using just the train set
                            # we'll do it a very naive way here but you should think more carefully about this first
                            train_set.fillna(train_set.mean(), inplace=True)
                            train_set.dropna(axis=1, how='any', inplace=True)
                            
                            validation_set = df[df[timestamp_prediction_time] > datetime.strptime(validation_date, '%Y-%m-%d') - timedelta(days=0)]
                            # fill in missing values for validation set using all the df
                            # we'll do it a very naive way here but you should think more carefully about this first
                            validation_set.fillna(df.mean(), inplace=True)
                            validation_set.dropna(axis=1, how='any', inplace=True)

                            # get predictors by removing those dropped by dropna
                            predictors_to_use = list(set(predictor).intersection(train_set.columns))

                            model = clf.fit(train_set[predictor], train_set[current_outcome]) 
                            pred_probs = clf.predict_proba(validation_set[predictor])[::,1]

                            #pred_probs_sorted, true_outcome_sorted = zip(*sorted(zip(pred_probs, validation_set[current_outcome]), reverse=True))
                            results_df.loc[len(results_df)] = [models_to_run[index],clf, p, current_outcome, validation_date, group,
                                                               len(train_set),len(validation_set), 
                                                               predictor, 
                                                                precision_at_k(validation_set[current_outcome],pred_probs, 100),
                                                                precision_at_k(validation_set[current_outcome],pred_probs, 5),
                                                                precision_at_k(validation_set[current_outcome],pred_probs, 10),
                                                                precision_at_k(validation_set[current_outcome],pred_probs, 20),
                                                                precision_at_k(validation_set[current_outcome],pred_probs, 30),
                                                                precision_at_k(validation_set[current_outcome],pred_probs, 40),
                                                                precision_at_k(validation_set[current_outcome],pred_probs, 50),
                                                                recall_at_k(validation_set[current_outcome],pred_probs, 5),
                                                                recall_at_k(validation_set[current_outcome],pred_probs, 10),
                                                                recall_at_k(validation_set[current_outcome],pred_probs, 20),
                                                                recall_at_k(validation_set[current_outcome],pred_probs, 30),
                                                                recall_at_k(validation_set[current_outcome],pred_probs, 40),
                                                                recall_at_k(validation_set[current_outcome],pred_probs, 50),
                                                                roc_auc_score(validation_set[current_outcome], pred_probs)]

                            # plot precision recall graph
                            # we'll show them here but you can also save them to disk
                            plot_precision_recall_n(validation_set[current_outcome], pred_probs, clf, 'show')
                            # write results to csv as they come in so we always have something to see even if models runs for days
                            with open(outfile, "a") as myfile:
                                csvwriter = csv.writer(myfile, dialect='excel', quoting=csv.QUOTE_ALL)
                                strp = str(p)
                                strp.replace('\n', '')
                                strclf = str(clf)
                                strclf.replace('\n', '')
                                csvwriter.writerow([models_to_run[index],strclf, strp, current_outcome, validation_date, group,len(train_set),len(validation_set), predictor,  precision_at_k(validation_set[current_outcome],pred_probs, 100), precision_at_k(validation_set[current_outcome],pred_probs, 5), precision_at_k(validation_set[current_outcome],pred_probs, 10), precision_at_k(validation_set[current_outcome],pred_probs, 20), precision_at_k(validation_set[current_outcome],pred_probs, 30), precision_at_k(validation_set[current_outcome],pred_probs, 40), precision_at_k(validation_set[current_outcome],pred_probs, 50), recall_at_k(validation_set[current_outcome],pred_probs, 5), recall_at_k(validation_set[current_outcome],pred_probs, 10), recall_at_k(validation_set[current_outcome],pred_probs, 20), recall_at_k(validation_set[current_outcome],pred_probs, 30), recall_at_k(validation_set[current_outcome],pred_probs, 40), recall_at_k(validation_set[current_outcome],pred_probs, 50),roc_auc_score(validation_set[current_outcome], pred_probs)])
                        except IndexError:
                            print('Error:',e)
                            continue

    # write final dfframe to csv
    dfoutfile = 'df_' + outfile
    results_df.to_csv(dfoutfile, index=False)


if __name__ == '__main__':
    main()