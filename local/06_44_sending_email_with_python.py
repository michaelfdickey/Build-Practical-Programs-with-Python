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
