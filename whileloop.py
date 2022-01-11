#continue

i = 0
str1 = 'pythonprogramming'

while i < len(str1):
    if str1[i] == 'm' or str1[i] == 'g':
        i += 1
        continue
    print('Current Letter : ', str1[i])
    i += 1


#break
print("demo of break")

i = 0
str1 = 'pythonprogramming'

while i < len(str1):
    if str1[i] == 't':
        i += 1
        break
    print('Current Letter : ', str1[i])
    i += 1
#pass
print("demo of pass")
i = 0
str1 = 'pythonprogramming'

while i < len(str1):
    i += 1
    pass
print('Value of i : ', i)

#exp-1
i=1
while(i<=10):
    print(i)
    i=i+1
#exp=2
i=1
num = 0
b = 9
num = int(input("enter the number"))
while i<=10:
    print("%d X %d = %d \n"%(num,i,num*i))
    i = i+1

i = 1
while(i<=5):
    print(i)
    i=i+1
else:
    print("the while loop exhausted")