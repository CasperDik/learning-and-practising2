# https://bitbucket.org/scisports/ssda-how-to-expected-goals/src/master/notebooks/how-to-expected-goals.ipynb?viewer=nbviewer

import os
import sys
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import average_precision_score
from sklearn.metrics import roc_auc_score

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# Import scikit-plot functions
#from scikitplot.metrics import plot_roc_curve
#from scikitplot.metrics import plot_precision_recall_curve
#from scikitplot.metrics import plot_calibration_curve

# Import SciPy function
from scipy.spatial import distance

path_dataset = os.path.abspath(os.path.join(os.sep, os.getcwd(), os.pardir, 'data', 'scisports-shots.parquet'))
df_dataset = pd.read_parquet(path_dataset)
