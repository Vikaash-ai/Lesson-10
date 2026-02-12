# The variables
string = str(input("Enter a string: "))
total = 1

# The for loop
for i in range(len(string)):
    if string[i] == ' ':
        total = total + 1

print(f"\n The total number of words in this string: {string}, = {total}")