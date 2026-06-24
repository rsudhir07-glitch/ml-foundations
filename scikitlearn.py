# from sklearn.preprocessing import LabelEncoderCity
# from sklearn.preprocessing import OneHotEncoder
# import pandas as pd

# df = pd.DataFrame({
#     'places': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai']
# })

'''ENCODING'''

# dummy = pd.get_dummies(df['places'])
# print(dummy) #* THIS WILL GIVE BOOLEAN ENCODED VALUES OF PLACES IN COLUMN 

# dummy = pd.get_dummies(df['places'], dtype = int)
# print(dummy) #* THIS WILL CHANGE THE BOOLEAN VALUES INTO Os AND 1s

# encoder = OneHotEncoder(sparse_output=False)
# df['encodedvalues'] = encoder.fit_transform(df[['places']])
# print(df)

''' FEATURE SCALING'''

'''MIN MAX SCALING'''

# from sklearn.preprocessing import MinMaxScaler
# import pandas as pd

# ages = [18, 22, 30, 40] #* THIS IS A 1D ARRAY
# df = pd.DataFrame(ages) #* NOW IT IS CONVERTED INTO A DATAFRAME WITH A ROW AND COLUMN, WHICH MEANS ITS NOW A 2D ARRAY, BECAUSE MINMAXSCALER WORKS ONLY ON 2D ARRAYS

# scaler = MinMaxScaler()
# scaled_data =  scaler.fit_transform(df)
# # print(pd.DataFrame(scaled_data, columns = ['ages'])) #* HERE WE ARE CONVERTING THE SCALED DATA INTO A DATAFRAME AND GIVING NAME TO THE COLUMN AS AGE

''''''
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

# data = {
#     'AGE' : [20,25,30,35],
#     'SALARY' : [25000,40000,55000,70000]
# }

# df = pd.DataFrame(data)
# scaler = MinMaxScaler()

# scaled = scaler.fit_transform(df)
# framed = pd.DataFrame(scaled , columns = df.columns)
# print(framed )
# print(framed.shape)
# print(framed.max())
# print(framed.min())

'''STANDARDIZATION'''

# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# data = {
#     'AGE' : [20,25,30,35],
#      'SALARY' : [25000,40000,55000,70000]
# }
# df = pd.DataFrame(data)
# scaler = StandardScaler()
# scaled = scaler.fit_transform(df)
# print(pd.DataFrame(scaled , columns= df.columns))

'''TRAIN TEST SPLIT'''

# from sklearn.model_selection import train_test_split
# import pandas as pd

# data = {
#     'Age': [22, 25, 47, 52, 46],
#     'Salary': [25000, 32000, 48000, 52000, 50000],
#     'Purchased': [0, 1, 1, 0, 1]
# }

# df = pd.DataFrame(data)

# X = df[['Age', 'Salary']] #* X IS WHAT WE USE TO MAKE THE PREDICTION WHICH ARE CALLED FEATURES

# y = df['Purchased'] #* Y IS WHAT WE WANT THE MODEL TO PREDICT

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# print( y_test)  

''''''
# import pandas as pd
# from sklearn.model_selection import train_test_split


# data = {
#     'Age': [20, 25, 30, 35, 40, 45],
#     'Salary': [25000, 30000, 40000, 50000, 60000, 70000],
#     'Purchased': [0, 0, 1, 1, 1, 0]
# }
# df = pd.DataFrame(data)
# x = df[['Age' , 'Salary']]
# y = df['Purchased']

# x_train, x_test , y_train , y_test = train_test_split(
#     x,y,
#     test_size=0.33,
#     random_state=42
# )

# print(x_train)
# print()
# print(x_test)
# print()
# print(y_train)
# print()
# print(y_test)

'''REGRESSION'''

'''LINEAR REGRESSION'''

# import pandas as pd
# from sklearn.linear_model import LinearRegression

# data =  {
#     'x' : [1,2,3,4],
#     'y' :  [8,11,14,17]
# }

# df = pd.DataFrame(data)
# x = df[['x']] #* WE WANT THE FEATURE/INPUT IN THE FORM OF A 2D ARRAY
# y = df['y']

# model = LinearRegression()
# train = model.fit(x,y)
# prediction = model.predict([[5]])  

# print(prediction)   

'''K N N '''

#* PREDICTION IS BASED ON NEIGHBORS
#* 0 MEANS FALSE AND 1 MEANS TRUE
   
# from sklearn.neighbors import KNeighborsClassifier

# X = [[1], [2], [3], [8], [9], [10]] 

# Y = [0, 0, 0, 1, 1, 1]

# model = KNeighborsClassifier(n_neighbors = 3) #* SEE FOR 3 NEIGHBORS
# model.fit(X,Y)
# prediction = model.predict([[7]])
# print(prediction)


'''LOGISTIC REGRESSION'''

# #* SAME AS LINEAR REGRESSION, BUT IT GIVES RESULTS IN THE FORM OF 0 OR 1 MEANING FALSE OR TRUE RESPECTIVELY

# from sklearn.linear_model import LogisticRegression

# X = [[1], [2], [3], [8], [9], [10]]
# Y = [0, 0, 0, 1, 1, 1]

# model = LogisticRegression()
# model.fit(X,Y)

# prediction = model.predict([[11]])[0] #* [0] GIVES THE INPUT VALUE ONLY, NOT A LIST 
# print(prediction)


'''DECISION TREES'''

from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [5], [6], [7]]

Y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, Y)

prediction = model.predict([[4]])

print(prediction)