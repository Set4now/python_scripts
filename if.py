valueone=raw_input("what is the first number?")
valuetwo=raw_input("what is the second number?")
def condition():
	if valueone == valuetwo:
		result=True
		print "Both numbers are %s" % (result)
	elif valueone != valuetwo:
		result=False
		print "Both numbers are %s" % (result)
	else:
		print "Please enter valid entires"
		condition()

condition()
