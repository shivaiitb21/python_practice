# All classes have a function called __init__(), which is always executed when the class is being initiated.
# the __init__() function is used to assign values to object properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)