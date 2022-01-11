list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)

list1 = [10, 20, 30, 40, 50]
# get list size
# len(list1) -1: because index start with 0
# iterate list in reverse order
# star from last item to first
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])

for i in range(5):
    print(i)
else:
    print("Done!")

n = 5
# first number of sequence
start = 5
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 5
print("\nSum of above series is:", sum_seq)