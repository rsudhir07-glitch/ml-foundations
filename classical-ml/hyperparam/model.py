'''
we will use the fifa player dataset , use hyperparamter tuning and see if there are any changes in the metrics

baseline accuracy = 97


'''

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score , recall_score , f1_score , confusion_matrix

from sklearn.model_selection import GridSearchCV , RandomizedSearchCV

df = pd.read_csv('classical-ml/xgboost/first_model/fifa_player_dataset.csv')

columns_to_drop = [
    
    "player_id",
    "player_name",
    "match_id",

    # Data leakage
    "goals_team",
    "goals_opponent",
    "player_rating",
    "performance_score",
    "tournament_rating",
    "offensive_contribution",
    "defensive_contribution",
    "possession_impact",
    "pressure_resistance",
    "creativity_score",
    "consistency_score",
    "clutch_performance_score"
]

df = df.drop(columns=columns_to_drop)

# print(df.select_dtypes(include = object).columns) # to find out which columns have the data type object so we can encode them 

# encoding values
categorial_columns = df.select_dtypes(include = ['object'] ).columns
categorial_columns = categorial_columns.drop('match_result')

df = pd.get_dummies(df, columns = categorial_columns , drop_first = False) # one hot encoded the feature columns 

# features and target
X = df.drop(columns = 'match_result')
y = df['match_result']

le = LabelEncoder()
y = le.fit_transform(y)

X_train , X_test , y_train  , y_test = train_test_split(
    X,y,
    test_size = 0.3,
    random_state= 42,
    stratify=y
)

xgboost_model = XGBClassifier(
    random_state=42
)
## hyperparameter tuning 

params = {
    'n_estimators' : [100, 200 , 500],
    'learning_rate' : [0.1 , 0.05 ],
    'max_depth' : [ 3 , 4, 5],
    'subsample' : [  0.8 , 1.0],
    'colsample_bytree' : [0.8 , 1.0]

}

grid = RandomizedSearchCV(
    estimator  = xgboost_model,
    param_distributions = params,
    n_iter = 50,
    n_jobs=-1,
    cv = 5,
    scoring = 'accuracy'

)

grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)

best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)





# model evaluation 

accuracy = accuracy_score(y_test, y_pred,)
precision = precision_score(y_test, y_pred,average="weighted")
recall = recall_score(y_test, y_pred,average="weighted")
f1score = f1_score(y_test, y_pred,average="weighted")
cm = confusion_matrix(y_test, y_pred)

print('accuracy is :' ,accuracy)
print('precision is :' ,precision)
print('recall is :' ,recall)
print('f1_score is :' ,f1score)
print('confusion matrix is :', cm)

print("Default Accuracy:", 97)
print("Tuned Accuracy:", accuracy)
print(grid.best_params_)

