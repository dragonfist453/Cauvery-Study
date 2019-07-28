import pandas as pd
import numpy as np

file = open("2019_rainfall_crop_values.txt","w+")
data = pd.read_excel("/home/karthik/Cauvery Study/Crops_water_rain.xlsx")
X = data.iloc[:,:3].values
y = data.iloc[:,3].values

'''from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])'''

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test).astype(int)
'''
from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(regressor,X,y,cv=10)

y_pred = regressor.predict(X1).astype(int)

file.write(f"Last 10 years : {np.array(X[:,-1].mean())} \nLast 5 years : {y.mean()}\nNext 5 years: {y_pred.mean()}\n")
file.write(f"Accuracy of data : {accuracy.mean()}\nStandard deviation : {accuracy.std()}\n")
file.write(np.array2string(y)+"\n"+np.array2string(y_pred))
plt.scatter(data.iloc[:,6],y,color='blue')
plt.plot(data.iloc[:,5],y_pred,color='red')'''
file.close()

