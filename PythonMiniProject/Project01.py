# Program to calculate the percentage.
def calculate_percentage(total, obtained):
     if total > 0:
         return(obtained/total)
     else:
         return None
 
# Main program
print("Welcome to ithe percentage calculating calculator program.")

# Handeling user input.
try:
    total = float(input("Enter the total value:-"))
    obtained = float(input("Enter the obatained value:- "))     
    
    percentage = calculate_percentage(total, obtained)
    
    if percentage is not None:
        print(f"The obtained percentage is:- {percentage}")
        
    else:
        print("Error: The value must be greater than 0.")
        
except ValueError:
    print("Error: Plese enter the valid numeric value.")          