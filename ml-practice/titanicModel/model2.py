import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.metrics import accuracy_score, precision_score , recall_score , f1_score


df = pd.read_csv('ml-practice/titanicModel/titanic.csv')

# handling missing data
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# encoding
encoder = LabelEncoder()
df['Sex'] = encoder.fit_transform(df['Sex'])

# model training 
x = df[['Age' , 'Sex' , 'SibSp' , 'Fare', 'Pclass' , 'Parch' ]]
y = df['Survived']

x_train , x_test , y_train , y_test = train_test_split(
  x,y,
  test_size = 0.3,
  random_state = 42

)
gradient_model = GradientBoostingClassifier(
   n_estimators = 150,
   learning_rate = 0.1,
   random_state = 42,
   max_depth = 2


)
gradient_model.fit(x_train , y_train)

y_pred = gradient_model.predict(x_test)

# model evaluation 

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('accuracy : ' , accuracy)
print('precision : ' , precision)
print('f1 : ' , f1)
print('recall : ' , recall)

