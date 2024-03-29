# Section 2

# 5. scraping text with selenium



scaping sample text from automated.pythonanywhere.com

install selenium

in repl:

![image-20220612130937775](image-20220612130937775.png)

need to do an update to settings if you didn't fork author's repl. show hidden files:

![image-20220612131302881](image-20220612131302881.png)

open `replit.nix`

add two new lines:

```
pkgs.chromium
pkgs.chromedriver
```

![image-20220612131453651](image-20220612131453651.png)

close file then hide those files again

now you can go ahead and import selenium in your main.py

```
from selenium import webdriver
```

then create a driver variable

```
driver = web.driver.Chrome()
```

Add options for selenium and put it in a function `get_driver`

```
from selenium import webdriver

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
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome()
  driver.get("https://automated.pythonanywhere.com/")
  return driver
```

create new function `main` to get the elements

```
def main():
  driver = get_driver()
  element = driver.find_element_by_xpath("")
```

the `find_element_by_xpath` will identify and return that specific text identified by `xpath`

to get the xpath for that web element, open inspect in the browser, then click copy and copy xpath:

![image-20220612132626009](image-20220612132626009.png)

result:

`/html/body/div[1]/div/h1[1]`

error:

> ", line 81, in start
>     raise WebDriverException(
> selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://chromedriver.chromium.org/home

response from instructor

> [Ardit](https://www.udemy.com/user/adiune/) — Instructor
>
> 0 upvotes0
>
> 
>
> 15 hours ago
>
> Hi Michael, the solution is to not create a new Repl, but fork my Repl instead. You can find my Repl links attached as lecture resources. For your convenience, below is link to the Repl which contains the complete code for the lecture "Scraping Simple Text with Selenium":
>
> https://replit.com/@ArditS/Scrape-Simple-Text-with-Selenium-done

working code of mine in instructors forked replit (no PATH error)

```

from selenium import webdriver


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
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  
  options.add_argument("disable-blink-features=AutomationControlled")

  options.add_argument("executable_path='/home/runner/Scrape-Simple-Text-with-Selenium'")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver


def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  return element.text

print(main())
```



# 6) scraping from your local IDE



>   File "06_scrape_with_selenium.py", line 2, in <module>
>     from selenium import webdriver
> ModuleNotFoundError: No module named 'selenium'

run

```
pip install selenium
```

now you get local error:

```
    self.service.start()
  File "C:\ProgramData\Anaconda3\lib\site-packages\selenium\webdriver\common\service.py", line 81, in start
    raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://chromedriver.chromium.org/home

```

go to https://chromedriver.chromium.org/downloads

find out what version of chrome you have: 

search what is my browser and go to https://www.whatismybrowser.com/

add:

```
from selenium.webdriver.chrome.service import Service

#location of the chromedriver.exe you just downloaded:
service = Service('C:\\Users\\Matus1976\\Downloads\\chromedriver_win32\\chromedriver.exe') 
```

change

```
  driver = webdriver.Chrome(options=options)
```

to

```
  driver = webdriver.Chrome(service=service, options=options)
```

![image-20220613173508299](image-20220613173508299.png)

# 7) scraping dynamic value

if you right click and inspect this changing element you get only `/div` as the xpath, so sometimes this doesn't work

/div

![image-20220613174604224](image-20220613174604224.png)

the previous xpath was:

```
"/html/body/div[1]/div/h1[1]"
```

/html means this document

/body isthe main tag and contains the div tag you grabbed

there are two `/div` under body though

![image-20220613174745637](image-20220613174745637.png)

so you were getting the first instace of div under body with `html/body/div[1]` and under that the first div and first header with `/div/h1[1]` 

so now you want the 2nd header

![image-20220613175131559](image-20220613175131559.png)

you can also right click and get full xpath in chrome inspect

sometimes

so now you are using:

```
def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return element.text
```

but the returned text doesn't have the value:

```
Average World Temperature Now:
 
```

this is because the value doens't appear for a few seconds

so add a pause

```
import time

...

def main():
  driver = get_driver()
  time.sleep(2)          #pause for 2 seconds
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return element.text
```

result

![image-20220613175521819](image-20220613175521819.png)

Let's make a new function that grabs just that number:

use split

```
Average World Temperature Now: 28
 "average : 22".split(": ")
['average ', '22']

```

new program

```

from selenium import webdriver
import time


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
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  
  options.add_argument("disable-blink-features=AutomationControlled")

  options.add_argument("executable_path='/home/runner/Scrape-Simple-Text-with-Selenium'")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def clean_text(text):
  """ extract only the temperature from the text """
  output = float(text.split(": ")[1])
  #splits it at the `: `, gets 2nd index, and converts to float
  return output


def main():
  driver = get_driver()
  time.sleep(2)          #pause for 2 seconds
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)
  

print(main())
```

works

![image-20220613180015328](image-20220613180015328.png)

next get this working  locally

# 8) Automate Login Process

your script will login to this form https://automated.pythonanywhere.com/login/

script logins and then clicks on the home page

script will need the url https://automated.pythonanywhere.com/login/

username is automated

pw is automatedautomated

updated website

```
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver
```

update element

we don't need to use xpath, you can use the id if it's there

![image-20220614185124743](image-20220614185124743.png)

![image-20220614185136617](image-20220614185136617.png)

id = "id_username" whenever that's present you can use it

```
def main():
  driver = get_drvier()
  element = driver.find_element(by="id", value="id_username")
  return element.text
```

also we want to send keys

```
def main():
  driver = get_drvier()
  element = driver.find_element(by="id", value="id_username").send_keys("automated")
  return element.text
```

don't need to assign it or return anything either

```
def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  # return element.text
```

works

```
def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated")
```

works, but add a sleep to slow things down, 

```
import time

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated")
```

and send a RETURN

```
import selenium.webdriver.common.keys import Keys

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
```

so the whole program now looks like

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver

def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)

print(main())
```

last you can add this to display your url to know it worked

```
def main():
  driver = get_drvier()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  print(driver.current_url) #<---

```



![image-20220614190311042](image-20220614190311042.png)

Next we want to click on the Home button

![image-20220614191703932](images/image-20220614191703932.png)

we want to use the xpath since it has no id

![image-20220614191344898](images/image-20220614191344898.png)

`/html/body/nav/div/a`

find that element and then click on it

```
def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  print(driver.current_url)
```

works

```
https://automated.pythonanywhere.com/
None
```

next we will extract the world temp value from the page after we have logged in

# 9) Exercise - Login, Click, Scrape

date-time

```
>>> from datetime import date
>>> today = date.today()
>>> today
datetime.date(2022, 6, 18)
>>> print(today)
2022-06-18
>>> 
KeyboardInterrupt
>>> 
```



```
>>> from datetime import datetime
>>> now = datetime.now()
>>> now
datetime.datetime(2022, 6, 18, 2, 30, 41, 997621)
>>> print(now)
2022-06-18 02:30:41.997621
>>> time_string = now.strftime("%H:%M:%S")
>>> time_string
'02:30:41'
>>> print(time_string)
02:30:41
```

# 10) scrape dynamic value and output text file

on replit

```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from datetime import datetime 

def get_driver():
  # Set options to make browsing easier
  print("  running get_driver")
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def clean_text(text):
  """ extract only the temperature from the text """
  print("  running clean_text")
  output = float(text.split(": ")[1])
  #splits it at the `: `, gets 2nd index, and converts to float
  #print(output)
  return output


def get_current_temp(driver):
  print("  running get_current_temp")
  """
  # login
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  """

  """
  # open web page 
  driver = get_driver()
  """
  
  # scrape text
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  current_temp = clean_text(element.text)
  print("  ", current_temp)
  return current_temp

def write_file(current_temp,file_name):
  print("  running write_file")
  file = open(file_name, 'w')
  #print(file)
  file.write(current_temp)
  file.close()
  
def date_time_name():
  print("  running date_time_name")
  # get date
  today = date.today()
  print("   date is: ", today)

  # get time
  now = datetime.now()
  str_time = now.strftime("%H:%M:%S")
  print("   time is: ", str_time)

  # concatonate datetime 
  file_name = str(today) + "." + str(str_time)
  print("   filename is: ", file_name)

  # return string for filename 
  ## 2022-2-10.14-33-59.txt
  return file_name
  
def main(driver):
  print(" running main")
  current_temp = str(get_current_temp(driver))
  print("current temp is: ", current_temp)
  file_name = date_time_name()
  write_file(current_temp,file_name)


driver = get_driver()

keep_going = True
while keep_going == True:
  main(driver)
  time.sleep(2)
```

error message

```
Matus1976@DESKTOP-98E2DP4 MINGW64 /d/Files - Google Drive/Files - New Merged/MFD Personal/Programming/python/Udemy/Build-Practical-Programs-with-Python (main)
$ python ./local/10_scrape_dynamic_save.py
 current temp is:  28.0
today is:  2022-06-18
str_time:  15:57:37
file_name:  2022-06-18.15:57:37.txt
 file_name is:  '2022-06-18.15:57:37.txt'
Traceback (most recent call last):
  File "./local/10_scrape_dynamic_save.py", line 79, in <module>
    main()
  File "./local/10_scrape_dynamic_save.py", line 76, in main
    write_file(temp, file_name)
  File "./local/10_scrape_dynamic_save.py", line 52, in write_file
    file = open(file_name, 'w')
OSError: [Errno 22] Invalid argument: '2022-06-18.15:57:37.txt'

```

windows doesn't like : in filenames

change to

```
  # get time
  now = datetime.now()
  str_time = now.strftime("%H-%M-%S")
  print("str_time: ", str_time)
```

# 12) deleting all text files

```
rm *.txt
```

# 13) reviewing solution to scrape dynamic value and save as text file

my solution is above

notes from instructor:

gets driver for home page:

```
def get_driver():
  # Set options to make browsing easier
  print("  running get_driver")
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver
```

move the element into a loop:

strftime - generates a useful string from the datetime object 

using datetime

```
from datetime import datetime
datetime.now()
datetime.datetime(2022, 6, 19, 18, 17, 16, 170593)
datetime.now().strftime("%Y")
'2022'
datetime.now().strftime("%Y-%M")
'2022-17'
datetime.now().strftime("%Y-%M-%D")
'2022-17-06/19/22'
datetime.now().strftime("%Y-%M-%d")
'2022-18-19'

```

full string

```
datetime.now().strftime("%Y-%M-%d.%H-%M-%S")
'2022-18-19.18-18-49'
```

# 14) access online retailer

titan22.com

sad.monday.funky

//*[@id="shopify-section-header"]/div[1]/div/div[3]/a[2]/span/svg - nope

//*[@id="shopify-section-header"]/div[1]/div/div[3]/a[2]/span/svg - 

/html/body/header/div[1]/div[1]/div/div[3]/a[2]/span/svg - copy full xpath

![image-20220619114352371](images/image-20220619114352371.png)

//*[@id="shopify-section-header"]/div[1]/div/div[3]/a[2]/span/svg

/html/body/header/div[1]/div[1]/div/div[3]/a[2]/span/svg

just land right on the login page, login, then click contact us

`/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a`

code update - `$ git commit -m "14-15 solution accessing an online retailer"`

# 16) Download stock data for any company for any date

download historical stock data via python

https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1655683200&interval=1wk&events=history&includeAdjustedClose=true

![image-20220620182201324](images/image-20220620182201324.png)

example url

```
https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1655683200&interval=1d&events=history&includeAdjustedClose=true
```

get started

to download files with python, use the requests library

```
import requests

url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1655683200&interval=1d&events=history&includeAdjustedClose=true"

content = requests.get(url).content     #this is a method that expects a url 
print(content)
```

content is a byte object

```
$ python local/02-16_download_stock_data.py
b'Forbidden'
```

it's forbidden, we need the headers

yahoo finance doens't allow scraping scripts to download files

you can skip this by providing headers to impersonate a browser

```
import requests

url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1655683200&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

content = requests.get(url, headers=headers).content     #this is a method that expects a url 

print(content)
```

works...

```
Matus1976@DESKTOP-98E2DP4 MINGW64 /d/Files - Google Drive/Files - New Merged/MFD Personal/Programming/python/udemy/Build-Practical-Programs-with-Python (main)
$ python local/02-16_download_stock_data.py
b'Date,Open,High,Low,Close,Adj Close,Volume\n1980-12-12,0.128348,0.128906,0.128348,0.128348,0.100178,469033600\n1980-12-15,0.122210,0.122210,0.121652,0.121652,0.094952,175884800\n1980-12-16,0.113281,0.113281,0.112723,0.112723,0.087983,105728000\n1980-12-17,0.115513,0.116071,0.115513,0.115513,0.090160,86441600\n1980-1
...etc
```

but now we need to write these to a file on disk

using requests.get().content grabs things as binaries, so for writing the file use `wb` instead of `w`

```
content = requests.get(url, headers=headers).content     
with open('aapl.csv', 'wb')
```

then write the file

```
with open('aapl.csv', 'wb') as file:
    file.write(content)
```

let's further improve the script by letting the user choose the period and the ticker symbol

```
from_date = input('Enter start from date in format (YYYY/MM/DD): ')
to_date = input('Enter end date in YYYY/MM/DD format:' )
```

convert human date format to epoch

```
>>> from_date = '2022/1/2'
>>> print(from_date)
2022/1/2
```

then convert to datetime object with a specific format

```
>>> from datetime import datetime
>>> d = datetime.strptime(from_date, '%Y/%m/%d')
>>> d
datetime.datetime(2022, 1, 2, 0, 0)
```

then convert `d` to epoch time with `import time`

```
>>> import time
>>> epoch = time.mktime(d.timetuple())
>>> epoch
1641110400.0
>>>
```

so in your program it will look like

```
import requests
from datetime import datetime
import time

from_date = input('Enter start from date in format (YYYY/MM/DD): ')
to_date = input('Enter end date in YYYY/MM/DD format:' )

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = time.mktime(from_datetime.timetuple())
to_epoch = time.mktime(to_datetime.timetuple())
```

then add these into your yahoo finance url, adding `from_epoch` and `to_epoch`:

```
url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
```

run the program, you'll get

```
b'{"finance":{"result":null,"error":{"code":"Internal Server Error","description":"The template variable \'from_epoch\' has no value"}}}'

```

this is because our print(content) and our values our epoch is in the float format

```
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))
```

or it needs the `f` in front of the url

```
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"
```

`f` makes it an fstring and allows you to use the {variable} format 

# 17) Scrape Real-Time currency Rate with Beautiful Soup

learn how to use beautiful soup - a great webscraping library

selenium is more targeted toward browser automations, logging in and out, clicking on buttons, scrape values, etc

beautiful soup, if you want to just extract data you don't have to open the browser.  Selenium is kind of a hybrid between web scraping and scripting

beautiful soup is just a library taht directly accesses websites. 

start with x-rates.com

string for conversion in x-rates currency converter

https://www.x-rates.com/calculator/?from=EUR&to=INR&amount=1

![image-20220627165818450](images/image-20220627165818450.png)

1. install beautiful soup

   ```
   pip install beautifulsoup4
   ```

   ```
   from bs4 import BeautifulSoup
   ```

2. example program

   ```
   from bs4 import BeautifulSoup
   
   def GetCurrency(input_currency, output_currency):
       url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
       print(url)
   
   GetCurrency("USD", "EUR")
   ```

   produces useable URL

3. now with BeautifulSoup you want to get the source code of the web page

   ![image-20220627170907727](images/image-20220627170907727.png)

It'll be HTML / CSS / JavaScript

![image-20220627170954859](images/image-20220627170954859.png)

you want to access all that code from python

using `requests`

```
pip install requests
```

```
import requests
```

you will use requests to get the contents:

```
content = requests.get(url).text
print(content)
# prints out HTML sourcecode
```

current program now:

```
from bs4 import BeautifulSoup
import requests

