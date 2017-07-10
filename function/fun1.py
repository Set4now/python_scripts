def add(list1, list2):
  list1.append('java')
  list2 = list1
  print list1
  print list2


list1 = ['python']
list2 = ['bash']

add(list1, list2)

print list1
print list2
