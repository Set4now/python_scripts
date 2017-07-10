'''
 This will reverse the sentence.
 For eg.
 string = "Welcome suman"
 expected output = "suman welcome"
'''
def rev_str(a):
  a=raw_input("Please write a sentence: ")
  print "The reverse string is:" 
  print " ".join(a.split(" ")[::-1])


rev_str("a")
