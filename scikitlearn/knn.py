'''K N N '''

#* PREDICTION IS BASED ON NEIGHBORS
#* 0 MEANS FALSE AND 1 MEANS TRUE
   
from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [8], [9], [10]] 

Y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors = 3) #* SEE FOR 3 NEIGHBORS
model.fit(X,Y)
prediction = model.predict([[7]])
print(prediction)


#* K NEAREST NEIGHBORS

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error , r2_score
import pandas as pd
from sklearn.preprocessing import StandardScaler
data = {
    'Age': [20, 25, 30, 35, 40 , 45 , 50, 55, 60 , 65],
    'Salary': [20000, 30000, 50000, 70000, 90000 , 100000 , 120000, 130000 , 140000 , 160000]
}   

df = pd.DataFrame(data)
knn = KNeighborsRegressor(n_neighbors = 3)

x = df[['Age']]
y = df['Salary']

x_train , x_test , y_train , y_test = train_test_split(
    x,y,
    test_size = 0.2,
    random_state = 42
)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

knn.fit(x_scaled , y_train)

y_pred = knn.predict(x_test_scaled)

print(r2_score(y_test , y_pred))
