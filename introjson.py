import json
class RatesParser:
    def __init__(self,rate_file):
        rates_info=self._open_json_file(rate_file)
        self.base=rates_info['rates']
        self.gbp=self.base['GBP']
    def _open_json_file(self,file):
        with open(file) as rates:
            return json.load(rates)
rates_reader=RatesParser('exchange_rates.json')
print(rates_reader)