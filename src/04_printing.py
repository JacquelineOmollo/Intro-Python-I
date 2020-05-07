"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("%d %d %s" % (x, y, z))

# Use the 'format' string method to print the same thing
name = input("What's your name? ")

if name == "Jackie":
    print("Hello, nice to see you {}".format(name))

print("Have a nice day!")

# Finally, print the same thing using an f-string
name = "Eden"
age = 42
print(f"Hello, Her name is {name} and she is {age} years old.")
