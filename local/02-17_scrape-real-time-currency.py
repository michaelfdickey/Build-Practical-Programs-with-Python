from bs4 import BeautifulSoup
import requests

def GetCurrency(input_currency, output_currency):
    """ gets the current currency exchange rate and returns the rate """
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    print(url)
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup)
    raw_currency = soup.find("span", class_="ccOutputRslt").get_text()
    print(raw_currency)

    raw_currency_length = len(raw_currency)
    #print(raw_currency_length)
    currency = (raw_currency[0:raw_currency_length-4])
    #print(repr(currency))
    currency = float(currency)
    #print(type(currency))
    rate = currency
    return rate


GetCurrency("EUR", "AUD")

