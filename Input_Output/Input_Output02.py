# Error handling.
try:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("You entered:", numbers)
except ValueError:
    print("Please enter the valid integers only.")