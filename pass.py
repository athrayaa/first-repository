import random

upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
symbol="!@#$%^&*()_"

string= upper+lower+number+symbol
length=16

password="".join(random.sample(string,length))
print("your new password is: "+password)

a=56
b=75
c=a*b
print(c)
