# Sum
# Nunyie
print("This code produces the sum between 2 inputs.")
def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a number")
            
num1 = valid_input("First Number = ")
num2 = valid_input("Second Number = ")

answer = float(num1+num2)
print("The sum of both numbers = ",answer)