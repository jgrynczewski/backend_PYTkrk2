import requests

res = requests.get("https://www.google.pl")
print(res.text)