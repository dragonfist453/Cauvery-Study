import pandas as pd
import openpyxl as xl

data = pd.DataFrame()
rows = 0
for i in range(15):
     data_to_import = pd.read_excel("/home/karthik/Cauvery Study/dataset-domestic-rainfall.xlsx",i)
     data = data.iloc[:,:]+data_to_import.iloc[rows:,:]
     rows = len(data_to_import[:])

data.to_excel("dataset-whole-rainfall.xlsx")
