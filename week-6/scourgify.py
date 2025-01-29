import csv
import sys
import os

def main():

    # expect two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not os.path.exists(sys.argv[1]):
        sys.exit(f"Couldn't read {sys.argv[1]}")

    # else
    file_to_read = sys.argv[1]
    names_houses = []
    file_to_write = sys.argv[2]
    with open(file_to_read, "r") as read_f:
        reader = csv.DictReader(read_f)
        for row in reader:
            names_houses.append([row["name"], row["house"]])


    with open(file_to_write, "w") as write_f:
        writer = csv.DictWriter(write_f, fieldnames = ["first","last", "house"])
        writer.writeheader()
        for name_house in names_houses:
            name = name_house[0].rsplit(", ")
            last_name = name[0]
            first_name = name[1]
            house = name_house[1]
            writer.writerow({"first": first_name, "last": last_name, "house": house})



if __name__ == "__main__":
    main()
