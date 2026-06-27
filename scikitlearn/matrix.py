
'''CLASSIFICATION METRICES'''

'''

# Classification metrics are used to evaluate machine learning models that predict categories (classes) rather than continuous numerical values.

# Examples:

# Yes / No
# Spam / Not Spam
# Cat / Dog
# Pass / Fail
# Fraud / Not Fraud
# Disease / No Disease

# classification matrices - recall, accuracy, f1_score, precision and confusion_matrix

'''

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

y_true = [0, 1, 1, 0, 1, 0, 1]
y_pred = [0, 1, 0, 0, 0, 1, 1]

accuracy = accuracy_score(y_true , y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true , y_pred)
f1score = f1_score(y_true , y_pred)

print('accuracy :' , accuracy )

print('precision :' , precision )

print('recall :' , recall )

print('f1_score :' , f1score )

'''CONFUSION MATRIX'''

from sklearn.metrics import confusion_matrix

y_true = [1, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 0, 1, 1]

cm = confusion_matrix(y_true , y_pred)
print(cm)

# # RESULT - TN FP
# #             FN TP


'''REGRESSION METRICES'''

'''

# Regression metrices are used when we are dealing with numerical predictions, such as - house price, student marks etc...

# Regression matrix - MAE , MSE , RMSE , R square

'''
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

y_true = [10, 20, 30, 40]

y_pred = [12, 18, 35, 38]

mae = mean_absolute_error(y_true, y_pred)   
mse = mean_squared_error(y_true, y_pred) 
rmse = root_mean_squared_error(y_true, y_pred)
rsquare = r2_score(y_true, y_pred)

print('mae :' , mae)
print('mse :' , mse)
print('rmse :' , rmse)
print('rsquare :' , rsquare)



