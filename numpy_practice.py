import numpy as np

scores = np.array([
    [78, 85, 90],
    [92, 88, 79],
    [65, 70, 72],
    [89, 91, 94],
    [76, 80, 85]
])

# print('shape is :',scores.shape)
# print('size is :',scores.size)
# print('number of dimensions is :',scores.ndim)
# print('maximum score is :',scores.max())
# print('minimum score is :',scores.min())
# print('average score is :',scores.mean())

# avgscore = np.mean(scores, axis = 1) #*ROW WISE AVERAGE 
# print(avgscore)

# averages = np.mean(scores, axis=1) > 85 #! IMPORTANT
# print(scores[averages]) #* ROWS WHERE AVERAGE IS GREATER THAN 85


# scores[scores < 75] += 5
# print(scores) #* ADDING 5 TO SCORES LESS THAN 75

# scores[scores<70] = 70
# print(scores) #* REPLACING VALUES

# greater = scores > 90
# print(scores[greater])

# average = np.mean(scores, axis = 1)
# sorted = np.argsort(average)
# print(sorted) #* SORTING ROWS BASED ON THEIR AVERAGE IN ASCENDIND 

# sum = np.sum(scores, axis=1)
# print(np.sort(sum)) #* SORTING BASED ON SUM OF SCORES IN A ROW