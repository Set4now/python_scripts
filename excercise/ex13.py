a = [1, 2, 3, 4]
print 'length ' + '---> ' + str(len(a))
print 'range is ' + str(range(len(a)))


sum = 0
mul = 1

for i in a:
  sum += i
  mul = mul * i
print sum
print mul

a.sort(reverse=True)
print a[0]
