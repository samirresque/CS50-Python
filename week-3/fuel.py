def main():
    fuel = fuel_percent()
    if fuel <= "1":
        print("E")
    elif fuel >= "90":
        print("F")
    else:
        print(f"{fuel}%")

def fuel_percent():
    while True:
        try:
            fuel = input("Fuel Fraction: ")
            x = fuel.split("/")
            numerator = int(x[0])
            denominator = int(x[1])
            if denominator == 0 or numerator > denominator:
                continue
        except ValueError:
            print("Invalid Fraction!")
        else:
            return f"{round((numerator/denominator)*100)}"

main()
