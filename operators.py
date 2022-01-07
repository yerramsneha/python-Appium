
#Arithmetic operators
x = 10
y = 20
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)  # modulus
print(x**2)  # Exponentiation
print(15//2) # floor division

#Comparison operators
print(x==y) #equal
print(x!=y) #not equal
print(x>y)  #greater than
print(x<y)  # less than
print(x>=y) #greater than or equal to
print(x<=y) #less than or equal to

#Assignment Operators
x=5
print(x)
x+=5  # x = x +5
print(x)
a = 10
a-=3 # x = x - 5
print(a)
a = 5
a *= 3
print(a)
a = 5
a /= 3
print(a)
a = 5
a %= 3
print(a)
a = 5
a //= 3
print(a)
a = 5
a **= 3
print(a)
a = 9
a &= 3  # bitwise AND
print(a)
a = 9
a |= 3  # bitwise or
print(a)
a = 9
a ^= 3 # XOR
print(a)
a = 9
a >>= 3 # Right shift
print(a)
a = 9
a <<= 3 # left shift
print(a)
#Logical Operators
x = 3
print(x <5 and x<10)
print(x <5 or x<10)
print(not(x <5 and x<10))

#Membership Operators
x = ["apple","banana"]
print("banana" in x)
x = ["apple","banana"]
print("banana" not in x)
#Identity Operators
x = ["apple","banana"]
y = ["apple","banana"]
z = 20
print(x is z)
print(x != y)
#Bitwise Operators
print(5&6)
print(5|6)
print(5^6)
print(~(5))
print(4<<5)
print(4>>5)