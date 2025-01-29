

def hello(g):
    greeting = g.strip()
    if greeting.split(",")[0] == "hello":
        return "$0"
    elif greeting.split()[0][0] == "h":
        return "$20"
    else:
        return "$100"

def main():
    greeting = input("enter the greeting: ").lower()
    buck = hello(greeting)
    print(buck)

main()




