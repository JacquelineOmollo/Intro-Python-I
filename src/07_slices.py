"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
s1 = a[1: -4]
print(s1)

# Output the second-to-last element: 9
s2 = a[-2: -1]
print(s2)

# Output the last three elements in the array: [7, 9, 6]
s3 = a[-3:]
print(s3)

# Output the two middle elements in the array: [1, 7]
s4 = a[-4: -2]
print(s4)

# Output every element except the first one: [4, 1, 7, 9, 6]
s5 = a[1:]
print(s5)

# Output every element except the last one: [2, 4, 1, 7, 9]
s6 = a[: -1]
print(s6)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
s7 = s[-6:-1]
print(s7)
