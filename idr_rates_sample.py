import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.7755559512482e-05, 'date': 'Thu, 13 Aug 2020 12:00:02 GMT', 'inverseRate': 14758.936494588},
             'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.7416373930399e-05, 'date': 'Thu, 13 Aug 2020 12:00:02 GMT', 'inverseRate': 17416.634516353}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])