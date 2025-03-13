#Prog5
#quotient
#Nunyie
print("This code produces the quotient between 2 numbers")
print("Output is rounded to 5 decimal places.")

def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a number")
            
num1 = valid_input("First Number = ")
num2 = valid_input("Second Number = ")

variable = float(num1/num2)
answer = round(variable, 5)
print("The quotient is =", answer)