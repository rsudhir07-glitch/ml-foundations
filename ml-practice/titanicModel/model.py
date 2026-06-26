import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score , recall_score , f1_score 

from sklearn.metrics import confusion_matrix

df = pd.read_csv('ml-practice/titanicModel/titanic.csv')
# Filling the missing values 

mean_age = df['Age'].mean()

df['Age'] = df['Age'].fillna(mean_age)

# Encoding categorial data

le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

# Model training

x = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch']]
y = df['Survived']

x_train, x_test , y_train, y_test = train_test_split(
    x,y,
    test_size = 0.3,
    random_state = 42

)

model = LogisticRegression()
model.fit(x_train , y_train)

y_pred = model.predict(x_test)

# Model Evaluation

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print('accuracy : ' , accuracy)
print('precision : ' , precision)
print('f1 : ' , f1)
print('recall : ' , recall)


# Confusion matrix

cm = confusion_matrix(y_test , y_pred)
print(cm)
print(model.coef_)
print(x.columns)