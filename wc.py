#This will do the word counts in a file.
import sys

def wc(filename):
  f = open(sys.argv[1], 'r')
  lines = f.read()
  list = lines.split()
  print list
  for words in list:
    print words, list.count(words)

if len(sys.argv) >= 1:
  wc(sys.argv[1])
else:
  print "Please provide the filename"


