import requests
import sys


r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
r.json()

fiyat = r.json()["bpi"]["USD"]["rate_float"]
fiyat = float(fiyat)

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isnumeric or (type(sys.argv[1]) == float):
    sys.argv[1] = float(sys.argv[1])
    amount = fiyat*(sys.argv[1])
    amount = float(amount)
elif sys.argv[1].isnumeric() == False:
    sys.exit("Command-line argument is not a number")



print(f"${amount:,.4f}")





