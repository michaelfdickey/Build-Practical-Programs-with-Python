import requests
import json 

url = 'https://api.languagetool.org/v2/check'

# create data as dictionary to pass for language check:
data = {
    'text':'Tis is a nixe day!',
    'language':'auto'
    }

response = requests.post(url, data)       #using post now, before we used get

print(response.text)

# check the type of the output
print(type(response.text))

result = json.loads(response.text)
print(result)