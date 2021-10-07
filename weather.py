import sys
import requests as rq
import pprint as pp
import datetime as dt

class Weather:
    def __init__(self, api_key, date, localization):
        self.api_key = api_key
        self.date = date
        self.localization = localization
        self.data = self.get_data()

    def get_data_handler(self, date):
        exists = False
        with open('file.txt', 'r+') as f:
            lines = f.readlines()
            for id,line in enumerate(lines):
                if line == f'{date}\n':
                    avg, min, max, hum, wind = lines[id+1].replace('\n','').split(',')
                    exists = True
            if exists == False:
                avg, min, max, hum, wind = self.get_weather_info()
                f.write(f'{date}\n{avg}, {min}, {max}, {hum}, {wind}\n')
        return avg, min, max, hum, wind

    def get_data(self):
        URL = f'https://api.weatherapi.com/v1/history.json?key={self.api_key}&q={self.localization}&dt={self.date}'
        r = rq.get(URL)
        return r.json()

    def get_weather_info(self):
        r = self.data
        avg_temp = r['forecast']['forecastday'][0]['day']['avgtemp_c']
        min_temp = r['forecast']['forecastday'][0]['day']['mintemp_c']
        max_temp = r['forecast']['forecastday'][0]['day']['maxtemp_c']
        humidity = r['forecast']['forecastday'][0]['day']['avghumidity']
        wind = r['forecast']['forecastday'][0]['day']['maxwind_kph']
        return avg_temp, min_temp, max_temp, humidity, wind

    def __str__(self): # pozwala na printowanie obiektu pojedyńczo
        return f'{self.date}, {self.localization}'

    def __repr__(self): # pozwala na printowanie obiektu np w liście
        return f'{self.date}, {self.localization}'

    def __getitem__(self, key): # pozwala na odwoływanie się do obiektu jak do słownika
        return self.data[key]
    
    def __setitem__(self, key, value): # pozwala na zmienianie wartości w słowniku obiektu
        self.data[key] = value
        
api_key = sys.argv[1]
if len(sys.argv) >= 3:
    date = sys.argv[2]
else:
    date = str(dt.date.today())
localization = 'London'

w = Weather(api_key, date, localization)

avg, min, max, hum, wind = w.get_data_handler(date)

print(f'Day: {date}')
print(f'Avarage temperature: {avg}')
print(f'Minimum temperature: {min}')
print(f'Maximum temperature: {max}')
print(f'Humidity: {hum}%')
print(f'Maximum wind speed: {wind}km/h')

