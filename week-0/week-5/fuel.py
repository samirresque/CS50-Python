
def main():

    fraction = input("Fraction: ")
    percentage = convert(fraction)
    fuel = gauge(percentage)
    print(fuel)

def convert(fraction):
    x = fraction.split("/")
    numerator = x[0]
    denominator = x[1]

    if not numerator.isdigit() or not denominator.isdigit():
        raise ValueError
    numerator = int(numerator)
    denominator = int(denominator)
    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator:
        raise ValueError

    return round((int(numerator)/int(denominator))*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
