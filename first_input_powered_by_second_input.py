# Exponent
# Nunyie
print("This code raises the first number entered by the second number entered")
print("Output is rounded to 5 decimal places.")

def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a number")
            
num1 = valid_input("First Number = ")
num2 = valid_input("Second Number = ")

variable = float(num1**num2)
answer = round(variable, 5)
print(f"{num1} to the power of {num2} = {answer} ")