def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax


print highestNumber ([77,48,19,17,93,90])



def sum(l):
  count=0
  for num in l:
    count += num
    
  return count

print sum([77,48,19,17,93,90])


