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



