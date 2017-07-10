import os
import sys

source_file=raw_input("Enter the path of the file: ")
target_file=raw_input("Enter the backup filename with absolute path: ")

if source_file == "" or target_file == "":
	print sys.argv[0]
	if sys.argv[2] == "abc" or sys.argv[3] == "xyz":
		print "Please enter the file names in user promt or on command line"
		sys.exit()
           

if os.path.exists(source_file):
	with open(source_file, 'r') as fr:	
		with open(target_file, 'w+') as fw:
			for lines in fr:
				fw.write(lines)
else:
	print 'Please check if the source file to backup exist or not'
		
