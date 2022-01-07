"""
demo about if-else

"""
#if
a = 5
if a>0:
    print("a is positive")

num = int(input("enter the number"))
if num%2 == 0:
    print("Number is even")

a = int(input("Enter a ? "))
b= int(input("enter b"))
c = int(input("Enter c"))
if a>b and a>c:
    print("a is largest")
if b>a and b>c:
    print("b is largest")
if c>a and c>b:
    print("c is largest")

#if-else

age = int(input("Enter your age? "))
if age > 18:
    print("You are Eligible")
else:
    print("Sorry! you are not eligible")

# if-elif-elif-else
marks = int(input("Enter the marks? "))
if marks > 85 and marks <= 100:
    print("Congrats! grade A")
elif marks >60 and marks <= 85:
    print("Grade B")
elif marks >40 and marks <=60:
    print("Grade c")
elif (marks>30 and marks <= 40):
    print("Grade c")
else:
    print("you are fail!! ")


