
def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("Date: ")
            if len(date) > 10 and "," in date: # if input is not of the form 9/8/2019 (MM/DD/YYYY)
                date = date.replace(",", "").split(" ")
                month = date[0]
                day = int(date[1])
                year = int(date[2])

                if day >= 1 and day <= 31:
                    if month in months:
                        if len(str(year)) == 4:
                            break

                continue

            elif "/" in date:
                date = date.split("/")
                day = int(date[1])
                year = int(date[2])
                month = int(date[0])

                if day >= 1 and day <= 31:
                    if month >= 1 and month <= 12:
                        month = months[month-1]
                        if len(str(year)) == 4:
                            break
                continue
        except ValueError:
            pass
    print(f"{year}-{months.index(month)+1:02}-{day:02}")
main()








