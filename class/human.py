class human:
# this is class variable which is availablw to all the instances
  gender="male"
  num_of_humans = 0


  def __init__(self, name, age, **kwargs):
	#self.name = kwargs['name'] if 'name' in kwargs else None
        self.name = name
	#self.age = kwargs['age'] if 'age' in kwargs else None
	self.age = age
        self.skill = kwargs['skill'] if 'skill' in kwargs else None
        human.num_of_humans += 1

#These are all regular instance method that takes self which the instance itself as a first arguement automatically.
#
#
  def allot_project(self):
	if self.skill == "Python":
		print self.name + " with age " +  str(self.age) + "shoud be alloted to python development"
        elif self.skill == "Java":
		print self.name + " with age " +  str(self.age) + "shoud be alloted to java development"

# This method will apply on class not on instance. So it will have an effect 
  @classmethod
  def changing_gender(cls, gender):
    cls.gender = gender

  @staticmethod
  def is_workingday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return True

## the dancers class will inherites the init method from human ( the parent class) 
## Also changing a similar attritbute like gender which both parent and child class have, will not have any effect on the parent class attribute.
## We can create init method of child classes as well like the below:-
class dancers(human):
  gender="Female"
  def __init__(self, name, age, **kwargs):
    human.__init__(self, name, age, **kwargs)
    self.level=kwargs['level'] if 'level' in  kwargs else None
    

dancer1=dancers("sushmita", 25, skill="katthak", level="medium")
print dancer1.name
print dancer1.age
print dancer1.skill
print dancer1.gender
print dancer1.level

##Printing the number of humans before creating the object
#
#
#
print human.num_of_humans

#creating instances of the class
#
#
#
## these variables will hold the object

sudip=human("sudip",29,skill="Java")
abhishek=human("abhishek",28,skill="Python")

#Printing the number of humans after creating the object
#
#
#
print human.num_of_humans


# access the varible inside the object sudip
#
#
print sudip.gender
sudip.allot_project()
abhishek.allot_project()

#changing attribute "gender" for an specific object ike sudip
#
#
#
sudip.gender = "female"
print sudip.gender
#
#
#
#But the attribute gender for abhishek will remain the same
print abhishek.gender
#Check what the class hols...methods etc
#
print dir()

#
# check what the intance or object sudip holds
print dir(sudip)


# check all the attributes including class and instance this instance holds
print (sudip.__dict__)


### Adding a class method... a method which takes class as the first agruement as "cls"
#
#
#
#  @classmethod
#  def changing_gender(cls, gender):
#    cls.gender = gender
# Changing the gender with class method
human.changing_gender("shemale")

print abhishek.gender

# the gender of sudip will still remain as female since this attrbute applied on sudip (instance) explicitly
print sudip.gender

### Applyting static method 

import datetime
my_day=datetime.date(2017, 7, 27)
print sudip.is_workingday(my_day)


print isinstance(dancers, human)
print issubclass(dancers, human)

print help(dancers)