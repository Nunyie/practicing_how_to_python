#Prog7
#sum of 10
#Nunyie
print("This code produces the sum of 10 numbers")
print("Output is rounded to 5 decimal places.")

def valid_input(u):
    while True:
        try:
            return float(input(u))
        except ValueError:
            print("Please enter a number")
            
numbers = []
for i in range(1, 11):
    number = valid_input(f"Number {i} = ")
    numbers.append(number)
    
total_sum = sum(numbers)
rounded_sum = round(ts, 5)
print(f"The sum of the numbers entered is = {rounded_sum}")