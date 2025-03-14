# NotEqual
# Nunyie
print("This code tells when 2 entered values are not equal.")
def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a Number")

num1=valid_input("First Number = ")
num2=valid_input("Second Number = ")

if num1 != num2:
    print("Both Number are not equal.")
    
else:
    print("Numbers entered is equal")