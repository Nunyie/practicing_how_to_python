# Difference
# Nunyie
print("This code produces the difference between 2 inputs.")
def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a number")
            
num1 = valid_input("First Number = ")
num2 = valid_input("Second Number = ")

variable = float(num1-num2) #variable is when the answer can either be a negative or a positive number
answer = abs(variable) #answer uses absolute so it would variable becomes positive
print("The difference between both numbers =",answer)