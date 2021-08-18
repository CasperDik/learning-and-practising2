""""
building different xG models with artificial data and data from Wyscout and Statsbomb
to begin used data and followed model from this tutorial:
https://bitbucket.org/scisports/ssda-how-to-expected-goals/src/master/notebooks/how-to-expected-goals.ipynb?viewer=nbviewer
"""

# learn plots and stats data tell sth about how good model is
# then learn about the model
# try different models
# use different data
# change file structure?

import os
import sys
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# Import scikit-plot functions
from scikitplot.metrics import plot_roc
from scikitplot.metrics import plot_calibration_curve
from scikitplot.metrics import plot_precision_recall
# Import SciPy function
from scipy.spatial import distance

# todo: try same but with different data
# https://github.com/andrewRowlinson/expected-goals-thesis
# statsbom: https://github.com/statsbomb/open-data
# Wyscout: https://figshare.com/collections/Soccer_match_event_dataset/4415000/2
# !different type of datafile(json) + (maybe) different stats collected!

path_dataset = os.path.abspath(os.path.join(os.sep, os.getcwd(), os.pardir, 'xG', 'scisports-shots.parquet'))
df_dataset = pd.read_parquet(path_dataset)

for action in ['action', 'action1', 'action2']:
    for side in ['start', 'end']:
        # Normalize the X location
        key_x = '{}_{}_x'.format(action, side)
        df_dataset[key_x] = df_dataset[key_x] / 105

        # Normalize the Y location
        key_y = '{}_{}_y'.format(action, side)
        df_dataset[key_y] = df_dataset[key_y] / 68

# opposing goal position
# since normalized--> in the middle thus 0.5, at the other end thus 1
goal = (1, 0.5)

# compute Eucledian distance from each action towards opponents goal
for action in ['action', 'action1', 'action2']:
    key_start_x = '{action}_start_x'.format(action=action)
    key_start_y = '{action}_start_y'.format(action=action)
    key_start_distance = '{action}_start_distance'.format(action=action)

    df_dataset[key_start_distance] = df_dataset.apply(lambda s: distance.euclidean((s[key_start_x], s[key_start_y]), goal), axis=1)

# change the dataset(X and y) and drop irrelevant columns
columns_features = ['action_start_x', 'action_start_y', 'action_body_part_id', 'action_start_distance', 'action1_start_distance', 'action2_start_distance', "action1_type_id", "action_seconds", "action_period", "action1_result", "action2_type_id", "action2_result",]
column_target = 'action_result'

X = df_dataset[columns_features]
y = df_dataset[column_target]

# split dataset in train and test (90/10)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.90)

# model 1
classifier = XGBClassifier(objective='binary:logistic', max_depth=5, n_estimators=100)
classifier.fit(X_train, y_train)
# todo: learn about XGB classifier --> revolutionairy in machine learning --> very good to know i guess
# todo: compare model with other models? --> Probit, logit, ML?

# For each shot, predict the probability of the shot resulting in a goal
y_pred = classifier.predict_proba(X_test)
# actual/observed total attempts
y_total = y_train.count()
# observed total goals
y_positive = y_train.sum()

print('The training set contains {} examples of which {} are positives.'.format(y_total, y_positive))

# AUC-ROC score
# todo: learn what all these outcomes mean and how to interpret
auc_roc = roc_auc_score(y_test, y_pred[:, 1])
print('Our classifier obtains an AUC-ROC of {}.'.format(auc_roc))

# AUC-PR
auc_pr_baseline = y_positive / y_total
print('The baseline performance for AUC-PR is {}.'.format(auc_pr_baseline))

auc_pr = average_precision_score(y_test, y_pred[:, 1])
print('Our classifier obtains an AUC-PR of {}.'.format(auc_pr))

# generate ROC curve
plot_roc(y_test, y_pred, plot_micro=False, plot_macro=False)
plt.show()
# Plot AUC-PR curve
plot_precision_recall(y_test, y_pred)
plt.show()
# plot calibration curve
plot_calibration_curve(y_test, [y_pred])
plt.show()

print("done")
