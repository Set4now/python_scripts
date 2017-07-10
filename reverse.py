user_input=raw_input("Please enter a string: ")
if user_input == "":
  print "Dont leave it blank"
elif user_input == user_input[::-1]:
  print "The word is palindrome"
else:
  print "This is not an example of palindrome"
