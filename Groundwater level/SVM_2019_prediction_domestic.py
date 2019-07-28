import pandas as pd
import numpy as np

file = open("2019_SVM_values_domestic.txt","w+")
for i in range(15):
    data = pd.read_excel("/home/karthik/Cauvery Study/dataset-domestic.xlsx",i)
    X = data.iloc[:,[0,1,2,3,4,5]].values
    y = data.iloc[:,-1].values
    y = y.reshape(-1,1)
    X1 = data.iloc[:,[0,1,2,3,4,6]].values
    #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1,random_state=0)
    
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X = sc_X.fit_transform(X)
    y = sc_y.fit_transform(y)
   
    from sklearn.svm import SVR
    regressor = SVR()
    regressor.fit(X,y)
    
    y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array(X1)))).astype(int)
    y = sc_y.inverse_transform(y).astype(int)
    y = y.reshape(1,-1)
    file.write(str(i+1)+"\t"+np.array2string(y)+"\t"+np.array2string(y_pred)+"\n")
file.close()