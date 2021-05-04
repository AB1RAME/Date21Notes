import json

pet_data = {'name': 'Bob', 'Food': 'Carrots'}
print(pet_data)
pet_data_json_str = json.dumps(pet_data)

print(pet_data_json_str)


# with open ('new_json_file.json','w') as jsonfile:
#    json.dump(pet_data,jsonfile)
# with open('new_json_file.json') as jsonfile:
#     pet = json.load(jsonfile)
#     print(type(pet))
#     print(pet['name'])


class RatesParser:
    def __init__(self, rates_file):
        rate_info = self._open_json_file(rates_file)
        self.base = rate_info['base']
        self.rates = rate_info['rates']
        self.gbp = self.base['GBP']

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)


rates_reader = RatesParser('exchange_rates.json')
print(rates_reader.rates)
