# Write a python program to demonstrate arithmatic and comparison operator.
Num1 = int(input("Enter the first number :- "))
Num2 = int(input("Enter the second number:- "))

# Arithmatic operation.
print(f"The addition of the two numbers  {Num1} + {Num2} is:- {Num1 + Num2}")
print(f"The difference of the two number {Num1} - {Num2} is:- {Num1 - Num2}")
print(f"The multiplication of the two numbers {Num1} * {Num2} is:- {Num1 * Num2}")
print(f"The division of the two numbers {Num1} / {Num2} is:- {Num1/Num2}")
print(f"The exponential of the two numbers {Num1} ** {Num2} is:- {Num1 ** Num2}")
print(f"The modulo the the two numbers {Num1} % {Num2} is:- {Num1%Num2}")
print(f"The floor division of the two numbers {Num1} // {Num2} is:- {Num1//Num2 if Num2 != 0 else 'undefined(Division by zero.)'}")

# Comparision operator.
print(f"Is {Num1} equal to {Num2}? {Num1 == Num2}")
print(f"Is {Num1} does not equal to {Num2}? {Num1 != Num2}")
print(f"IS {Num1} greater than {Num2}? {Num1 > Num2}")
print(f"IS {Num1} less than {Num2}? {Num1 < Num2}")
print(f"Is {Num1} greater than or equal to {Num2}? {Num1 >= Num2}")
print(f"Is {Num1} less than or equal to {Num2}? {Num1 <= Num2}")
