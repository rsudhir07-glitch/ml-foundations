import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score , recall_score , f1_score
from sklearn.metrics import confusion_matrix

df = pd.read_csv('xgboost/first_model/fifa_player_dataset.csv')

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
    random_state= 42
)



model = XGBClassifier(random_state = 42)
model.fit(X_train ,y_train )
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction,)
precision = precision_score(y_test, prediction,average="weighted")
recall = recall_score(y_test, prediction,average="weighted")
f1score = f1_score(y_test, prediction,average="weighted")
cm = confusion_matrix(y_test, prediction)

print(accuracy)
print(precision)
print(recall)
print(f1score)
print('confusion matrix')
print(cm)

