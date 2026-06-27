# from sklearn.preprocessing import LabelEncoder
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

#* TO BRING THE DATASET BETWEEN 0 AND 1, SO THAT LARGER VALUES DONT DOMINATE THE LEARNING MODEL

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

# from sklearn.tree import DecisionTreeClassifier

# X = [[1], [2], [3], [5], [6], [7]]

# Y = [0, 0, 0, 1, 1, 1]

# model = DecisionTreeClassifier()

# model.fit(X, Y)

# prediction = model.predict([[4]])

# print(prediction)

# '''CLASSIFICATION METRICES'''

# '''

# Classification metrics are used to evaluate machine learning models that predict categories (classes) rather than continuous numerical values.

# Examples:

# Yes / No
# Spam / Not Spam
# Cat / Dog
# Pass / Fail
# Fraud / Not Fraud
# Disease / No Disease

# classification matrices - recall, accuracy, f1_score, precision and confusion_matrix

# '''

# # from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# # y_true = [0, 1, 1, 0, 1, 0, 1]
# # y_pred = [0, 1, 0, 0, 0, 1, 1]

# # accuracy = accuracy_score(y_true , y_pred)
# # precision = precision_score(y_true, y_pred)
# # recall = recall_score(y_true , y_pred)
# # f1score = f1_score(y_true , y_pred)

# # print('accuracy :' , accuracy )

# # print('precision :' , precision )

# # print('recall :' , recall )

# # print('f1_score :' , f1score )

# '''CONFUSION MATRIX'''

# # from sklearn.metrics import confusion_matrix

# # y_true = [1, 1, 0, 0, 1, 0]
# # y_pred = [1, 0, 0, 0, 1, 1]

# # cm = confusion_matrix(y_true , y_pred)
# # print(cm)

# # #  RESULT - TN FP
# # #             FN TP


# '''REGRESSION METRICES'''

# '''

# Regression metrices are used when we are dealing with numerical predictions, such as - house price, student marks etc...

# Regression matrix - MAE , MSE , RMSE , R square

# '''
# # from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

# # y_true = [10, 20, 30, 40]

# # y_pred = [12, 18, 35, 38]

# # mae = mean_absolute_error(y_true, y_pred)   
# # mse = mean_squared_error(y_true, y_pred) 
# # rmse = root_mean_squared_error(y_true, y_pred)
# # rsquare = r2_score(y_true, y_pred)

# # print('mae :' , mae)
# # print('mse :' , mse)
# # print('rmse :' , rmse)
# # print('rsquare :' , rsquare)

# '''PRACTICE KNN DECISION TREES AND FEATURE SCALING'''

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.preprocessing import MinMaxScaler, StandardScaler

# #* FEATURE SCALING
 
# data = {
#     'Age': [20, 25, 30, 35, 40 , 45 , 50, 55, 60 , 65],
#     'Salary': [20000, 30000, 50000, 70000, 90000 , 100000 , 120000, 130000 , 140000 , 160000]
# }   
# df = pd.DataFrame(data)

# x = df[['Age' , 'Salary']]


# scaler = StandardScaler()
# # scaled_x = scaler.fit_transform(x)
# # print(scaled_x)

# #* K NEAREST NEIGHBORS

# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error , r2_score

# knn = KNeighborsRegressor(n_neighbors = 3)

# x = df[['Age']]
# y = df['Salary']

# x_train , x_test , y_train , y_test = train_test_split(
#     x,y,
#     test_size = 0.2,
#     random_state = 42
# )

# x_scaled = scaler.fit_transform(x_train)
# x_test_scaled = scaler.transform(x_test)

# knn.fit(x_scaled , y_train)

# y_pred = knn.predict(x_test_scaled)

# print(r2_score(y_test , y_pred))

'''RANDOM FOREST'''

'''
COLLECTION OF MANY DECISION TREES WHICH USE A RANDOM SUBSET OF DATA TO MAKE PREDICTIONS
CALSSIFICATION IS DONE BY VOTING SYSTEM 
REGRESSION IS DONE BY TAKING THE AVERAGE

RANDOM FOREST WORKS BETTER WHEN TRAINING SAMPLE IS VERY HIGH 

NO SCALING REQUIRED 
HIGH ACCURACY
LESS CHANCES OF OVERFITTING 
CAN WORK WITH LARGE DATASET
CAN HANDLE CLASSIFICATION AND REGRESSION

USES MORE MEMORY
USUALLY SLOWER THAN DECISION TREES

'''
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# data = {
#     'Age': [22, 25, 47, 52, 46],
#     'Salary': [25000, 32000, 48000, 52000, 50000],
#     'Purchased': [0, 1, 1, 0, 1]
# }

# df = pd.DataFrame(data)
# x = df[['Age']]
# y = df['Salary']

# x_train , x_test , y_train , y_test  = train_test_split(
#     x , y , 
#     test_size = 0.2,
#     random_state = 42
# )
# model_1 = RandomForestRegressor(n_estimators = 100 , random_state = 42)

# model_1.fit(x_train , y_train)
# y_pred = model_1.predict([[32]])
# print(y_pred)

