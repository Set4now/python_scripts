def copies(str):
  if len(str) > 2:
    last_two = str[-2:]
    #return '{}{}{}{}'.format('last_two')
    return last_two + last_two + last_two + last_two
print copies('suman')
