try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print(c)
except Exception as e:
    print("cant divide by 0")
    print(e)
else:
    print("enjoy your code.. there is no exception...")

