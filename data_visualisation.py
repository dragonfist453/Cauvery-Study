import seaborn as sns
import pandas as pd

data = pd.read_excel("dataset.xlsx")
sns.set()
sns.relplot(x='Log_last10',y='Log_last5',kind='line',data=data);
