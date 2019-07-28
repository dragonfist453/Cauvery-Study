import pandas as pd
import numpy as np

file = open("2019_Random_Forest_values_domestic.txt","w+")
for i in range(15):
    data = pd.read_excel("/home/karthik/Cauvery Study/dataset-domestic.xlsx",i)
    X = data.iloc[:,[0,1,2,3,4,5]].values
    y = data.iloc[:,-1].values
    y = y.reshape(-1,1)
    X1 = data.iloc[:,[0,1,2,3,4,6]].values
    #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1,random_state=0)
    

   
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(1000)
    regressor.fit(X,y)
    
    y_pred = regressor.predict(X1).astype(int)
    y = y.reshape(1,-1)
    print(f"Village : {i}\ny = {y.mean()} \ny_pred : {y_pred.mean()}")
    file.write(str(i+1)+"\t"+np.array2string(y)+"\t"+np.array2string(y_pred)+"\n")
file.close()