import requests


"""
r = requests.get('https://newsapi.org/v2/everything?qInTitle=covid%20china&from=2023-2-15&to=2023-2-28&sortBy=popularity&language=en&apiKey=1f14bd75e6bc496c980923a36b6add39')

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

# print all the article titles 
articles = content['articles']
print(type(articles))

#for article in articles:
#    print(article['title'])

for article in articles:
    print("> Title: ", article['title'])
    print("  Description: ", article['description'])
    print("  URL: ", article['url'])
"""


# we want the user to define the search parameters
def get_news(topic, from_date, to_date, language='en', api_key='1f14bd75e6bc496c980923a36b6add39'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    request_result = requests.get(url)
    content = request_result.json()
    articles = content['articles']
    for article in articles:
        print("> ", article['title'])   
        
topic_search_result = get_news(topic='covid china', from_date='2023-2-15', to_date='2023-2-28')
#print(topic_search_result)




