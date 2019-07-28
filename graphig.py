import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def straightify(values):
    returnval = []
    for num in values:    
        returnval.append(1000/num)
    return returnval        

data = pd.read_excel("dataset-whole-rainfall.xlsx")
X = data.iloc[:,[12]].values
y = data.iloc[:,[9]].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = 0 , strategy = 'median')
imputer = imputer.fit(X[:,:])
X[:,:] = imputer.transform(X[:,:])

#X = straightify(X)

plt.scatter(X,y)
plt.show()


