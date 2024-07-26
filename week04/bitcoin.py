import requests
import sys

if len(sys.argv) == 2:
    try:
        number = float(sys.argv[1])
    except:
        sys.exit('Command-line argument is not a number')
else:
    sys.exit('Missing command-line argument')

amount = float(requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate_float']) * number

print(f"${amount:,.4f}")
