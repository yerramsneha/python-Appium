str = "python"
for i in str:
    print(i)

list = [1,2,3,4,5,6,7,8,9,10]
n=5
for i in list:
    c = n*i
    print(n,"*",1,"=",c)

list1 = [10,50,25,46,35,86]
sum = 0
for i in list1:
    sum = sum + i
print("the sum is: ",sum)

#range(start,stop,step size)

for i in range(10):
    print(i,end='')

n = int(input("enter the number"))
for i in range(1,11):
    c = n * i
    print(n,"*",i,"=",c)

num = int(input("enter the number \n"))
for i in range(5,num,5):
    print(i)

l1 = ['peter','Jhon','ricky','dev']
for i in range(len(l1)):
    print("hello",l1[i])

rows = int(input("enter the rows"))
for i in range(0,rows+1):
    for j in range(i):
        print(i,end="")
    print()

for i in range(0,5):
    print(i)
    break;
else:
    print("for loop completly exhausted, since there is no break.")
print("loop got broken")