def GetCurrency(input_currency, output_currency):
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    print(url)
    print(content)

GetCurrency("USD", "EUR")
```

out of all that source code we only want 

![image-20220627171917549](images/image-20220627171917549.png)

you can search for it

![image-20220627171951740](images/image-20220627171951740.png)

or inspect element

![image-20220627172010576](images/image-20220627172010576.png)

![image-20220627172037495](images/image-20220627172037495.png)

![image-20220627172055042](images/image-20220627172055042.png)

when need to parse that source code

that's where beautiful soup is great

it understands HTML structure, knowledge of elements / div tags / nested elements

use the html parser to look through the conent:

```
soup = BeautifulSoup(content, 'html.parser')
```

if you print out soup here, it prints out basically the same thing. 

code looks like this now:

```
from bs4 import BeautifulSoup
import requests

def GetCurrency(input_currency, output_currency):
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    print(url)
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    print(soup)

GetCurrency("USD", "EUR")
```

We want this

![image-20220627172406521](images/image-20220627172406521.png)

```
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

GetCurrency("USD", "EUR")
```

run that, you get

```
D:\Files - Google Drive\Files - New Merged\MFD Personal\Programming\python\Udemy\Build-Practical-Programs-with-Python\local>python 02-17_scrape-real-time-currency.py
https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1
0.944916 EUR
```

let's clean it up and just get that float. we want to remove the last four characters

```
from bs4 import BeautifulSoup
import requests

def GetCurrency(input_currency, output_currency):
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

GetCurrency("EUR", "INR")
```

complete program

```
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
```



