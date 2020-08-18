import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

flavors = whisky.iloc[:, 2:14]
corr_flavor = pd.DataFrame.corr(flavors)
corr_whisky = pd.DataFrame.corr(flavors.transpose())

plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)     # or corr_flavors
plt.axis("tight")
plt.colorbar()
#plt.show()

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
print(np.sum(model.rows_, axis=1))

whisky["group"] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)

