
'''DECISION TREES'''

from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [5], [6], [7]]

Y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, Y)

prediction = model.predict([[4]])

print(prediction)