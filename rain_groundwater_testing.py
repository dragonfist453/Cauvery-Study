import pandas as pd
import numpy as np

data = pd.read_excel("/home/karthik/Cauvery Study/dataset-whole-rainfall-modified.xlsx")
X = data.iloc[:,[0,1,2,3,4,7,10]].values
y = data.iloc[:,9].values

''' 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 0 , strategy = 'most_frequent', axis = 0)
imputer = imputer.fit(X[:,[5,6]])
X[:,[5,6]] = imputer.transform(X[:,[5,6]])
#imputer = imputer.fit(y[:,0:1])
#y[:,0:1] = imputer.transform(y[:,0:1])
'''

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.01)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
regressor = Sequential()

# Adding the input layer and the first hidden layer
regressor.add(Dense(output_dim = 5, init = 'uniform', activation = 'relu', input_dim = 4))

# Adding the second hidden layer
regressor.add(Dense(output_dim = 3, init = 'uniform', activation = 'relu'))

# Adding the output layer
regressor.add(Dense(output_dim = 1, init = 'uniform', activation = 'relu'))

# Compiling the ANN
regressor.compile(optimizer = 'adam', loss = 'MSE')

# Fitting the ANN to the Training set
#regressor.fit(X_train, y_train, batch_size = 1, nb_epoch = 100)

#y_pred = regressor.predict(X_test).astype(int) 