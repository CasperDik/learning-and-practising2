#horrible layout of the codeK

import numpy as np, random, scipy.stats as ss
import pandas as pd

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

#ex1
data = pd.read_csv("HarvardX_wine.csv")
numeric_data = data.copy()
#ex2
numeric_data.rename(columns={'color':'is_red'}, inplace=True)

numeric_data["is_red"].replace("red", 1, inplace=True)
numeric_data["is_red"].replace("white", 0, inplace=True)

numeric_data.drop(["quality","high_quality"], axis=1, inplace=True)
#ex3
import sklearn.preprocessing as sk
scaled_data = sk.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns=numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)
#ex4
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages

observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0]
y = principal_components[:,1]

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

#ex5
import numpy as np
np.random.seed(1) # do not change

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)

def accuracy(predictions, outcomes):
    return np.mean(predictions == outcomes)*100

#ex6
print(accuracy(0, data["high_quality"]))

#ex7
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
library_predictions = knn.predict(numeric_data)
accuracy(library_predictions, data["high_quality"])

#ex8
n_rows = data.shape[0]
random.seed(123)
selection = random.sample(range(n_rows), 10)

#ex9
predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])
p = predictors[selection]

my_predictions = knn_predict(p, predictors[training_indices,:], outcomes[training_indices], k=5)
percentage = accuracy(my_predictions, data["high_quality"])
