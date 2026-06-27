'''GRADIENT BOOSTING'''

'''

MAKES TREES SEQUENTIALLY WITH EACH TREE TRYING TO CORRECT THE MAKES OF THE PREVIOUS ONE
USED FOR BOTH CLASSIFICATION AND REGRESSION

VERY HIGH ACCURACY
SLOWER TO TRAIN
MORE SENSITIVE TO TUNING
CAN OVERFIT IF NOT TUNED

'''

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import GradientBoostingRegressor

# data = {
#     'Age': [22, 25, 47, 52, 46],
#     'Salary': [25000, 32000, 48000, 52000, 50000]
# }

# df = pd.DataFrame(data)

# X = df[['Age']]
# y = df['Salary']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y,
#     test_size=0.2,
#     random_state=42
# )

# model = GradientBoostingRegressor(
#     n_estimators=100,
#     learning_rate=0.1,
#     random_state=42
# )

# model.fit(X_train, y_train)

# prediction = model.predict([[32]])

# print(prediction)