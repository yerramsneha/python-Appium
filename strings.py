str1 = 'HElloPython'
print(str1)
str2 ='''Triple quotes string 
demo in python
enjoy...'''
print(str2)
print(str2[3])
print(str2[15])
print(str1[::-1])
#del str1
#print(str1)
print('p'in str2)
print('p'not in str2)
print("{} and {} both are popular programming languages".format("python","java"))
print("{1} and {0} best players".format("Sachin","Rohit"))
print("{b},{a},{c}".format(a = "JAmes",b = "peter",c ="ricky"))
i = 10
f = 1.290
str3 = "Deva"
print("Hi, Iam Integer... My value is %d \n Hi, Iam float.. value: %f \n Hi, iam string value : %s"%(i,f,str3))
str = "python"
str1 = str.capitalize()
print("old value ",str)
print("new value ",str1)

str = "pyThoN"
str1 = str.casefold()
print("old value ",str)
print("new value ",str1)

str = "python"
str1 = str.center(20,'!')
print("old value ",str)
print("new value ",str1)

str = "python"
str1 = str.upper()
print("old value ",str)
print("new value ",str1)

str = "PYTHON"
str1 = str.lower()
print("old value ",str)
print("new value ",str1)

str = "pythonpythonpython"
print(str.count("t"))

str = "pythonpythonpython"
print(str.find("t"))

str = "pythonpythonpython"
print(str.find("t",6))

str = "pythonpythonpython"
print(str.find("t",10,20))

str = "python"
str1 = str.replace("t","T")
print("old value ",str)
print("new value ",str1)

str = "python"
str1 = str.encode()
print("old value ",str)
print("new value ",str1)

str = "python"
str1 = str.isalpha()
print("old value ",str)
print(str1)


str = "12345"
str1 = str.isdigit()
print("old value ",str)
print(str1)