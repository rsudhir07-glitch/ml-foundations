
''' SUPPORT VECTOR MACHINES - SVM'''

# import pandas as pd 
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC , SVR

'''

SVC - SUPPORT VECTOR CLASSIFIER

# '''
# data = {
#     'Age': [22, 25, 47, 52, 46],
#     'Purchased': [0, 1, 1, 0, 1]
# }

# df = pd.DataFrame(data)

# x = df[['Age']]
# y = df['Purchased']

# # splitting data into training and testing 
# x_train , x_test , y_train , y_test = train_test_split(
#     x, y , 
#     test_size = 0.2,
#     random_state = 42
# )

# # feature scaling 

# scaler = StandardScaler()
# x_train = scaler.fit_transform(x_train )
# x_test = scaler.transform(x_test)

# # svm 

# svm = SVC(kernel='linear') # creating the model 
# svm.fit(x_train , y_train ) # teaching the model

# new_input = scaler.transform([[44]]) # applying the same scaling to the new_input as the training data 

# prediction = svm.predict(new_input) 

# print(prediction)


'''SVR - SUPPORT VECTOR REGRESSOR'''


# data = {
#     'Age': [22, 25, 47, 52, 46],
#     'Salary': [25000, 32000, 48000, 52000, 50000]
# }

# df = pd.DataFrame(data)

# x = df[['Age']]
# y = df['Salary']


# # splitting data into training and testing 
# x_train , x_test , y_train , y_test = train_test_split(
#     x, y , 
#     test_size = 0.2,
#     random_state = 42
# )

# # feature scaling 

# scaler = StandardScaler()
# x_train = scaler.fit_transform(x_train)
# x_test = scaler.transform(x_test)



# model = SVR(kernel = 'rbf')
# model.fit(x_train , y_train)

# new_input = scaler.transform([[44]]) 
# prediction = model.predict(new_input)

# print(prediction)
