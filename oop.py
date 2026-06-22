# class student:
#     def __init__(self):
#         print('init is running')

# student() #* "INIT IS RUNNING"

''''''
#* class is the blueprint which we use to create objects

# class student:
#     def __init__(self, name, marks):
#         print('student being added to the database')
#         self.name = name
#         self.marks = marks
       
#* self refers to the object being created using class
# s1 = student('sudhir', 34)
# print(s1.name)        
# print(s1.marks)


''''''
# class student:
#      def __init__(self, name, marks):
#           self.name = name
#           self.marks = marks

#      def welcome(self): #* THIS IS A METHOD
#           return f"welcome, {self.name}"

# s1 = student('sudhir', 56)
# print(s1.welcome())
# print(s1.marks)

''''''
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def averagescore(self):
#        print('hi',self.name , 'your average score is' , sum(self.marks)/len(self.marks)) 
    
# s1 = student('sudhir', [3,4,5])  
# s1.averagescore() 
     
# s2 = student('ronaldo', [4,5,6])
# s2.averagescore()  
      
'''''' #! IMPORTANT 
# class Account:
#     def  __init__(self, number, balance):
#         self.number = number
#         self.balance = balance

#     def debit(self, amount):
#         self.balance -= amount
#         print('your remaining balance is', self.balance)
    
#     def credit(self, amount):
#         self.balance += amount
#         print('your remaining balance is', self.balance)
    
        
# acc1 = Account(7489, 10000)
# acc1.debit(5000) 
# acc1.credit(10000)    

'''INHERTITANCE'''

# class car:    
#     def start(self): print('started')
    
#     def stop(self): print('stopped')

# class carname(car):
#     def __init__(self, name):
#         self.name = name

# class cartype(carname):
#     def  __init__(self, type , name):
#         super().__init__(name)
#         self.type = type
      
# car1 = cartype('diesel','fortuner')

# print(car1.name)
# print(car1.type)


# class parent:
#     def greet(self):
#         print('hello user')


# class child(parent):
#     def hello(self): #* NO SUPER() NEEDED WHEN CALLING INHERITED METHODS
#         print('welcome')    


# d = child()
# print(d.greet())


# class person:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print('NAME :', self.name)
#         print('AGE :' ,self.age)    


# class student(person):
#     def __init__(self, name, age , course):
#         super().__init__(name,age) #* OVERRIDING PARENTS __init__() AND NEED PARENT SETUP, USE SUPER()
#         self.course = course

#     def display(self):
#         print('student details')
#         super().display() #* OVERRIDING ANY METHOD BUT NEED PARENT SETUP TOO, USE SUPER()
#         print('COURSE:' , self.course)


# s1 = student("Sudhir", 18, "BA English")

# s1.display()