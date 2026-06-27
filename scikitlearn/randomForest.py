
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
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

data = {
    'Age': [22, 25, 47, 52, 46],
    'Salary': [25000, 32000, 48000, 52000, 50000],
    'Purchased': [0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)
x = df[['Age']]
y = df['Salary']

x_train , x_test , y_train , y_test  = train_test_split(
    x , y , 
    test_size = 0.2,
    random_state = 42
)
model_1 = RandomForestRegressor(n_estimators = 100 , random_state = 42)

model_1.fit(x_train , y_train)
y_pred = model_1.predict([[32]])
print(y_pred)

