match = re.search(pat, text) will return a match object
match.group() tells about matching object ( True or False)
if match:
example:-

def find(pat, text)
  match = re.search(pat, text)
  if match:
   print match.group()
  else:
    print 'not found'

. any character except new line
find('...g', piiig)
stop at the first search (left to right)

\w word character  a-z,0-9,_  (Note:- space is not a word charcter)
find(r':\w\w\w', ':cat')
:cat

\d 
find(r'\d\d\d', ':123')
:123


\s white space
find(r'\d\s\d\s\d', '1 2 3')
1 2 3 

+ 1 or more
* 0 or more

find(r'\d\s+\d\s+\d', '1    2        3')
1   2         3


\S non white space 


>>> match = re.search(r'[\w.]+.\w+@[\w.]+', 'blaaa suman.deb@gmail.com @ y')
>>> print match.group()
suman.deb@gmail.com

[] -->  is a set of character

([]) --> group

re.findall (searches allthe string)





