import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score , recall_score , f1_score , confusion_matrix



df = pd.read_csv('classical-ml/xgboost/second_model/ai_student_impact_dataset (1).csv')

df = df.drop(columns='Student_ID')

type_object = df.select_dtypes(include = 'object').columns
type_object = type_object.drop('Burnout_Risk_Level')

# now we will one hot encode the categorial data
df = pd.get_dummies(df, columns = type_object , drop_first = False )

# now features and target
X = df.drop(columns = 'Burnout_Risk_Level')
y = df['Burnout_Risk_Level']

# now we will label encode the target 
le = LabelEncoder()
y = le.fit_transform(y)



X_train , X_test , y_train , y_test = train_test_split(
    X,y,
    test_size = 0.2,
    random_state = 42
)

xgboost_model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

xgboost_model.fit(X_train, y_train)
y_pred = xgboost_model.predict(X_test)




importance = pd.Series(
    xgboost_model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)



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

