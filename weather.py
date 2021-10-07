import sys
import requests as rq
import pprint as pp

class Weather:
    def __init__(self, api_key, date, localization):
        self.api_key = api_key
        self.date = date
        self.localization = localization
        #self.data = self.get_data_handler()
        self.data = {
            '2021-10-05': 'Bedzie lało',
            '2021-10-04': 'Bedzie słonko'
            }

    def get_data_handler(self):
        pass
        
    def show_localization(self):
        print(self.localization)

    def get_data(self):
        URL = f'https://api.weatherapi.com/v1/history.json?key={self.api_key}&q={self.localization}&dt={self.date}'
        r = rq.get(URL)
        return r.json()

    def __str__(self): # pozwala na printowanie obiektu pojedyńczo
        return f'{self.date}, {self.localization}'

    def __repr__(self): # pozwala na printowanie obiektu np w liście
        return f'{self.date}, {self.localization}'

    def __getitem__(self, key): # pozwala na odwoływanie się do obiektu jak do słownika
        return self.data[key]
    
    def __setitem__(self, key, value): # pozwala na zmienianie wartości w słowniku obiektu
        self.data[key] = value
        
api_key = sys.argv[1]
date = sys.argv[2]
localization = 'London'

w = Weather(api_key, date, localization)
w['2021-10-05'] = 'Test'
print(w['2021-10-05'])

