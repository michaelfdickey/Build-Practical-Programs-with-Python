# Requires getting a new newsapi from https://newsapi.org and replacing the api key in the url below 
# manually copy and paste the request url into browser to see error messages, e.g.:
# https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39
# {"status":"error","code":"parameterInvalid","message":"You are trying to request results too far in the past. Your plan permits you to request articles as far back as 2023-02-01, but you have requested 2022-06-27. You may need to upgrade to a paid plan."}



import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39')

# this ^ url has parameters that are used to filter the results and can be modified, e.g. to get united states news instead of 'stock market':
# https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39

content = r.json()

# print(content)

print(type(content))
print('dictionary len is: ', len(content))
print('status is: ', content['status'])
print('total results is: ', content['totalResults'])

# get the title of the first article
print(content['articles'][0]['title'])

# https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39

"""
## United States News
r = requests.get('https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39')
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
r = requests.get('https://newsapi.org/v2/everything?qInTitle=spacex&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39')
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
r = requests.get('https://newsapi.org/v2/everything?qInTitle=nuclear%20fusion&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39')
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