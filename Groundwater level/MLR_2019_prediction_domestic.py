import pandas as pd
import numpy as np

file = open("2019_values_domestic.txt","w+")
for i in range(15):
    data = pd.read_excel("/home/karthik/Cauvery Study/dataset-domestic.xlsx",i)
    X = data.iloc[:,[0,1,2,3,4,5]].values
    y = data.iloc[:,6].values
    
    X1 = data.iloc[:,[0,1,2,3,4,6]].values
    #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1,random_state=0)
    
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X,y)
    
    y_pred = regressor.predict(X1).astype(int)
    
    
    file.write(str(i+1)+"\t"+np.array2string(y)+"\t"+np.array2string(y_pred)+"\n")
file.close()