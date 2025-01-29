user_input = input("Enter your string: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#for letter in user_input:
#    if letter in vowerls:
for letter in user_input:
    if letter in vowels:
        user_input = user_input.replace(letter, "")
print(user_input)
