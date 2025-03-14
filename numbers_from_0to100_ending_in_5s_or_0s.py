# ends with 0/5
# Nunyie
print("This code prints out numbers that ends in 0 or 5 from 0-100.")
           
for number in range(0, 101):
    if number %5 == 0 or number %10 ==0:
        print(number)