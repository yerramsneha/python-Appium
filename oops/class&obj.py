class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()


class Employee:
    id = 10
    name = "John"

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp = Employee()
emp.display()


# del emp.id
# emp.display()

class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count + 1


s1 = Student()
s2 = Student()
s3 = Student()
print("The number of students:", Student.count)


class Student:
    def __init__(self):
        print("non parametrized constructor")

    def show(self, name):
        print("Hello", name)


student = Student()
student.show("John")

class student:
    def __init__(self):
        print("The First Constructor")
    def __init__(self):
        print("The Second Constructor")

st = student()
