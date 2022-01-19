def fun1():
    print("my first function")


fun1()


# return

def sum1():
    a = 10
    b = 20
    c = a + b
    return c


print("the sum is ", sum1())


# arguments

def func(name):
    print("Hi", name)


func("python")


# Python function to calculate the sum of two variables
# defining the function
def sum(a, b):
    return a + b;


# taking values from the user
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# printing the sum of a and b
print("Sum = ", sum(a, b))


def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function = ", list1)


list1 = [10, 20, 30, 40]
print("list before calling function ", list1)
change_list(list1)
print("list outside function = ", list1)


def change_string(str):
    str = str + "adding string"
    print("printing the string inside function: ", str)


string1 = "hi iam there"
change_string(string1)
print("printing outside function: ", string1)


# Required arguments

def func(name):
    message = "Hi " + name
    return message


name = input("Enter the name:")
print(func(name))


# Default Arguments

def printme(name, age=25):
    print("My name is ", name, "and age is ", age)


printme(name="john")


def printme(name, age=25):
    print("My name is ", name, "and age is ", age)


printme(name="john", age=30)


# Variable-length Arguments (*args)

def printme1(*names):
    print("type of passed argument is ", type(names))
    print("printing the passed arguments....")
    for name in names:
        print(name)


printme1("john", "sneha", "ravi", "sanvi")


# Keyword arguments(**kwargs)

def func(name, message):
    print("printing the message with ", name, "and ", message)


func(name="John", message="hello")


# The function simple_interest(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case
def simple_interest(p, t, r):
    return (p * t * r) / 100


print("Simple Interest: ", simple_interest(t=10, r=10, p=1900))
