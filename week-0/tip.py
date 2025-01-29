def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = float(d.replace("$", ""))
    return float(f"{d:.1f}")


def percent_to_float(p):
    # TODO
    p = float(p.replace("%", ""))
    return float(p/100)


main()
