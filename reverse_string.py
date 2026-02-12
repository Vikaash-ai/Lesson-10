# The string
string = str(input("Please enter a string: "))

string2 = ' '
# for loop
for i in string:
    string2 = i + string2
    
print(f"\n Original string: {string}")
print(f"\n Reversed String: {string2}")