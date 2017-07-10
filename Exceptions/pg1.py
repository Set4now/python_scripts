#user_input=int(raw_input("Enter a number: "))
try:
  user_input=int(raw_input("Enter a number: "))
  print user_input
except ValueError:
  print "Please enter a number"
else:
  print "You have entered a correct number"
