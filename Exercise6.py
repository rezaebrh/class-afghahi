# #سوال گفته شده توی جلسه ۱۲
# list = [int(x) for x in input().split()]
# for i in range(len(list)):
#     for j in range(i + 1, len(list)):
#         if list[i] < list[j]:
#             for k in range(j + 1, len(list)):
#                 if list[j] < list[k]:
#                     print(list[i], list[j], list[k])


# #1
# list = [int(x) for x in input().split()]
# print("tool =", len(list))
# print("aval =", list[0])
# print("akhar =", list[len(list)-1])
#
#
# #2
# list = [int(x) for x in input().split()]
# single_digit = int(input())
# list += [single_digit]
# print(list)
#
#
# #3
# list = [int(x) for x in input().split()]
# index = int(input())
# number = int(input())
# list1 = list[0:index]
# list2 = list[index:len(list)]
# list1 += [number]
# list = list1 + list2
# print(list)
#
#
# #4
# my_list = [int(x) for x in input().split()]
# my_list = my_list[0:len(my_list) - 1]
# print(my_list)
#
#
# #5
# my_list = [int(x) for x in input().split()]
# index = int(input())
# my_list1 = my_list[0:index]
# my_list2 = my_list[index + 1:len(my_list)]
# print(my_list1 + my_list2)
#
#
# # 6
# my_list = [int(x) for x in input().split()]
# number = int(input())
# for i in range(len(my_list)):
#     if my_list[i] == number:
#         print(i)
#         break
# else:
#     print(-1)
#
#
# #7
# my_list = [int(x) for x in input().split()]
# number = int(input())
# for i in range(len(my_list)):
#     if my_list[i] == number:
#         my_list1 = my_list[0:i]
#         my_list2 = my_list[i + 1:len(my_list)]
#         print(my_list1 + my_list2)
#         break
#
#
#
# #8
# my_list = [int(x) for x in input().split()]
# first_index = int(input())
# second_index = int(input())
# my_list1 = my_list[first_index:second_index + 1]
# print(my_list1)
#
#
# #9
# my_list = [int(x) for x in input().split()]
# i = 0
# count = 0
# if len(my_list) == 50:
#     while i <= len(my_list) - 1:
#         if my_list[9] == my_list[i]:
#             count += 1
#         i += 1
# print(count)
#
#
# #10
# my_list = [int(x) for x in input().split()]
# total_sum = 0
# for i in range(len(my_list)):
#     total_sum += my_list[i]
# print(total_sum)



























