import re
import string
def password_Strength(s):
    return (
        len(s)>=8 and
        re.search(r'[A-Z]',s) is not None and
        re.search(r'[a-z]',s) is not None and
        re.search(r'\d',s) is not None and
        re.search(r'\w',s) is not None 
    )
s=input()
a=password_Strength(s)
if a==True:
    print("Password is Strength")
else:
    print("Password is Weak")


#Another Approach

def password1_Strength(s):
     if len(s)<8:
         return False
     upper=any(char.isupper() for char in s)
     lower=any(char.islower() for char in s)
     digit=any(char.isdigit() for char in s)
     si=set(string.punctuation)
     symbol=any(char in si for char in s)
     return upper and lower and digit and symbol
s=input()
a=password1_Strength(s)
if a==True:
    print("Password is Strength")
else:
    print("Password is Weak")
