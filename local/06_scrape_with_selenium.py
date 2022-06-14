
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\Matus1976\\Downloads\\chromedriver_win32\\chromedriver.exe')

def get_driver():
  ## Set options to make browsing easier:
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
  driver.get("https://automated.pythonanywhere.com/")
  return driver


def main():
  driver = get_driver()
  element = driver.find_element(
      by="xpath", value="/html/body/div[1]/div/h1[1]")
  return element.text


print(main())
