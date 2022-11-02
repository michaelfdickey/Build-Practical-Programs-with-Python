import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')

# this ^ url has parameters that are used to filter the results and can be modified, e.g. to get united states news instead of 'stock market':
# https://newsapi.org/v2/everything?qInTitle=united%20states&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c

content = r.json()

# print(content)

print(type(content))
print('dictionary len is: ', len(content))
print('status is: ', content['status'])
print('total results is: ', content['totalResults'])

# get the title of the first article
print(content['articles'][0]['title'])

# https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c

"""
## United States News
r = requests.get('https://newsapi.org/v2/everything?qInTitle=united%20states&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print('dictionary len is: ', len(content))
print('status is: ', content['status'])
print('total results is: ', content['totalResults'])
print(content['articles'][0]['title'])
print('len of articles dict: ', len(content['articles']))

# getting the title of all the articles
for i in range(len(content['articles'])):
    print('> ',content['articles'][i]['title'])
    #print('\n') # print a new line
"""

## SpaceX News
r = requests.get('https://newsapi.org/v2/everything?qInTitle=spacex&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print('dictionary len is: ', len(content))
print('status is: ', content['status'])
print('total results is: ', content['totalResults'])
print(content['articles'][0]['title'])
print('len of articles dict: ', len(content['articles']))

# getting the title of all the articles
for i in range(len(content['articles'])):
    print('> ', content['articles'][i]['title'])
    #print('\n') # print a new line


## Nuclear Energy News
r = requests.get('https://newsapi.org/v2/everything?qInTitle=nuclear%20fusion&from=2022-6-27&to=2022-6-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print('dictionary len is: ', len(content))
print('status is: ', content['status'])
print('total results is: ', content['totalResults'])
print(content['articles'][0]['title'])
print('len of articles dict: ', len(content['articles']))

# getting the title of all the articles
for i in range(len(content['articles'])):
    print('> ', content['articles'][i]['title'])
    #print('\n') # print a new line

# emails you text news service daily for specific topics back from specific date. 