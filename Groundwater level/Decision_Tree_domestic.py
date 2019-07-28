import pandas as pd
import numpy as np

file = open("Predicted_Decision_Tree_domestic.txt","w+")
for i in range(15):
    data = pd.read_excel("/home/karthik/Cauvery Study/dataset-domestic.xlsx",i)
    X = data.iloc[:,:-1].values
    y = data.iloc[:,-1].values
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1,random_state=0)
    
    from sklearn.tree import DecisionTreeRegressor
    regressor = DecisionTreeRegressor()
    regressor.fit(X_train,y_train)
    
    y_pred = regressor.predict(X_test).astype(int)
    
    
    file.write(str(i+1)+"\t"+np.array2string(y_pred)+"\t"+np.array2string(y_test)+"\n")
file.close()