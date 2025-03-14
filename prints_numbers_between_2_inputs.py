# Inbetween
# Nunyie
print("Numbers inbetween input.")
  
def valid_input(u):
    while True:
        try:
            return int(input(u))
        except ValueError:
            print("Please enter a number")
            
num1= valid_input("Input 1 = ")
num2= valid_input("Input 2 = ")

start = min(num1, num2)
end = max(num1, num2)

print(f"Numbers between {start} and {end} :")
for number in range(start + 1, end):
    print(number)