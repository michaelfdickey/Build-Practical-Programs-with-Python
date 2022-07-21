# City Time Temperature Condition

import requests

# we want the user to define the search parameters

def get_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Kent,wa,us&APPID=b039ffaa32e86ce1bb6086256bbe5f90&units=imperial'
    request_result = requests.get(url)
    content = request_result.json()
    #print(content)
    return(content)

def get_forecast():
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=Kent,wa,us&cnt=8&APPID=b039ffaa32e86ce1bb6086256bbe5f90&units=imperial'
    request_result = requests.get(url)
    content = request_result.json()
    #print(content)
    return(content)

weather_content = get_weather()

#print(weather_content['coord'])
#print(weather_content['weather'])
#print(weather_content['base'])
#print(weather_content['main']['temp'])          #current temp
#print(weather_content['main']['temp_min'])      #min temp
#print(weather_content['main']['temp_max'])      #max temp
#print(weather_content['name'])      #pressure    

forecast = get_forecast()

"""
print(forecast['list'][0]['main']['temp'])
print(forecast['list'][1]['main']['temp'])
print(forecast['list'][2]['main']['temp'])
print(forecast['list'][3]['main']['temp'])
print(forecast['list'][4]['main']['temp'])
print(forecast['list'][5]['main']['temp'])
print(forecast['list'][6]['main']['temp'])
print(forecast['list'][7]['main']['temp'])
"""

todays_temps = []

for n in range(8):
    #print(n, forecast['list'][n]['main']['temp'])
    todays_temps.append(forecast['list'][n]['main']['temp'])

#print(forecast['list'][0]['weather'][0]['description'])

todays_weather = []

for n in range(8):
    #print(n, forecast['list'][n]['weather'][0]['description'])
    todays_weather.append(forecast['list'][n]['weather'][0]['description'])

# display the weather for the day 
print(" ")
print("The current weather for ", (weather_content['name']), "is: ", weather_content['weather']
      [0]['description'], " and a temp of ", weather_content['main']['temp'], " degrees.")
print(" ")
print("todays_temps: ", todays_temps)
print("todays_weather: ", todays_weather)
print(" ")


"""
{
'coord': {'lon': -122.2348, 'lat': 47.3809}, 
'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
'base': 'stations',
'main': {'temp': 85.24, 'feels_like': 85.39, 'temp_min': 77.29, 'temp_max': 90.27, 'pressure': 1016, 'humidity': 44}, 
'visibility': 10000, 
'wind': {'speed': 4, 'deg': 219, 'gust': 8.01}, 
'clouds': {'all': 0}, 
'dt': 1658364795, 
'sys': {'type': 2, 'id': 2034316, 'country': 'US', 'sunrise': 1658320372, 'sunset': 1658375842}, 
'timezone': -25200, 
'id': 5799625, 
'name': 'Kent', 
'cod': 200}



"""



"""
def get_news(topic, from_date, to_date, language='en', api_key='890603a55bfa47048e4490069ebee18c'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    request_result = requests.get(url)
    content = request_result.json()
    articles = content['articles']
    for article in articles:
        print("> ", article['title'])


topic_search_result = get_news(
    topic='covid china', from_date='2022-6-27', to_date='2022-6-28')
#print(topic_search_result)
"""