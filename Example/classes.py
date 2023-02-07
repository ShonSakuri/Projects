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
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"Hello my name is {self.name}")

p1 = Person("Shon", 16)
p1.myfunc()