
camelCase = input("Enter the variable name: ")
snake_case = "" #an empty string
for letter in camelCase:
    if letter.isupper():
        snake_case += "_" + letter.lower()
    else:
        snake_case += letter.lower()

print(snake_case)




