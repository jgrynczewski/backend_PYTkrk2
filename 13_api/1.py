import requests

res = requests.get("http://data.fixer.io/api/latest?access_key=032053b70cf616de08638aeaeb1cfd1d&base=EUR&symbols=USD,PLN")
if res.status_code != 200:
    raise Exception("Error: API request unsuccessful.")

data = res.json()

rate1 = data["rates"]["PLN"]
rate2 = data["rates"]["USD"]


print(f"1 EUR to {rate1} PLN")
print(f"2 EUR to {rate2} USD")
