def grocery():
    items = {} #dict for storing the item as well as its count
    while True:
        try:
            item = input().lower()
        except EOFError:
            break

        if item in items:
            #increase the count of the item; don't apend the items[] list
            items[item] += 1
        else:
            items[item] = 1

    for item in sorted(items):
        print(f"{items[item]} {item.upper()}")

def main():
    grocery()

main()

