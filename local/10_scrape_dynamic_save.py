from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from datetime import datetime


service = Service('C:\\Users\\Matus1976\\Downloads\\chromedriver_win32\\chromedriver.exe')


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
  options.add_argument("executable_path='/home/runner/Scrape-Simple-Text-with-Selenium'")
  driver = webdriver.Chrome(service=service, options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver


def clean_text(text):
  """ extract only the temperature from the text """
  output = float(text.split(": ")[1])
  #splits it at the `: `, gets 2nd index, and converts to float
  return output


def get_current_temp(driver): 
  # get text with world temp
  time.sleep(3)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  current_temp = clean_text(element.text)
  print(" current temp is: ", current_temp)
  return current_temp


def write_file(temp, file_name):
  print(" file_name is: ", repr(file_name))
  file = open(file_name, 'w')
  file.write(str(temp))
  file.close


def get_filename():
  # get date
  today = date.today()
  print("today is: ", today)

  # get time
  now = datetime.now()
  str_time = now.strftime("%H-%M-%S")
  print("str_time: ", str_time)

  # combine date and time
  file_name = str(today) + "." + str(str_time) + ".txt"
  print("file_name: ", file_name)

  return file_name


driver = get_driver()

def main(driver):
  temp = get_current_temp(driver)
  file_name = get_filename()
  write_file(temp, file_name)

index = 0

while index < 5:
  main(driver)
  time.sleep(2)
  index += 1
