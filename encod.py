# importing libraries 
import numpy as np 
import pandas as pd

# importing the required data 
data = pd.read_csv("grocery.csv")
print(data) 

# label encoding the data 
from sklearn.preprocessing import LabelEncoder 

le = LabelEncoder() 

data['Item']= le.fit_transform(data['Item']) 
print(data)

# importing one hot encoder from sklearn 
from sklearn.preprocessing import OneHotEncoder 
ohe = OneHotEncoder() 

# one hot encoding the data
from sklearn.compose import ColumnTransformer 
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough') 
datum = np.array(columnTransformer.fit_transform(data).toarray()) 
datum = pd.DataFrame(datum)
print(datum)

data = ohe.fit_transform(data).toarray()
data = pd.DataFrame(data)
print(data)