a = 5
print("the type of a ",type(a))

b = 55.2
print("the type of b ",type(b))

c = 1 + 3j
print("the type of c",type(c))
print("c is a complex number",isinstance(1 + 6j,int))
# sequence type
# strings

str = "string with double quotes"
print(str)
str1 = '''A Multiline
String'''
print(str1)

str2 = "hello java "
str3 = "strings demo"
print(str2[6:]) # slicing
print(str2[4]) #4th character
print(str2 * 4) #repete
s = str2 + str3
print(s) # concatenation

#list

list1 = [5,5.5,"python","java",8, 8]
print(type(list1))
print(list1)
print(list1[:5])
print(list1 + list1)
print(list1 * 3)
list1[4] = "hi"
print(list1)

#tuple

tup = ("hi","welcome","to","python",3,3)
print(type(tup))
print(tup)
print(tup[3:])
print(tup + tup)
print(tup * 3)
#tup[3] = "hi"

#dictionary
d = {"first":1,2:'java',3:'php'}
for x,y in d.items():
    print(x,y)
len(d)
print(type(d))
print(d[2])
print(d.keys())
print(d.values())
d[4] = 'perl'
print(d)

#boolean

print(type(True))
print(type(False))

#Set

set1 = set()
set2 = {'Java',2,3,'python',3}
print(set2)
print(type(set2))
set2.add(10)
print(set2)
set2.remove(3)
print(set2)
set2.add('python1')
print(set2)