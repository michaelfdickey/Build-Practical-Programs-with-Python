
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(
    'C:\\Users\\Matus1976\\Downloads\\chromedriver_win32\\chromedriver.exe')


def get_driver():
  options = webdriver.ChromeOptions()                   # Set options to make browsing easier:
  options.add_argument("disable-infobars")              # on your browser you have info bars, may interfere with script, so this disables it
  options.add_argument("start-maximized")               # starts the browser as maximized
  options.add_argument("disable-dev-shm-usage")         # disable some issues often encountered on linux boxes
  options.add_argument("no-sandbox")                    # give program greater privs on that web page script will scrape
  # this experiemental option helps selenium avoid detection from the browser when websites try to detect scripts
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_argument("executable_path='/home/runner/Scrape-Simple-Text-with-Selenium'")
  driver = webdriver.Chrome(service=service, options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver


def clean_text(text):
  """ extract only the temperature from the text """
  output = float(text.split(": ")[1])
  #splits it at the `: `, gets 2nd index, and converts to float
  return output


def main():
  # login
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)

  # click on home after logged in
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(2)

  # get text with world temp
  time.sleep(3)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)
  
  
  # this will print the url of the page you are on to confirm you logged in
  print(driver.current_url)


print(main())
