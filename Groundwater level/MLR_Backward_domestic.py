import pandas as pd
import numpy as np
import statsmodels.formula.api as sm

file = open("Predicted_Backward_domestic.txt","w+")
Sl = 0.05
for m in range(15):
    data = pd.read_excel("/home/karthik/Cauvery Study/dataset-domestic.xlsx",m)
    X = data.iloc[:,:-1].values
    y = data.iloc[:,-1].values
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1)
    
    col_train = len(X_train[:])
    X2 = np.append(arr = np.ones((col_train,1)).astype(int), values = X_train, axis = 1)
    k=[0,1,2,3,4,5,6]
    X4 = X2[:,k]
    col_test = len(X_test[:])
    X3 = np.append(arr = np.ones((col_test,1)).astype(int), values = X_test, axis = 1)
   
    num = len(X_train[0])
    for i in range(0,num):
        regressor_OLS = sm.OLS(y_train,X4).fit()
        maxvar = max(regressor_OLS.pvalues.astype(float))
        if maxvar > Sl:
            for j in range(0,num-i):
                if regressor_OLS.pvalues[j].astype(float) == maxvar:
                    k.pop(j)
                    X4 = X2[:,k]
                    
    regressor_OLS = sm.OLS(y_train,X4).fit()    
    X_real = X3[:,k]
    y_back = regressor_OLS.predict(X_real).astype(int)
    
    
    file.write(str(m+1)+"\t"+np.array2string(y_back)+"\t"+np.array2string(y_test)+"\n")

file.close()