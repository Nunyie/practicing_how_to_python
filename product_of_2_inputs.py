#Prog4
#Product
#Nunyie
print("This code produces the product between 2 numbers")
print("Output is rounded to 5 decimal places.")
def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a number")
            
num1 = valid_input("First Number = ")
num2 = vvalid_inputi("Second Number = ")

non_rounded_answer = float(num1*num2)
answer = round(non_rounded_answer, 5)
print("The product of both numbers =", answer)