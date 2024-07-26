given = 0

while given < 50:
    print('Amount Due:', 50 - given)
    amount = int(input('Insert Coin: '))
    if amount in [25, 10, 5]:
        given += amount

print('Change Owed:', given - 50)
