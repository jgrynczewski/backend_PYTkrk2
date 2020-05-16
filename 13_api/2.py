# Command-line app
import requests

base = input("Pierwsza waluta:")
symbol = input("Druga waluta:")

res = requests.get("http://data.fixer.io/api/latest?access_key=032053b70cf616de08638aeaeb1cfd1d",
                   params={"base":base, "symbols": symbol})
if res.status_code != 200:
    raise Exception("Error: API request unsuccessful.")

data = res.json()

rate1 = data["rates"][symbol]


print(f"1 {base} to {rate1} {symbol}")
