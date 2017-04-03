class employee:
  raise_amount = 8.5
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@example.com' 

  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  @classmethod
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

  @staticmethod
  def is_workday(day):
   if day.weekday() == 5 or day.weekday() == 6:
     return False
   return True

class developer(employee):
    raise_amount = 8.3
    #pass

dev_1 = developer('test', 'user', 120000)
dev_2 = developer('newtest', 'user1', 32000)


dev_1.apply_raise()

import datetime
my_date = datetime.date(2016, 12, 17)

print employee.is_workday(my_date)

emp_1 = employee('suhail', 'ahmed', 50000)
emp_2 = employee('pankaj', 'goyel', 100000)

emp_str_1 = 'gopal-deb-100000'
emp_str_2 = 'leena-deb-200000'

new_emp1 = employee.from_string(emp_str_1)
new_emp2 = employee.from_string(emp_str_2)

print new_emp1.pay
print new_emp1.first
print new_emp1.email
print dev_1.email
print dev_2.email

employee.set_raise_amount(1.5)
#emp_1.set_raise_amount(2.5)
#emp_2.set_raise_amount(3.5)
#dev_1.apply_raise()

print 'the initialu salary is ' + str(emp_1.pay)
print 'increment of every one is ' +  str(employee.raise_amount)
print 'the initial salary is ' + str(emp_2.pay)

print emp_1.raise_amount
print emp_2.raise_amount
print dev_1.pay

