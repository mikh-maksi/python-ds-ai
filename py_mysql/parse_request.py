import requests, json
r = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
print(str(r.text))
k = json.loads(str(r.text))
print(k[0])