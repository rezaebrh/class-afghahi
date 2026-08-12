#1
my_list = [int(x) for x in input().split()]
direction = input()
repeat = int(input())
if direction == 'left':
    i = 1
    while i <= repeat:
        my_list.remove(my_list[0])
        my_list.append(my_list[len(my_list)-1])
        i += 1

if direction == 'right':
    i = 1
    while i <= repeat:
        my_list.remove(my_list[len(my_list)-1])
        my_list.insert(0 , my_list[0])
        i += 1
print(my_list)


#2
my_list = [int(x) for x in input().split()]
direction = input()
repeat = int(input())
how = input()
if how == 'shift':
    if direction == 'left':
        i = 1
        while i <= repeat:
            my_list.remove(my_list[0])
            my_list.append(my_list[len(my_list)-1])
            i += 1
    if direction == 'right':
        i = 1
        while i <= repeat:
            my_list.remove(my_list[len(my_list)-1])
            my_list.insert(0 , my_list[0])
            i += 1
    print(my_list)
if how == 'rotate':
    if direction == 'left':
        i = 1
        while i <= repeat:
            my_list.append(my_list[0])
            my_list.remove(my_list[0])
            i += 1
    if direction == 'right':
        i = 1
        while i <= repeat:
            my_list.insert(0, my_list[len(my_list) - 1])
            my_list.remove(my_list[len(my_list)-1])
            i += 1
    print(my_list)


#3
my_list = [int(x) for x in input().split()]
larg_num = my_list[0]
for i in range(1 , len(my_list)):
    if my_list[i] > larg_num:
        larg_num = my_list[i]
count = 0
for i in range(len(my_list)):
    if larg_num == my_list[i]:
        count += 1
print(larg_num)
print(count)


#4
my_list = [int(x) for x in input().split()]
start = int(input())
end = int(input())
jump = int(input())
my_list1 = my_list[start:end]
my_list2 = []
for i in range(len(my_list1)):
    if i % jump == 0:
        my_list2.append(my_list1[i])
print(my_list2)


#5
numـmember = int(input("tedad aza:"))
max_number = int(input("maximum aza:"))
out_list = []
for i in range(numـmember):
    member = int(input("ozv:"))
    if member <= max_number:
        out_list.append(member)
print(out_list)


#6
def average(mylist):
    sum = 0
    for i in range(len(mylist)):
        sum += mylist[i]
    return sum / len(mylist)

def placement(mylist, index, number):
    mylist1 = mylist[:index + 1]
    mylist1.append(number)
    mylist2 = mylist[index + 1:len(mylist)]
    return mylist1 + mylist2

def index_max_number(mylist):
    maximum = mylist[0]
    index = 0
    for i in range(1, len(mylist)):
        if mylist[i] > maximum:
            maximum = mylist[i]
            index = i
    return index

my_list = [int(x) for x in input().split()]
out_list = placement(my_list, index_max_number(my_list), average(my_list))
print(out_list)


#7
my_list = []
for i in range(8):
    num = int(input())
    if num not in my_list:
        my_list.append(num)
for i in range(10):
    num = int(input())
    if num not in my_list:
        my_list.append(num)
print(my_list)


#8
def intersection_list(my_list1, my_list2):
    my_intersection = []
    for i in range(len(my_list1)):
        for j in range(len(my_list2)):
            if my_list1[i] == my_list2[j] and my_list1[i] not in my_intersection:
                my_intersection.append(my_list1[i])
    return my_intersection

def sort_list(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

my_list1 = [int(x) for x in input().split()]
my_list2 = [int(x) for x in input().split()]
my_list3 = intersection_list(my_list1, my_list2)
my_list4 = sort_list(my_list3)
print(my_list4)


#9
my_list = []
a = int(input("a:"))
number_of_members = int(input("number of members:"))
for i in range(number_of_members):
    member = int(input())
    if member != a:
        my_list.append(member)
print(my_list)


#10
my_list = []
maximum_number = float('-inf')
index = 0
number_of_members = int(input())
for i in range(number_of_members):
    member = int(input())
    if member > maximum_number:
        maximum_number = member
        index = i
    my_list.append(member)
my_list2 = my_list[:index]
my_list3 = my_list[index + 1:]
print(my_list2 + my_list3)