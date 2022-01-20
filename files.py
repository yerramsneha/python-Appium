import os;
file1 = open("f1.txt","w")

if file1:
    print("file is opened successfully")

file1.close()

#try:
 #   file2 = open("f2.txt","r")
#finally:
#    print("finally block excuted")
print("opening file")
f2 = open("f2.txt","r")
print(f2.read())
f2 = open("f1.txt","w")
f2.write(''' python is modern day language
its easy to understand''')
f2.close()

f2 = open("f2.txt","w")
f2.write(''' python is modern day language
its easy to understand''')
f2.close()

f2 = open("f2.txt","a")
f2.write(''' this is append txt python is modern day language
its easy to understand''')
f2.close()

f2 = open("f2.txt","r")
for i in f2:
    print(i)

f2 = open("f2.txt","r")
c = f2.readline()
c1 = f2.readline()
print(c)
print(c1)
f2.close()

#fileptr = open("file2.txt","x")
#print(fileptr)
#if fileptr:
 #   print("File created successfully")

fileptr = open("f2.txt","r")
print("The filepointer is at byte :",fileptr.tell())
c2 = fileptr.read()
print("after reading,file pointer at..",fileptr.tell())
fileptr.close()
#os.rename("f1.txt","file1.txt")
#os.remove("file1.txt")