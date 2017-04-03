import sys

if len(sys.argv) > 1:
   name = sys.argv[1]
else:
   name = raw_input('Enter the name: ')

if len(sys.argv) > 2:
   age = int(sys.argv[2])
else:
   age = int(raw_input('Enter the age: '))

sayhello = 'hello ' + name 

if age == 100:
   sayage = 'you are already 100 years old'
elif age < 100:
   sayage =  'You will be 100 in ' + str(100 - age) + ' years'
else:
   sayage =  'you turned 100 in', str(age - 100), 'years ago'

print sayhello, sayage
