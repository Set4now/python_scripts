class Employee:
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@example.com'


  def fullname(self):
    return '{0} {1}'.format(self.first, self.last)

# creating instances

emp_1 = Employee('suman', 'deb', 1000000)
emp_2 = Employee('shubham', 'srivastava', 200000)

# printing instances attributes

print emp_1.email
print emp_2.email

#Applying methods on instances

print emp_1.fullname()
print emp_2.fullname()


# Applying methods on class but giving instance name as arguement

print Employee.fullname(emp_1)
