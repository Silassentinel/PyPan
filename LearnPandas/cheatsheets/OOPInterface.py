# cheatsheet file for interfaces

from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def myfunc(self):
        pass

class MyClass(MyInterface):
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = MyClass("John", 36)

print(p1.name)
print(p1.age)
p1.myfunc()
