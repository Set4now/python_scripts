import re

#suman.deb2@cognizant.com

input = raw_input("Enter the email adress: ")

user = input.split("@")

print user[0]
