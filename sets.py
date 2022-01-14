Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(Days)
print(type(Days))
print("looping through the set elements ... ")
for i in Days:
    print(i)

set1 = {}
print(type(set1))
set2 = set()
print(type(set2))

Months = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(Months)
print("\nAdding other months to the set...")
Months.add("July")
Months.add ("August")
print("\nPrinting the modified set...")
print(Months)
print("\nlooping through the set elements ... ")
for i in Months:
    print(i)

M1 = set(["January","February", "March", "April", "May", "June"])
print(M1)
M1.update(["July","August","October","November"])
print(M1)

print(M1)
M1.discard("July")
print(M1)

print(M1)
M1.remove("June")
print(M1)

print(M1)
M1.pop()
print(M1)

print(M1)
M1.clear()
print(M1)

M2 = set(["January","February", "March", "April", "May", "June"])
print("\nprinting the original set ... ")
print(M2)
print("\nRemoving items through discard() method...");
Months.discard("Feb"); #will not give an error although the key feb is not available in the set
print("\nprinting the modified set...")
print(M2)
print("\nRemoving items through remove() method...");
Months.remove("Jan") #will give an error as the key jan is not available in the set.
print("\nPrinting the modified set...")
print(M2)