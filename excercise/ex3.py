nums = raw_input("Please enter the numbers: ")

new_nums = nums.split(",")

lis = []
tup = ()

for i in new_nums:
  lis.append(i)
  tup = tuple(lis)

print lis
print tup
