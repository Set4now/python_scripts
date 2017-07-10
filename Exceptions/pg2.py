try:
  f=open('corrupt_file.txt', 'r')
  var=suman
#  if var != 'badvar':
#    raise Exception
except IOError as e:
  print e
except Exception as e:
  print 'wrong'
else:
  print f.read()
  f.close()
  print var
finally:
  print 'Progammed finished'
