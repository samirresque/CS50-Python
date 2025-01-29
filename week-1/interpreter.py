user_input = input("enter the arithmetic: ")

terms = user_input.split()
x = int(terms[0])
y = terms[1]
z = int(terms[2])
match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x-z))
    case "/":
        print(float(x/z))
    case "*":
        print(float(x*z))
    


