# Automating Emails in Python

## 44) sending a single email with python

to copy a reply environment

if you enter the URL with the #main.py you can fork the repl to have the same environment

```
replit.com/@arditS/Send-Single-Email#main.py
```

```
replit.com/@arditS/Send-Single-Email  #forks repl
```

```
replit.com/@arditS/Send-Single-Email-done		#copy of completed program
```

emails sent through email clients like gmail or outlook

these app use the SMTP protocol (simple mail transfer protocol)

to use SMTP use a python SMTP package, `yagmail`

```
import yagmail
```

set vars for email info:

```
sender = 'mfd.oldphones@gmail.con'
receiver = 'matus1976@gmail.com'
subject = 'Test email sent from python'
contents = """
here is the content of the email!
Hi!
"""
```

\# password

not a good idea to store password in plain text, use a secret. in repl create a secret called password and set the value to your password. this actually needs to be a "gmail app password"

## create gmail app password

- go to manage your google account
- click security
- turn on 2 step verification
- go back to security
- click app passwords

Make sure you have no typos in username and password! like `.con` 

working program:

```
import yagmail
import os

# prepare variables for email information

sender = 'mfd.oldphones@gmail.com'
receiver = 'matus1976@gmail.com'
subject = 'Test email sent from python'
contents = """
here is the content of the email!
Hi!
"""

# password
# not a good idea to store password in plain text, use a secret
# in repl create a secret called password and set the value to your password
# this actually needs to be a "gmail app password"

# ask for the password
password = input('Enter your password: ')
print('password is: ', repr(password))
      
# for repl get the password 
#password = os.getenv('PASSWORD')

# direct input
# password = ''

yag = yagmail.SMTP(sender,password )       # create an instance of the SMTP object isntance using the SMTP class
yag.send(to=receiver, subject=subject, contents=contents)

print("email sent")

```









