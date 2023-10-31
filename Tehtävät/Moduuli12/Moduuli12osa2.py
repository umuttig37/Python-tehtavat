import requests

apiKey ='39ea54bc5640a2f8bfe46fea0ea6e1e8'

kaupunki = input('Give city: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={apiKey}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    temperature = int(temp - 273.15)
    print('temperature: ' + str(temperature) + "°C")
    print(f'Description: {desc}')

else:
    print('Tapahtui virhe datan haussa')
