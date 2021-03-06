class Employee:
  
  raise_amount = 1.04
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@example.com'


  def fullname(self):
    return '{0} {1}'.format(self.first, self.last)

  def apply_raise(self):
    return int(self.pay * self.raise_amount)


# creating instances

emp_1 = Employee('suman', 'deb', 1000000)
emp_2 = Employee('shubham', 'srivastava', 200000)

# printing instances attributes

#print emp_1.email
#print emp_2.email

#Applying methods on instances

#print emp_1.fullname()
#print emp_2.fullname()


# Applying methods on class but giving instance name as arguement

#print Employee.fullname(emp_1)

print 'employeeone has a pay of ' + str(emp_1.pay)
print 'employeeone after apprasial ' + str(emp_1.apply_raise())

## creating a variable for an instance
## only applies to emp_2 the rest of the instances would have no effect.


emp_2.raise_amount = 1.05
print emp_2.apply_raise()
print emp_1.apply_raise()
