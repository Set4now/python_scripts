import fileinput

f = open('cal.py', 'r+')
f.read()
f.write('This is nothing')
f.close()

with open('cal.py', 'a') as myfile:
    myfile.write('second line')

#f1 = open('test', 'r')
#f2 = open('test.tmp', 'w')
#for line in f1:
#	f2.write(line.replace('redhat', 'windows'))
#f1.close
#f2.close

#with fileinput.FileInput('test', inplace=True, backup='.bak') as file:
#	for line in file:
#	   print(line.replace('redhat', 'windows'))
#        file.close()


for line in fileinput.FileInput("test",inplace=1,backup='.bkp'):
    line = line.replace("windows", "windows12 ")
    print line,
