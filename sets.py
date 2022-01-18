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
#Months.remove("Jan") #will give an error as the key jan is not available in the set.
print("\nPrinting the modified set...")
print(M2)
print("Set operations")
Day1 = {"Monday","Tuesday","Wednesday","Thursday","Sunday"}
Day2 = {"Friday","Saturday","Sunday"}
print(Day1|Day2)
print("union method")
print(Day1.union(Day2))
print("intersection")
print(Day1&Day2)
print("intersection")
print(Day1.intersection(Day2))

print("intersection_update")
a = {"Devansh", "bob", "castle"}
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav","castle"}
a.intersection_update(b,c)
print(a)
print("difference")
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1-Days2)
print(Days1.difference(Days2))
print("symmetric difference")
a = {1,2,3,4,5,6}
b = {1,2,9,8,10}
c = a ^ b
print(c)
print(a.symmetric_difference(b))

print("set comparisons")
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday"}
Days3 = {"Monday", "Tuesday", "Friday"}

# Days1 is the superset of Days2 hence it will print true.
print(Days1 > Days2)

# prints false since Days1 is not the subset of Days2
print(Days1 < Days2)

# prints false since Days2 and Days3 are not equivalent
print(Days2 == Days3)
