# 4 Building and using APIs

In this section, you will access various APIs with Python and even create your own APIs

 get a free News API following the steps below:

\1. You go to https://newsapi.org/

Representation State Transfer Application Process Interface

an API is a way for two applications to communicate, like HTML web pages are for people to communicate clearly with each oter, API is for apps to communicate clearly with each other

json is the usual format served by APIs

use the `requests` module

```
import requests
r = requests.get()
```

with the url, it will print the unformatted json

```
import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')

content = r.json()

print(content)
```

![image-20220710101832200](images/image-20220710101832200.png)

you can get individual keys with 

it's actually a dictionary, but only 3 keys

```
# print(content)

print(type(content))
print(len(content))
```

```
$ python local/04-21_rest_api.py
<class 'dict'>
3
```

getting individual keys

```
print(type(content))
print('dictionary len is: ', len(content))
print('status is: ', content['status'])
print('total results is: ', content['totalResults'])
```

```
$ python local/04-21_rest_api.py
<class 'dict'>
dictionary len is:  3
status is:  ok
total results is:  181

```

get the title of the first article

```
# get the title of the first article
print(content['articles'][0]['title'])

```

```
$ python local/04-21_rest_api.py
<class 'dict'>
dictionary len is:  3
status is:  ok
total results is:  181
Sterling rises against dollar as stock market rallies - Reuters.com

```



your python application is communicating through url parameters

```
r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')

# this ^ url has parameters that are used to filter the results and can be modified, e.g. to get united states news instead of 'stock market':
# https://newsapi.org/v2/everything?qInTitle=united%20states&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c

content = r.json()
```

r is a request object

if you apply the .json() method to that object, that's what converts it to a dictionary

print all the article titles:

```
# print all the article titles 
articles = content['articles']
print(type(articles))

for article in articles:
    print(article['title'])
```

additional article info:

```
for article in articles:
    print("> Title: ", article['title'])
    print("  Description: ", article['description'])
    print("  URL: ", article['url'])
```

use `f'string'` to construct string urls:

```
# we want the user to define the search parameters
def get_news(topic, from_date, to_date, language=en, api_key='890603a55bfa47048e4490069ebee18c'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'

```

22 - 12:00 min

## 23 - News API getting top headlines for any country

## 24 - Weather Forecast API

![image-20220719220317471](images/image-20220719220317471.png)

appends weather forecast to a text file output so you're using 'a' for append instead of 'w' 

openweathermap.org

![image-20220719221706917](images/image-20220719221706917.png)



```
import requests

def get_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Kent,wa,us&APPID=<<API KEY>>&units=imperial'
    request_result = requests.get(url)
    content = request_result.json()
    #print(content)
    return(content)

def get_forecast():
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=Kent,wa,us&cnt=8&APPID=<<API KEY>>&units=imperial'
    request_result = requests.get(url)
    content = request_result.json()
    #print(content)
    return(content)

weather_content = get_weather()
forecast = get_forecast()

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

```



## 26 Create your own currency rate REST API

