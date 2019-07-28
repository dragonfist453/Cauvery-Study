import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = open("2019_backward_values.txt","w+")
data = pd.read_excel("/home/karthik/Cauvery Study/dataset_whole.xlsx")
X = data.iloc[:,[0,1,2,3,4,6]].values
y = data.iloc[:,5].values

X1 = data.iloc[:,[0,1,2,3,4,5]].values
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.01,random_state=0)

X2 = np.append(arr = np.ones((150,1)).astype(int), values = X, axis = 1)
X2 = X2[:,[6]]
import statsmodels.formula.api as sm 
regressor_OLS = sm.OLS(y,X2).fit()
X_real = X1[:,-1]
y_back = regressor_OLS.predict(X_real).astype(int)

file.write(f"Last 10 years = {np.array(X[:,-1].mean())} \nLast 5 years : {y.mean()}\nNext 5 years: {y_back.mean()}\n")
'''plt.scatter(X_real,y,color='red')
plt.plot(X_real,regressor_OLS.predict(X_real),color='blue')'''

file.write(np.array2string(y)+"\n"+np.array2string(y_back))
file.close()