import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error , root_mean_squared_error, r2_score

df = pd.read_csv('/Users/sudhirkumardhankar/Ai:ML Learning/practiceml.py/employeeData.csv')

x = df[['Age' , 'Experience' , 'Education_Level' , 'Projects_Completed']]
y = df['Salary']

model = LinearRegression()

x_train , x_test , y_train , y_test = train_test_split(
    x , y ,
    test_size = 0.4,
    random_state = 42

)

model.fit(x_train , y_train ) #Train the model on the training data

y_pred = model.predict(x_test) # Now the model will make predictions using the testing data

mae = mean_absolute_error(y_test , y_pred)
mse = mean_squared_error(y_test , y_pred)
rmse = root_mean_squared_error(y_test , y_pred)
rsquare = r2_score(y_test , y_pred)

print('mae : ' ,mae)
print('mse : ' ,mse)
print('rmse : ' ,rmse)
print('rsquare : ' ,rsquare)

for actual, pred in zip(y_test[:5], y_pred[:5]):
    print(f"Actual: {actual:.0f} | Predicted: {pred:.0f}")