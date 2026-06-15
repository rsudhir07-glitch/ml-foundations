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


