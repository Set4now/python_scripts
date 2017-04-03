def create():
  mydic = dict()
  mydic['suman'] = 'redhat'
  mydic['kamesh'] = 'webadmin'
  return mydic

"""
The dictionary that is created is returned, but the local variable name in the function, spanish, is
lost when the function terminates.
In main, to remember the dictionary returned, it needs a name. The name does not have to match
the name used in createDictionary. The name dictionary is descriptive.
"""
def main():
  newdic = create()
  print "This value of suman is " + newdic['suman']
  print newdic['kamesh']

main()

