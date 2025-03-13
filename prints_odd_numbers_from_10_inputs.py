#Prog8
#Odd ones out
#Nunyie
print("This code shows the odd ones out from 10 inputed numbers")
print("Output is rounded the nearest Integer.")

def valid_input(u):
    while True:
        try:
            return int(input(u))
        except ValueError:
            print("Please enter a whole number")
            
numbers = []
for i in range(1, 11):
    number = valid_input(f"Number {i} = ")
    numbers.append(number)
    
odd_num = [num for num in numbers if num % 2 != 0]
if odd_num:
    print("They are:", [round(num, 5) for num in odd_num])
else:
    print("There are no odd numbers in the entered values.")