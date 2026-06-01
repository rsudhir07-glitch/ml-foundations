# age = int(input("please enter your age "))

# if age < 13:
#     print("you are a child")
# elif age < 20:
#     print ("you are a teenager ")   
# elif age < 60 :
#     print("you are an adult")
# else:
#     print("wassup unc")   



# age = int(input("please enter your age"))
# day = input (" what day is today ?")

# if age > 18 :
#     print ("ticket price is 12$")
 
# elif age < 18 and day == "wednesday" :
#     print ("ticket price is 6$")
# elif age < 18 :
#     print("ticket price is 8$")       
# else:
#     print ("ticket price is 10$")     




# password = input("please enter your password")
# passwordcharlength = len(password)

# if passwordcharlength < 6 : print("your password is weak ")
# elif passwordcharlength <= 10  : print("your password is medium ")
# else : print("your password is strong")




# year = 2032
# if year % 4 == 0  and year % 100 != 0:
#     print ("this is a leap year") 

# elif year % 400 == 0:
#     print("this is a leap year")
# else: print("this is not a leap year ")    



# n = 10
# sumofeven = 0

# for nums in range (1, n+1 ):
#     if nums % 2 == 0:
#         sumofeven = sumofeven + nums 
# print("sum of even numbers from 1 to ", n , "is", sumofeven)        

# given_number = 10
# sumofevennums = 0

# for nums in range(0,given_number+1):
#     if nums % 2 == 0:
#      sumofevennums = sumofevennums + nums 
# print(sumofevennums)    

# num = 5

# for multiplier in range(0,11):
#     value = num * multiplier
#     if multiplier == 5:
#        pass 
#     else: 
#        print(num, "*", multiplier, "=", value)

# name = 'sudhir'
# reversedname = ''

# for characters in name:
#   reversedname = characters + reversedname 

# print(reversedname)  

# text = 'teeter'

# for char in text:
#     if text.count(char) == 1:
#         print(char)


# while True:
 
#  UserInput = int(input("please enter your number : "))
#  if UserInput < 10 > 1:
#     print("you entered the right number")
#     break 
#  else: 
#     print("enter again : ")   


# usernumber = int(input("enter your number : "))
# condition = True 

# if usernumber > 1:
#     for number in range( 2, usernumber):
#      if (usernumber % number == 0):
#         condition = False 
#         break 

# print(condition)    

# import math 

# def square_cube(number):
#     cube = math.floor(number ** 3)
#     square = math.floor(number ** 2)
#     return cube, square 

# cube , square = square_cube (12.2)

# print("cube :", cube , 'square :', square )


# username = input('please enter your name : ')
# default_username = 'customer'

# def greeting(username):

#     if username == '':
#            print('hello ', default_username )
#     else : print('hello ', username )

# greeting(username)        


# def odd_num_generator(num):
#    for numbers in range(0, num + 1, 1):
#     print(numbers)
# odd_num_generator(15)   

 

# class name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname 
#         self.lastname = lastname 

#     def fullname(self):
#         return f"{self.firstname} {self.lastname}"
    

# student1 = name('sudhir', 'dhankar')    

# print(student1.fullname())


#! HERE 

# class information:
#     usecount = 0 

#     def __init__ (self, fullname, age):
#         self.fullname = fullname
#         self.age = age
#         information.usecount += 1 
#     def fullinformation(self):
#       return 'candidates name is' , self.fullname ,'and his age is' ,self.age 
    
     
# candidate1 = information('sudhir', 46)
# candidate2 = information('ronaldo', 41)
# candidate3 = information('neymar', 35)

# print(candidate1.fullinformation())
# print(candidate2.fullinformation())
# print(candidate3.fullinformation())

# print(information.usecount)