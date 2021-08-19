""""
building different xG models with artificial data and data from Wyscout and Statsbomb
to begin used data and followed model from this tutorial:
https://bitbucket.org/scisports/ssda-how-to-expected-goals/src/master/notebooks/how-to-expected-goals.ipynb?viewer=nbviewer
"""
import os
import pandas as pd


def data_transformations(data, test_size):
    from scipy.spatial import distance
    from sklearn.model_selection import train_test_split

    for action in ['action', 'action1', 'action2']:
        for side in ['start', 'end']:
            # Normalize the X location
            key_x = '{}_{}_x'.format(action, side)
            data[key_x] = data[key_x] / 105

            # Normalize the Y location
            key_y = '{}_{}_y'.format(action, side)
            data[key_y] = data[key_y] / 68

    # opposing goal position
    goal = (1, 0.5)

    # compute Eucledian distance from each action towards opponents goal
    for action in ['action', 'action1', 'action2']:
        key_start_x = '{action}_start_x'.format(action=action)
        key_start_y = '{action}_start_y'.format(action=action)
        key_start_distance = '{action}_start_distance'.format(action=action)

        data[key_start_distance] = data.apply(lambda s: distance.euclidean((s[key_start_x], s[key_start_y]), goal), axis=1)

    # change the dataset(X and y) and drop irrelevant columns
    columns_features = ['action_start_x', 'action_start_y', 'action_body_part_id', 'action_start_distance', 'action1_start_distance', 'action2_start_distance', "action1_type_id", "action_seconds", "action_period", "action1_result", "action2_type_id", "action2_result",]
    column_target = 'action_result'

    X = data[columns_features]
    y = data[column_target]

    # split dataset in train and test (90/10)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    return X_train, X_test, y_train, y_test


def XGBoost_manual(X_train, X_test, y_train, y_test, max_depth, n_estimators):
    from xgboost import XGBClassifier
    from sklearn.metrics import average_precision_score
    from sklearn.metrics import roc_auc_score
    import matplotlib.pyplot as plt
    # Import scikit-plot functions
    from scikitplot.metrics import plot_roc
    from scikitplot.metrics import plot_calibration_curve
    from scikitplot.metrics import plot_precision_recall

    classifier = XGBClassifier(objective='binary:logistic', max_depth=max_depth, n_estimators=n_estimators)
    classifier.fit(X_train, y_train)
    # For each shot, predict the probability of the shot resulting in a goal
    y_pred = classifier.predict_proba(X_test)

    y_total = y_train.count()           # actual/observed total attempts
    y_positive = y_train.sum()      # observed total goals
    print('The training set contains {} examples of which {} are positives.'.format(y_total, y_positive))

    # AUC-ROC score
    auc_roc = roc_auc_score(y_test, y_pred[:, 1])
    print('Our classifier obtains an AUC-ROC of {}.'.format(auc_roc))

    # AUC-PR
    auc_pr_baseline = y_positive / y_total
    print('The baseline performance for AUC-PR is {}.'.format(auc_pr_baseline))

    auc_pr = average_precision_score(y_test, y_pred[:, 1])
    print('Our classifier obtains an AUC-PR of {}.'.format(auc_pr))

    # generate ROC curve
    plot_roc(y_test, y_pred, plot_micro=False, plot_macro=False)
    # Plot AUC-PR curve
    plot_precision_recall(y_test, y_pred)
    # plot calibration curve
    plot_calibration_curve(y_test, [y_pred])
    plt.show()


def XGBoost_optimized(X_train, X_test, y_train, y_test):
    from xgboost import XGBClassifier
    from sklearn.metrics import average_precision_score
    from sklearn.metrics import roc_auc_score
    import matplotlib.pyplot as plt
    from sklearn.model_selection import GridSearchCV
    # Import scikit-plot functions
    from scikitplot.metrics import plot_roc
    from scikitplot.metrics import plot_calibration_curve
    from scikitplot.metrics import plot_precision_recall

    """We train an XGBoost classifier on our train set by performing a grid search over a set of reasonable
    hyperparameters to find the optimal hyperparameters for this task. We vary the maximum depths of the trees from
    3 to 6 and try learning 100, 500, and 1000 trees. We use the default three-fold cross-validation approach to find
    the best set of hyperparameters."""

    parameters = {
        'nthread': [4],
        'objective': ['binary:logistic'],
        'max_depth': [3, 4, 5, 6],
        'learning_rate': [0.01],
        'n_estimators': [100, 500, 1000],
        'seed': [42]
    }

    classifier = XGBClassifier()
    classifier = GridSearchCV(classifier, parameters, scoring='roc_auc', verbose=2)
    classifier.fit(X_train, y_train)

    # For each shot, predict the probability of the shot resulting in a goal
    y_pred = classifier.predict_proba(X_test)

    y_total = y_train.count()           # actual/observed total attempts
    y_positive = y_train.sum()      # observed total goals
    print('The training set contains {} examples of which {} are positives.'.format(y_total, y_positive))

    # AUC-ROC score
    auc_roc = roc_auc_score(y_test, y_pred[:, 1])
    print('Our classifier obtains an AUC-ROC of {}.'.format(auc_roc))

    # AUC-PR
    auc_pr_baseline = y_positive / y_total
    print('The baseline performance for AUC-PR is {}.'.format(auc_pr_baseline))

    auc_pr = average_precision_score(y_test, y_pred[:, 1])
    print('Our classifier obtains an AUC-PR of {}.'.format(auc_pr))

    # generate ROC curve
    plot_roc(y_test, y_pred, plot_micro=False, plot_macro=False)
    # Plot AUC-PR curve
    plot_precision_recall(y_test, y_pred)
    # plot calibration curve
    plot_calibration_curve(y_test, [y_pred])
    plt.show()


