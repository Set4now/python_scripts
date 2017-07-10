def fun(*arg, **kwargs):
  print arg
  for value in arg:
     print value
  for key, value in kwargs.iteritems():
     print key, value
  for count,value in enumerate(arg):
    print '{0}{1}'.format(count,value)

print fun('ad','sas','ads',suman='devops',a=1)
