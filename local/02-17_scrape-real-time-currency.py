from bs4 import BeautifulSoup
import requests

def GetCurrency(input_currency, output_currency):
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    print(url)
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup)
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    print(currency)

GetCurrency("EUR", "INR")

