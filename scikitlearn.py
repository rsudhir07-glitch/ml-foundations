# from sklearn.preprocessing import LabelEncoderCity
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.DataFrame({
    'places': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai']
})

'''ENCODING'''

# dummy = pd.get_dummies(df['places'])
# print(dummy) #* THIS WILL GIVE BOOLEAN ENCODED VALUES OF PLACES IN COLUMN 

# dummy = pd.get_dummies(df['places'], dtype = int)
# print(dummy) #* THIS WILL CHANGE THE BOOLEAN VALUES INTO Os AND 1s

# encoder = OneHotEncoder(sparse_output=False)
# df['encodedvalues'] = encoder.fit_transform(df[['places']])
# print(df)