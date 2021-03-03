# To re-download the data use command: kaggle competitions download -c facial-keypoints-detection
# Must have kaggle api installed: https://www.kaggle.com/docs/api

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

with open('training.csv') as csvfile:    
    data = pd.read_csv(csvfile, delimiter = ',')

labels = data.columns

for i in range(0,len(labels)-1,2):
    data.plot.scatter(x=labels[i], y=labels[i+1])

plt.show()
