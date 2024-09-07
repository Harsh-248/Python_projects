# a-z in small letter, 0-9 there in a email, ". _ @ "should come once in the email address.
# these are the conditions for this program using regex
import re
email_condition = "^[a-z]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input ('Enter your email :')

if re.search(email_condition, user_email):
    print('Valid Email')
else :
    print('Invalid Email')