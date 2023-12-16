import re

text='''Txt File:
Mr. Anderson
Ms. Thareja
Mrs. Morris
Mr. Roy
Ms. Gandhi
Mrs. Modi

https://www.google.com
http://www.udemy.com
www.udacity.com
https://www.stackoverflow.com
http://www.djsce.ac.in
https://plus.google.com

rishit.grover@gmail.com
kapeesh.grover@yahoo.co.in
abhishek.shah@gmail.com
shahp98@gmail.com
demo_user@gmail.com
rolflmoa@yahoo.co.in

27777647
233*333*88
455-78-888
022-240-93836
02642*221*381
'''

# names=re.findall(r'(?:Mr\.|Ms\.|Mrs\.)\s[A-Za-z]+\b',text)
# print(names)

# emails=re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z]+\.com|[a-zA-Z0-9._]+@[a-zA-Z]+\.co.in',text)
# print(emails)

# emails=re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z]+\.(?:com|co\.in)',text)
# print(emails)

# emails=re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-z.]+',text)
# print(emails)

# numbers=re.findall(r'[0-9*-]{5,}',text)
# print(numbers)

# email=re.findall(r'[a-zA-Z0-9_\-\.]+[@][a-z]+\.[a-z.]+',text)
# print(email)

# website=re.findall(r'[a-z:\./]*[a-z.]{3,4}[a-z]+[.][comin]+',text)
# print(website)

# name=re.findall(r'[M]+[mrs]+[.s]+[\s]{1}[a-zA-Z]+',text)
# print(name)