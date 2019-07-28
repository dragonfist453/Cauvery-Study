import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

file = open("2019_Random_Forest_values.txt","w+")
data = pd.read_excel("/home/karthik/Cauvery Study/dataset_whole.xlsx")
X = data.iloc[:,[0,1,2,3,4,6]].values
y = data.iloc[:,5].values

X1 = data.iloc[:,[0,1,2,3,4,5]].values
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.01,random_state=0)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100)
regressor.fit(X,y)

from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(regressor,X,y,cv=10)

y_pred = regressor.predict(X1).astype(int)
file.write(f"Last 10 years : {np.array(X[:,-1].mean())} \nLast 5 years : {y.mean()}\nNext 5 years: {y_pred.mean()}\n")
file.write(f"Accuracy of data : {accuracy.mean()}\nStandard deviation : {accuracy.std()}\n")
file.write(np.array2string(y)+"\n"+np.array2string(y_pred))

'''plt.scatter(data.iloc[:,6],y,color='blue')
plt.plot(data.iloc[:,5],y_pred,color='red')'''
file.close()