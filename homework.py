print("Enter a number with a power: ")

num = int(input("Number: "))
power = int(input("Power: "))
multiply = 1

for i in range(power):
    multiply = multiply * num
    
print(multiply)