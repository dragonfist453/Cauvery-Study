import pandas as pd
import numpy as np

data = pd.read_excel("/home/karthik/Cauvery Study/dataset_rainfall_whole.xlsx")
X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values
 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 0 , strategy = 'most_frequent', axis = 0)
imputer = imputer.fit(X[:,[5,6]])
X[:,[5,6]] = imputer.transform(X[:,[5,6]])

X1 = data.iloc[:,[0,1,2,3,4,5,6,8]]
#imputer = imputer.fit(y[:,0:1])
#y[:,0:1] = imputer.transform(y[:,0:1])

#from sklearn.model_selection import train_test_split
#X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.1)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10)
regressor.fit(X,y)

from tkinter import *
master = Tk()


y_pred = regressor.predict(X1).astype(int) 

print(y_pred)
