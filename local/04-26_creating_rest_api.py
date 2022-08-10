#04-27_creating_a_rest_api.py

#currently only works in repl.it 
#see here https://replit.com/@matus1976/26-create-custom-api#main.py 

from flask import Flask, jsonify

#scrape the current rate from xrate
from bs4 import BeautifulSoup
import requests

def GetCurrency(input_currency, output_currency):
    """ gets the current currency exchange rate and returns the rate """
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    #print(url)
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup)
    raw_currency = soup.find("span", class_="ccOutputRslt").get_text()
    #print(raw_currency)

    raw_currency_length = len(raw_currency)
    #print(raw_currency_length)
    currency = (raw_currency[0:raw_currency_length-4])
    #print(repr(currency))
    currency = float(currency)
    #print(type(currency))
    rate = currency
    return rate


#GetCurrency("EUR", "AUD")

app = Flask(__name__)

@app.route('/')
def home():
  return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
  rate = GetCurrency(in_cur, out_cur)
  result_dictionary= {'input_currency':in_cur, 'output_currency':out_cur, 'rate':rate}
  return jsonify(result_dictionary)
  

app.run(host='0.0.0.0')

