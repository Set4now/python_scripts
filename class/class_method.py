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

  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amt = amount

  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return  cls(first, last, pay)

# creating instances

emp_1 = Employee('suman', 'deb', 1000000)
emp_2 = Employee('shubham', 'srivastava', 200000)


print 'employeeone has a pay of ' + str(emp_1.pay)
print 'employeeone after apprasial ' + str(emp_1.apply_raise())


#emp_2.raise_amount = 1.05
#print emp_2.apply_raise()
#print emp_1.apply_raise()

Employee.set_raise_amount(1.08)

print emp_1.raise_amt

emp_str_1 = 'John-Doe-7000'

new_emp_1 = Employee.from_string(emp_str_1)

print new_emp_1.email

