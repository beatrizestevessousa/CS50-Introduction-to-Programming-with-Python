greeting = input('Greeting: ')

if 'hello' in greeting.lower():
    price = 0
elif greeting[0].lower() == 'h':
    price = 20
else:
    price = 100

print(f'${price}')
