
def main():
    plate = input("Plate: ").upper() #assume input in uppercase
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    plate_length = len(s)
    if (plate_length >= 2 and plate_length <= 6) and s.isalnum():
        if s[0].isalpha() and s[1].isalpha():
            if plate_length > 2:
                for i in range(2,plate_length):
                    if s[i].isnumeric():
                        first_numeric_pos = i # "HI245" = 2
                        if s[first_numeric_pos] != "0":
                            sliced_s = s[i:plate_length]
                            if sliced_s.isdigit():
                              return True
                        else:
                            return False

                if s.isalpha():
                    return True
            else:
                return True

    return False

if __name__ == "__main__":
    main()
