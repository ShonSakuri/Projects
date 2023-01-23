class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Shon", 16)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Shon", 16)

print(p1)

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Shon", 16)
p1.myfunc()