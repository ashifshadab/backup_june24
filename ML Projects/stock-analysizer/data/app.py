import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sb
  
import warnings 
warnings.filterwarnings("ignore") 


df = pd.read_csv('./26-05-2023-TO-26-05-2024-NIFTY1-ALL-N.csv') 
print(df.head(5))

plt.figure(figsize=(15,5)) 
plt.plot(df['Close']) 
plt.title('KOTAKNIFTY Close price.', fontsize=15) 
plt.ylabel('Price in RS.') 
plt.show()

features = ['Open', 'High', 'Low', 'Close', 'Volume'] 
  
plt.subplots(figsize=(20,10)) 
  
for i, col in enumerate(features): 
  plt.subplot(2,3,i+1) 
  sb.distplot(df[col]) 
plt.show()

plt.subplots(figsize=(20,10)) 
for i, col in enumerate(features): 
  plt.subplot(2,3,i+1) 
  sb.boxplot(df[col]) 
plt.show()

splitted = df['Date'].str.split('-', expand=True) 
  
df['day'] = splitted[1].astype('int') 
df['month'] = splitted[0].astype('int') 
df['year'] = splitted[2].astype('int') 
  
df.head()

df['is_quarter_end'] = np.where(df['month']%3==0,1,0) 
df.head()

data_grouped = df.groupby('year').mean() 
plt.subplots(figsize=(20,10)) 
  
for i, col in enumerate(['Open', 'High', 'Low', 'Close']): 
  plt.subplot(2,2,i+1) 
  data_grouped[col].plot.bar() 
plt.show()

df.groupby('is_quarter_end').mean()

df['open-close']  = df['Open'] - df['Close'] 
df['low-high']  = df['Low'] - df['High'] 
df['target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

plt.pie(df['target'].value_counts().values,  
        labels=[0, 1], autopct='%1.1f%%') 
plt.show()

plt.figure(figsize=(10, 10)) 
  
# As our concern is with the highly 
# correlated features only so, we will visualize 
# our heatmap as per that criteria only. 
sb.heatmap(df.corr() > 0.9, annot=True, cbar=False) 
plt.show() 

