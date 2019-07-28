#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def straightify(values):
    returnval = []
    for num in values:    
            returnval.append(1000/num)
    return returnval        


# In[3]:


data = pd.read_excel("/home/karthik/Cauvery Study/dataset-whole-rainfall-modified.xlsx")
X1 = data.iloc[:,[0,1,2,3,4]].values
X2 = data.iloc[:,[10]].values
y = data.iloc[:,[9]].values 


# In[4]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = 0 , strategy = 'median')
imputer = imputer.fit(X1[:,:])
X1[:,:] = imputer.transform(X1[:,:])


# In[5]:


for i in range(5):    
    X1[:,i] = straightify(X1[:,i])


# In[6]:


from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(X1,y)
regressor2 = LinearRegression()
regressor2.fit(X2,y)


# In[7]:


from ipywidgets import interactive, interact, fixed


# In[8]:
'''

def getvalues(Bathing = 15, 
              Cooking = 8, 
              Washing = 15, 
              Watering_plants = 10, 
              Rearing_animals = 2, 
              #Rainfall_max = 100,
              #Rainfall_total = 2000,
              Groundwater_last5 = 50
             ):
    predict_values1 =[ Bathing, 
                      Cooking, 
                      Washing, 
                      Watering_plants, 
                      Rearing_animals, 
                      #Rainfall_max,
                      #Rainfall_total,
                      #Groundwater_last5
                    ]
    predict_values1 = straightify(predict_values1)
    predict_values1 = np.array(predict_values1)
    predict_values1 = predict_values1.reshape(1,-1)
    predict_values2 = Groundwater_last5
    predict_values2 = np.array(predict_values2)
    predict_values2 = predict_values2.reshape(1,-1)
    y_pred1 = regressor1.predict(predict_values1).astype(int)
    y_pred2 = regressor2.predict(predict_values2).astype(int)
    print(f"Groundwater for present year will be {y_pred1[0][0]},{y_pred2[0][0]} metres below")


# In[9]:


X1 = interact(getvalues,
                 Bathing = (0,50,1), 
                 Cooking = (0,70,1), 
                 Washing = (0,80,1), 
                 Watering_plants = (0,230,1), 
                 Rearing_animals = (0,100,1), 
                 #Rainfall_max = (0,327,1),
                 #Rainfall_total = (0,6680,10), 
                 Groundwater_last5 = (0,160,1)
             )
display(X1)

'''
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




