import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
 
file = open("2019_backward_values_domestic.txt","w+")
for i in range(15):
    data = pd.read_excel("/home/karthik/Cauvery Study/dataset-domestic.xlsx",i)
    X = data.iloc[:,[0,1,2,3,4,5]].values
    y = data.iloc[:,6].values
    
    X1 = data.iloc[:,[0,1,2,3,4,6]].values
    col = len(X1[:])
    #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1,random_state=0)
    
    X2 = np.append(arr = np.ones((col,1)).astype(int), values = X, axis = 1)
    X2 = X2[:,[6]]

    regressor_OLS = sm.OLS(y,X2).fit()
    X_real = X1[:,-1]
    y_back = regressor_OLS.predict(X_real).astype(int)
        
    
    file.write(str(i+1)+"\t"+np.array2string(y)+"\t"+np.array2string(y_back)+"\n")
file.close()