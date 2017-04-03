#def sorting(dicts):
#  sorted(dicts.values())
#  return dicts
  

#print sorting({"first" : 1, "second" : 2, "fourth" : 4, "third" : 3})
 
dict = {"first" : 1, "second" : 2, "fourth" : 4, "third" : 3}

sorted_inc = sorted(dict.values())
print sorted_inc
sorted_rev = sorted(dict.values(), reverse=True)
print sorted_rev 

import operator  
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}  
print('Original dictionary : ',d)  
sorted_d = sorted(d.items(), key=operator.itemgetter(0))  
print('Dictionary in ascending order by value : ',sorted_d)  
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)  
print('Dictionary in descending order by value : ',sorted_d)  

if "suman" in d:
  print "there"
print "not"
