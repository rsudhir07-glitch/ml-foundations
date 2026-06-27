
'''REGRESSION'''

'''LINEAR REGRESSION'''

import pandas as pd
from sklearn.linear_model import LinearRegression

data =  {
    'x' : [1,2,3,4],
    'y' :  [8,11,14,17]
}

df = pd.DataFrame(data)
x = df[['x']] #* WE WANT THE FEATURE/INPUT IN THE FORM OF A 2D ARRAY
y = df['y']

model = LinearRegression()
train = model.fit(x,y)
prediction = model.predict([[5]])  

print(prediction)   


'''LOGISTIC REGRESSION'''

 #* SAME AS LINEAR REGRESSION, BUT IT GIVES RESULTS IN THE FORM OF 0 OR 1 MEANING FALSE OR TRUE RESPECTIVELY

from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [8], [9], [10]]
Y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X,Y)

prediction = model.predict([[11]])[0] #* [0] GIVES THE INPUT VALUE ONLY, NOT A LIST 
print(prediction)