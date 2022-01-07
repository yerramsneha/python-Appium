a = 50
b = a
print(id(a))
print(id(b))
a = 100
print(id(a))
x = y = z = 60
print(x)
print(y)
print(z)
# del x,y,z
# print(x)
# print(y)
# print(z)
a, b, c = 5, 40, 60
print(a)
print(b)
print(c)


def add():
    a = 10
    b = 20
    global d
    d=a + b
    print("the sum :", d)


add()

print(d)

a = 1000000000.55555555555555555555555555555555555555555555555555555555555555555555555
print(type(a))
print(a)
print(1,2,3,5,7,9,40,50)
print(a,b,c,d,x,y,z)
