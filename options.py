'''python class optparse.OptionParser, is a powerful tool for creating options for your script.
we call the parse_args function, which will return an options object and an args list object. We can access the variables defined in "dest=" when adding options on the options object returned. So it will have two options, options.name and options.age. If one of the variables wasn't passed in, we can check by using the "if variableName is None" condition. Then we will load from user input as before.'''


import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-n', '--name', dest='name', help='Your name')
parser.add_option('-a', '--age', dest='age', help='your age', type=int)

(options, args) = parser.parse_args()

if options.name is None:
   options.name = raw_input('Enter Name:')

if options.age is None:
    options.age = int(raw_input('Enter Age:'))

sayhello = 'Hello ' + options.name + ','
   

if options.age == 100:
   sayage = 'you are already 100 years old'
elif options.age < 100:
   sayage =  'You will be 100 in ' + str(100 - options.age) + ' years'
else:
   sayage =  'you turned 100 in', str(options.age - 100), 'years ago'

print sayhello, sayage
