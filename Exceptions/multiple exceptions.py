try:
    a = 10/0
except(ArithmeticError,IOError):
    print("Arthemetic")
else:
    print("Sucessfully done")