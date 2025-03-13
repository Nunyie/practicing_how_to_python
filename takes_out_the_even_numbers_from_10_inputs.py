# Prog7
# 10 inputs find even
# Nunyie

print("Pulls out the even numbers from 10 inputs")

def valid_input(u):
    while True:
        try:
            return int(input(u))
        except ValueError:
            print("Please enter a whole number")

numbers = []
for i in range(1, 11):
    number = valid_input(f"Input {i} = ")
    numbers.append(number)
    
even_number = [num for num in numbers if num % 2 == 0]
if even_number:
    print("They are:", [round(num, 0) for num in even_number])
else:
    print("There are no even numbers in the entered values.")