import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
        except:
            break
        names.append(name)

    names = p.join(names)
    print(f"Adieu, adieu, to {names}")


if __name__ == "__main__":
    main()
