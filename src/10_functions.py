# Write a function is_even that will return true if the passed-in number is even.
# Read a number from the keyboard
num = input("Enter a number: ")
num: int = int(num)

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        return True



# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


if is_even(num) == True:
        print("Even!")
else:
        print("Odd")
print(num)