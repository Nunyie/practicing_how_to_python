#Prog5
#Remainder
#Nunyie
print("This code produces the remainder the first number is divided by the second.")

def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a number")
            
num1 = valid_input("First Number = ")
num2 = valid_input("Second Number = ")

remainder = num1 % num2
print("The remainder is =", remainder)