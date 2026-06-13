

"""     FUNCTIONS PRACTICE SHEET    """



'''LARGEST OF THE TWO '''

# def larger(a,b):
#     if a>b:
#         return a 
#     else: return b

# print(larger(7,10))    

'''RETURN LENGTH OF A GIVEN STRING'''

# def stringlength(text):
#    return len(text)

# print(stringlength('snil'))

'''SUM OF ALL THE NUMBERS IN A LIST'''

# numbers = [1,2,3,4,5,5,6]
# def sum():
#     finalsum = 0
#     for i in numbers:
#       finalsum += i
#     return finalsum 
  
# result = sum()
# print(result)

'''LARGEST NUMBER IN A LIST'''

# numbers = [2,4,6,7,3,9]

# def larger():
#     largest = 0
#     for i in numbers:
#         if i > largest:
#             largest = i
#     return largest 

# result = larger()
# print(result)         

'''COUNT THE VOWELS'''

# def vowelcounter(text):
#     count = 0
#     for i in text:
#         if i in 'aeiou' :
#             count = count + 1
#     return count 

# result = vowelcounter('sudhir')
# print(result)        

'''REVERSED STRING'''

# def reverser(text):
#     reversed = ''
#     for i in text:
#       reversed = i + reversed
#     return reversed

# print(reverser('sudhir'))  


'''FUNCTION CALLING FUNCTION'''

# def square(a):
#     return a * a

# def sumofsquare():
#     return square(2) + square(3)

# result = sumofsquare()
# print(result)


'''LAMBDA FUNCTIONS'''

# func = lambda a , b : a ** b

# print(func(2,4))

'''FILTER'''

# def even(n):
#     return n % 2 == 0

# print(even(5)) #* THIS WILL RETURN BOOLEAN VALUE

# n = (1,2,3,4,5,6,7,8,9,10)
# filtered = filter(even,n) #* FILTER OUT THE VALUES ACCORDING TO THE THE FUCNTION

# print(list(filtered))


'''MAP'''

# map(function,iter)

# def double(n):
#     return n*2

# n = [1,2,3,4]

# result = map(double,n) #* MAP APPLIES THE FUNCION TO EACH VALUE OF THE GIVEN ITERATOR, LIKE THE LIST, TUPLES ETC...
# print(list(result))


'''REDUCE'''

# reduce(function,iter,[initial])

# import functools
                    
# def add(x,y):    #* IT APPLIES A PARTICULAR FUNCTION TO ALL THE LIST ITEMS, NO MATTER THE NUMBER OF PARAMETERS IN THE FUNCTION
#     return x + y
             
# n = [1,2,3,4,5]
# result = functools.reduce(add, n)
# print(result)


''' COMBINATION OF MAP, FILTER AND REDUCE '''

" SUM OF EVEN NUMBERS IN A LIST"

# import functools

# n = [1,2,3,4,5]
# def even(n):
#     return n % 2 == 0

# f = filter(even, n) #* FILTER OUT THE ELEMENTS OF n ON THE BASIS OF EVEN FUNCTION
# m = map(lambda x : x**2 , f) #* USE THE FILTERED VALUES FROM f AND SQUARE THEM
# r = functools.reduce(lambda x,y : x + y , m) #* NOW WE USE THE SQUARE VALUES FROM m ADD THEM ALTOGETHER

# print(r)

'''RECURSION'''

#* A FUNCTION THAT CALLS ITSELF

# def countdown(n):

#     if n == 0:
#         return 
#     print(n)
#     countdown(n - 1)

# countdown(5)    

'''CLOSURE'''

# def number(n):
#     def power(x):
#         return n ** x
#     return power
# num = number(4)
# print(num(2))


# def counter():
#     count = 0

#     def inner():
#         nonlocal count
#         count+=1

#         return count
#     return inner 

# res = counter()  
# print(res())
# print(res())
# print(res())

# def greet(text):

#     def inner():
#         return f"hello {text}"  
#     return inner

# greetsudhir = greet('sudhir')
# print(greetsudhir())