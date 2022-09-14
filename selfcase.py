# Self parameter is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

x = Person('shiva',25)
print(x.age)

