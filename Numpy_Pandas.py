#importing libraries

import numpy as np
import pandas as pd
import seaborn as sns

label=['a','b','c']
data=[10,20,30]
arr=np.array(data)
my_dict={'a':1,'b':2,'c':3,'d':4}
type(my_dict)

#Pandas Series practice
pd.Series(data=data,index=label)
pd.Series(data)

pd.Series(data=data,index=label)
pd.Series(my_dict)
ser1=pd.Series([1,2,3,4],['IND','USA','JAR','PAK'])

ser2=pd.Series([5,6,7,8],['IND','KAR','AND','PAK'])
ser1+ser2

#Pandas DataFrame pracctice

#importing randn library

from numpy.random import randn

df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

df[['W','X']]

#Adding new coloumn with existing column addition (W+X)

df['New']=df['W']+df['X']
df

type(df['New'])
df.drop('New',axis=1)
df

# Removing the column permanently by using inplace

df.drop('New',axis=1,inplace=True)

df
df.loc['A']
df.loc[['A','B']]

#Removing the rows from DataFrame

df.drop('E')
df.drop('E',inplace=True)
df.shape

#We can select rows by using iloc methode through Numaric index

df.loc[['A','B']]
df.iloc[1]
df.iloc[1:3]
df.loc['B':'D']
df.iloc[1:3,1:3]
df.loc['B':'C','X':'Y']
df.loc['C','X']

df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

#DataFrame conditional logics

dff1=df[df>0]

df
df[df<0]
df[df['W']<0]
df['X']<0

df_ser=df[df['W']>0]
df[df['W']>0]['X']

# Selecting the data by using AND and OR operations
df[(df['W']>0) & (df['Y']<0)]
df[(df['X']<0) & (df['Y']<0)]
df[(df['X']<0) | (df['Y']<0)]


#reset index or adding index to existing column
df_state='CA KA LA MA NA'.split()
df['States']=df_state
df.reset_index()
df.set_index('States',inplace=True)
df.iloc[2]
df

#Multi indexing on dataFrame

outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index
hier_index=pd.MultiIndex.from_tuples(hier_index)
df=pd.DataFrame(randn(6,2),hier_index,['A','B'])
df.loc['G1'].loc[2]
df.loc['G2'].loc[2]

df.index.names=['Groups','Num']
df.xs(1,level='Num')
df

#Deling with Null values

d={'A':[1,2,np.nan],'B':[1,np.nan,np.nan],'C':[1,2,3]}
df=pd.DataFrame(d)
df.dropna()
df.dropna(thresh=2)























