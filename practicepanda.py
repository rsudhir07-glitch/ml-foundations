import pandas as pd 

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma",
             "Frank", "Grace", "Helen", "Ian", "Jack"],
    "Department": ["IT", "HR", "IT", "Sales", "HR",
                   "IT", "Sales", "HR", "IT", "Sales"],
    "Age": [25, 30, 28, 35, 27, 32, 29, None, 31, 26],
    "Salary": [50000, 45000, 60000, 55000, 48000,
               65000, 52000, None, 62000, None],
    "JoiningDate": [
        "2020-01-15", "2019-03-10", "2021-07-20",
        "2018-11-01", "2022-02-12", "2017-06-18",
        "2020-08-25", "2021-12-05", "2019-09-30",
        "2023-01-01"
    ],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai",
             "Delhi", "Bangalore", "Mumbai", "Delhi", "Bangalore"]
}

"""NAME OF EMPLOYEES IN IT DEPARTMENT"""

df = pd.DataFrame(data)
# itemployees = df[df['Department'] == 'IT']['Name']
# print(itemployees) 

"""MULTIPLE CONDITION FILTER"""

# multifilter = df[df['Age'].between(25,30)]
# print(multifilter)


"""SORTING IN 2 COLUMNS""" 

# sortedsalary = df.sort_values(by=['Age', 'Salary'], ascending=[True, False])
# print(sortedsalary)

"""TOP 3 HIGHEST PAID"""

# highestpaid = df.sort_values(by="Salary", ascending=False)
# print(highestpaid.head(3))

"""NEW COLUMN"""

# bonuscolumn = df['Bonus'] = df['Salary'] * 0.1
# total = df['TotalPay'] = bonuscolumn + df['Salary']
# print(df)

'''MAXIMUM SALARY'''

# maxsalary = df['Salary'].max()
# print(maxsalary)
# employee = df[df['Salary'] == maxsalary]
# print(employee)

'''MISSING VALUES'''

# missingage = df['Age'].isnull()
# print(df[missingage])

'''FILLING MISSING COLUMNS'''

# missingage = df['Age'].fillna(df['Age'].mean())
# print(missingage)

'''AVERAGE SALARY BY DEPARTMENT'''

# result = df.groupby('Department')['Salary'].mean
# print(result)