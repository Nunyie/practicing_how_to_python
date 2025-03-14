# Smaller Num
# Nunyie
print("This code shows the smaller number between 2 entered inputs.")
def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Invalid Input. Please enter a Number.")
    
print("Please enter 2 numbers")

num1 = valid_input("First Number = ")
num2 = valid_input("Second Number = ")

if num1 < num2:
    print("The smaller number is",num1)
    
elif num2 < num1:
    print("The smaller number is",num2)
    
else:
    print("Both numbers are equal")