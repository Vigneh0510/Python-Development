#now we start the  task
import re
def email_checker(email):
    pattern=r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.]+\.(com|in|org)$'
    if re.match(pattern,email):
        if ".." in email:
            return False
        else:
            return True
    return False
email="hello+-123@gmail.com"
print(email_checker(email))
#code completed
#now check false or incorrect email
#task completed