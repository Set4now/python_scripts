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

class Developers(Employee):
  def __init__(self, first, last, pay, prog_lang):
    Employee.__init__(self, first, last, pay)
    self.prog_lang = prog_lang


dev_1 = Developers('kamesh', 'patni', 700000, 'python')

print dev_1.email
print dev_1.pay
print dev_1.prog_lang

print issubclass(Developers, Employee)
print isinstance(dev_1, Developers)
