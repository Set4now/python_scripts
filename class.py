class employee:

  raise_amount = 2

  def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@example.com'

  def fullname(self):
    return '{0} {1}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * employee.raise_amount)
 
emp_1 = employee('suman', 'deb', 100)
emp_2 = employee('kamesh', 'patni', 200)

emp_1.raise_amount = 6

#print emp_1.first
#print emp_1.pay
#print emp_1.email

#print employee.fullname(emp_1)
#print emp_1.fullname()

#print emp_1.pay
#emp_1.apply_raise()
#print emp_1.pay

print employee.raise_amount
print emp_1.raise_amount
print emp_2.raise_amount
