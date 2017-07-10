import os
with open(os.path.join(os.getcwd(), 'suman.txt'), 'r') as f:
    for line in f:
       print line



f=open('suman.txt', 'r')
print  f.readlines(1)


from itertools import islice
with open(os.path.join(os.getcwd(), 'suman.txt'), 'r') as f:
    for line in islice(f, 1):
       print line
print "================="

def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('suman.txt',1)
