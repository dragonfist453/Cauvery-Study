import raindata
import pandas as pd

for i in range(15):
    data = pd.read_excel("/home/karthik/Cauvery Study/Data Village-wise.xlsx",i)
    import_data = data.iloc[:,[10,11,12,17,18,19,32,33]]
