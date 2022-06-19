from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


service = Service(
    'C:\\Users\\Matus1976\\Downloads\\chromedriver_win32\\chromedriver.exe')


def get_driver():
  # Set options to make browsing easier:
  options = webdriver.ChromeOptions()
  # on your browser you have info bars, may interfere with script, so this disables it
  options.add_argument("disable-infobars")
  # starts the browser as maximized
  options.add_argument("start-maximized")
  # disable some issues often encountered on linux boxes
  options.add_argument("disable-dev-shm-usage")
  # give program greater privs on that web page script will scrape
  options.add_argument("no-sandbox")
  # this experiemental option helps selenium avoid detection from the browser when websites try to detect scripts
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_argument(
      "executable_path='/home/runner/Scrape-Simple-Text-with-Selenium'")
  driver = webdriver.Chrome(service=service, options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver


def login(driver):
  # login
  driver.find_element(by="id", value="CustomerEmail").send_keys("mfd.oldphones@gmail.com")
  time.sleep(2)
  
  driver.find_element(by="id", value="CustomerPassword").send_keys("sad.monday.funky" + Keys.RETURN)
  time.sleep(2)
  
  #click on home after logged in
  driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
  time.sleep(2)

def main():
  driver = get_driver()
  time.sleep(3)
  login(driver)
  print("done")

main()