def Logit(X_train, X_test, y_train, y_test):
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import average_precision_score
    from sklearn.metrics import roc_auc_score
    import matplotlib.pyplot as plt
    from scikitplot.metrics import plot_roc
    from scikitplot.metrics import plot_calibration_curve
    from scikitplot.metrics import plot_precision_recall

    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train, y_train)

    # For each shot, predict the probability of the shot resulting in a goal
    y_pred = classifier.predict_proba(X_test)

    y_total = y_train.count()  # actual/observed total attempts
    y_positive = y_train.sum()  # observed total goals
    print('The training set contains {} examples of which {} are positives.'.format(y_total, y_positive))

    # AUC-ROC score
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


def Random_Forest(X_train, X_test, y_train, y_test):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import average_precision_score
    from sklearn.metrics import roc_auc_score
    import matplotlib.pyplot as plt
    from scikitplot.metrics import plot_roc
    from scikitplot.metrics import plot_calibration_curve
    from scikitplot.metrics import plot_precision_recall

    classifier = RandomForestClassifier(max_depth=5, random_state=0)
    classifier.fit(X_train, y_train)

    # For each shot, predict the probability of the shot resulting in a goal
    y_pred = classifier.predict_proba(X_test)

    y_total = y_train.count()  # actual/observed total attempts
    y_positive = y_train.sum()  # observed total goals
    print('The training set contains {} examples of which {} are positives.'.format(y_total, y_positive))

    # AUC-ROC score
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


def StandardGradientBoosting(X_train, X_test, y_train, y_test):
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.metrics import average_precision_score
    from sklearn.metrics import roc_auc_score
    import matplotlib.pyplot as plt
    from scikitplot.metrics import plot_roc
    from scikitplot.metrics import plot_calibration_curve
    from scikitplot.metrics import plot_precision_recall

    classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=0)
    classifier.fit(X_train, y_train)

    # For each shot, predict the probability of the shot resulting in a goal
    y_pred = classifier.predict_proba(X_test)

    y_total = y_train.count()  # actual/observed total attempts
    y_positive = y_train.sum()  # observed total goals
    print('The training set contains {} examples of which {} are positives.'.format(y_total, y_positive))

    # AUC-ROC score
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


def lightGBM(X_train, X_test, y_train, y_test):
    import lightgbm as lgb
    import numpy as np
    from sklearn.metrics import average_precision_score
    from sklearn.metrics import roc_auc_score
    import matplotlib.pyplot as plt
    from scikitplot.metrics import plot_roc
    from scikitplot.metrics import plot_calibration_curve
    from scikitplot.metrics import plot_precision_recall

    # todo: learn how to build lightGBM model
    # https://www.kaggle.com/ezietsman/simple-python-lightgbm-example
    pass


# todo: try same but with different data
# https://github.com/andrewRowlinson/expected-goals-thesis
# statsbom: https://github.com/statsbomb/open-data
# Wyscout: https://figshare.com/collections/Soccer_match_event_dataset/4415000/2

path_dataset = os.path.abspath(os.path.join(os.sep, os.getcwd(), os.pardir, 'xG', 'scisports-shots.parquet'))
data = pd.read_parquet(path_dataset)

# todo: learn about XGB classifier
# todo: learn about all models and how to optimize (hyper)parameters
X_train, X_test, y_train, y_test = data_transformations(data, 0.9)
# XGBoost(X_train, X_test, y_train, y_test, 5, 100)
# XGBoost_optimized(X_train, X_test, y_train, y_test)
Logit(X_train, X_test, y_train, y_test)
# Random_Forest(X_train, X_test, y_train, y_test)
# StandardGradientBoosting(X_train, X_test, y_train, y_test)
# lightGBM(X_train, X_test, y_train, y_test)

