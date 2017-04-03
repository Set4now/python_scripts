input = raw_input("Please enter the string: ")
print "the length of the string is " + str(len(input))
dict = {}
for i in input:
  keys = dict.keys()
  if i in keys:
    dict[i] += 1
  else:
    dict[i] = 1
print dict
if len(input) < 2:
  print ""
print input[0:2] + input[-2:]

new_str = input.replace("t", "$")
index = input.index("t")
char = input[index]
new_str = char + new_str[char:]
print new_str
