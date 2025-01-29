amount_due = 50
change_owed = 0

while amount_due > 0:
    print("Amount Due:", amount_due)
    insert_coin = int(input("Insert Coin: "))
    while insert_coin != 25 and insert_coin != 5 and insert_coin != 10:
        print("Amount Due:", amount_due)
        insert_coin = input("Insert Coin: ")

    amount_due -= insert_coin

if amount_due < 0:
    change_owed = abs(amount_due)

print("Change Owed:",change_owed)


