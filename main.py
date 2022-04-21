import pandas as pd
import numpy as np

# read scv+making dataFrame
url = "dataset.csv"
df = pd.read_csv(url, skiprows=2)

df.columns = ['Тиждень', 'Python: (Україна)', 'Java: (Україна)']

py = df['Python: (Україна)']
java = df['Java: (Україна)']

# t1
print(df.describe())

# t2
sortedData = df.sort_values(by=[df.columns[1]], ascending=False).iloc[:5, :2]
print(sortedData)

# t3
print(df.corr())

# t4
df_avg = pd.concat([py.rolling(12).mean(), java.rolling(12).mean()], axis=1)
df_detrend = df[['Python: (Україна)', 'Java: (Україна)']] - df_avg
print(df_detrend.corr())

# t5


# t6
# last_five = df.tail(5)
last_five = df.iloc[-5:]
print(last_five)

# t7
sortedData_Java = df.sort_values(by=[df.columns[2]]).iloc[:5]
print(sortedData_Java)
