# -*- coding: utf-8 -*-
"""307DBSCAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wesAUODTosN-MWjyzc_nhPLdRG9qxALC

This training material is developed by Dr. Yang Song at UNC Wilmington.

This work is supported by NSF #2230046. You can use this material for non-commercial purposes. But please retain proper attribution by keeping this content.

### Assume that Dr. Yang Song is a poor phd student, and he cannot say no to his advisor...

Dr. Song has a clutering problem to solve, and he sampled 20% of the data for testing purpuse. He has build the model below with `t4.8k_sample.csv`.

Full dataset is [here](https://drive.google.com/file/d/1Te8tCSFKzSVSTJmVtZEMr8m0CPdeZewo/view?usp=sharing) and the sampled dataset is [here](https://drive.google.com/file/d/11WQT9PUmmJ_af2CS8UOYFaC1AVGxqFy5/view?usp=sharing).

Below is his finished code, and you don't need to make any changes.
"""

#from google.colab import drive
#drive.mount('/content/drive')

import pandas as pd
import numpy as np

# The datafile in google drive root/Colab Notebooks/data/t4.8k_sample.txt
# for the full data, we can read it like below -
df = pd.read_csv("data/t4.8k.txt", sep=" ", names=['x','y'])
#df = pd.read_csv('data/t4.8k_sample.csv')
df.head()

df.shape

from sklearn.cluster import DBSCAN
# This is a model Dr. Song tuned with the sampled model.
db = DBSCAN(eps=15, min_samples=15, metric='euclidean')
labels = db.fit_predict(df)

df["cluster_lables"] = labels
df.head(2)

df.cluster_lables.value_counts()

# On HPC, this line should be changed, too!
df.to_csv("/content/drive/My Drive/Colab Notebooks/data/t4.8k_output.csv")
