class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("dog Barking")

d =Dog()
a = Animal()
a.speak()
d.bark()
d.speak()

#multi-level
print("multi-level")

class Animal:
    def speak(self):
        print("Animal Speaking")
#The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()

#muitiple inheritance
print("muitiple-inheritance")
class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))

#issubclass
print("issubclass")
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))

#isinstance (obj, class) method
print("isinstance (obj, class) method")
print(isinstance(d,Calculation2))
