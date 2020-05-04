# For the exercise, look up the methods and functions that are available for use
# with Python lists.

import numpy

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
for i in range(8, 11):
    x.append(
        i
    )
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(x)
# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
for t in range(len(x)):
    print(x[t])

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# def multiply(theList):
#     results = 1000
#     for x in theList:
#         results = results * x
#     return results
#     print(multiply(x * 1000))

values = numpy.prod(x)
print(values * 1000)
