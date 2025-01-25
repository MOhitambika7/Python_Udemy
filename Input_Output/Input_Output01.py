# Taking string input.
Name = input("Enter your name:- ")
print(f"Hey {Name}")

# Taking Numeric input
Age = int(input("Enter your age: ")) # This int before the input changes the string to integer value. Because by default input is string.
print(f"{Name} is {Age} years old.")

Height = float(input("Enter your height: ")) # This float coverts string input into floating point value.
print(f"{Name} height is {Height}") 

# Advanced Input output.
# Using .format() method
name = "Alice"
age = 18
print("I am {}. I am {} years old.".format(name, age))

# Taking the multiple inputs in one line.
x, y = input("Enter the two numbers separated by a space: ").split()
print("You entered:- ", x, "and", y)

numbers = list(map(int,input("Enter the number separated by spaces:- ").split()))
print(f"Numbers are:- {numbers}")