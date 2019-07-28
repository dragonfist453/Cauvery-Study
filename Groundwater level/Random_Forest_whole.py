import pandas as pd
import numpy as np

file = open("Predicted_Random_Forest_whole.txt","w+")
Sl = 0.05
data = pd.read_excel("/home/karthik/Cauvery Study/dataset_whole.xlsx")
X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.05,random_state=0)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000)
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test).astype(int)

file.write(np.array2string(y_test)+"\n"+np.array2string(y_pred))
file.close()