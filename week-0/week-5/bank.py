def main():
    greeting = input("enter greeting: ")
    print(value(greeting))


def value(greeting):
    greeting_split = greeting.lower().split(" ")

    if greeting_split[0] == "hello":
        return "0"
    elif greeting_split[0][0] == "h":
        return "20"
    else:
        return "100"


if __name__ == "__main__":
    main()
