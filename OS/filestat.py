import os

cwd='/scripts_python/OS/'
print 'FileName' + '	' + 'Length' + '	' + 'ModificationTIme'
for file in os.listdir(cwd):
  print file + '	' + str(os.stat(file).st_size) + '	' + str(os.stat(file).st_mtime)



