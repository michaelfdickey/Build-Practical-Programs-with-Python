
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\Users\\Matus1976\\Downloads\\chromedriver_win32\\chromedriver.exe')

def get_driver():
  
  options = webdriver.ChromeOptions()       # Set options to make browsing easier:
  options.add_argument("disable-infobars")  # on your browser you have info bars, may interfere with script, so this disables it
  options.add_argument("start-maximized")   # starts the browser as maximized
  options.add_argument("disable-dev-shm-usage")         # disable some issues often encountered on linux boxes
  options.add_argument("no-sandbox")        # give program greater privs on that web page script will scrape
  # this experiemental option helps selenium avoid detection from the browser when websites try to detect scripts
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_argument("executable_path='/home/runner/Scrape-Simple-Text-with-Selenium'")
  driver = webdriver.Chrome(service=service, options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def clean_text(text):
    """ extract only the tempaerature from the text """
    output = float(text.split(": ")[1])             # splits at the ': '
    return output

def main():
  # first lesson, just get the temperature from the website
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)





print(main())
