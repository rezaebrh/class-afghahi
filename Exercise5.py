# 1
r_s = int(input()) #radif setare
for i in range(1 , r_s + 1):
    print((r_s - i) *  " " + (i) * "*")


# 2
p_b = int(input("payan bazi:"))#payan bazi
hop = int(input("hop:"))
s_b = int(input("shoro konande bazi:"))#shoro konande bazi
for i in range(1 ,p_b + 1):
    if s_b == 1 and i % 2 != 0 and i % hop == 0:
        print("hop!")
    elif s_b == 1 and i % 2 != 0:
        print(i)
    if s_b == 2 and i % 2 == 0 and i % hop == 0:
        print("hop!")
    elif s_b == 2 and i % 2 == 0:
        print(i)
if s_b != 1 or s_b != 2:
    print("Eror")


# 3
number = int(input())
plural = 0
while number > 0:
    plural = plural + number % 10
    number = number // 10
while 1<= plural <= 100:
    if plural % 2 == 0:
        plural = plural // 2
        continue
    if plural == 1:
        print("YES")
        break
    else:
        print("NO")
        break


# 4
def prime_numbers(x):
    prime_test = (10 ** (x - 1))
    prime = []
    while (prime_test < (10 ** x)):
        count = 0
        for i in range(1, prime_test + 1):
            if prime_test % i == 0:
                count += 1
            if count == 2 and prime_test == i:
                prime.append(prime_test)
        prime_test += 1
    return prime

num_digits = int(input("Enter a number: "))
favorite_num = int(input("Enter a favorite number: "))
primes = prime_numbers(num_digits)
for i in range(len(primes)):
    test = primes[i]
    while test > 0:
        last = test % 10
        if last == favorite_num:
            print(primes[i])
            break
        test //= 10


# 5
def num_of_digits(x):
    num_digits = []
    number = 10 ** (x - 1)
    while number < (10 ** x):
        num_digits.append(number)
        number += 1
    return num_digits


input_num_digi = int(input("Enter the number of digits: "))
num_def = num_of_digits(input_num_digi)
total = 0
for i in range(len(num_def)):
    total += num_def[i]
    if i == len(num_def) - 1:
        print(total)


# 6
متوجه سوال نشدم که چی از من می خواد


# 7
def prime_numbers(x):
    prime_test = (10 ** (x - 1))
    prime = []
    while (prime_test < (10 ** x)):
        count = 0
        for i in range(1, prime_test + 1):
            if prime_test % i == 0:
                count += 1
            if count == 2 and prime_test == i:
                prime.append(prime_test)
        prime_test += 1
    return prime

input_num_digits = int(input("Enter the number of digits: "))
prime = prime_numbers(input_num_digits)
for i in range (len(prime)):
    found = False
    test = prime[i]
    while test > 0:
        test = test // 10
        count = 0
        for j in range (1 , test + 1):
            if test % j == 0:
                count += 1
            if count == 2 and test == j and test < 10:
                print(prime[i])
            if count != 2 and test == j:
                found = True
                break
        if found:
            break


# 8
def oppositeـnumber(x):
    oppositeـnumber = []
    while x > 0:
        lastـdigit = x % 10
        oppositeـnumber.append(lastـdigit)
        x //= 10
    return oppositeـnumber

input = int(input(":"))
opposite_number = oppositeـnumber(input)
for i in range (len(opposite_number) - 1 , -1 , -1):
    if opposite_number[i] % 2 != 0:
        print(opposite_number[i] , end = "")


# 9
number = [int(x) for x in input()]
zero_one = [int(x) for x in input()]
for i in range(len(number)):
    for j in range(len(zero_one)):
        if j == i and zero_one[j] == 1:
            print(number[i] , end="")

# 10
def sum_of_digits(x):
    if x < 0:
        x = (x * -1)
    sum = 0
    while x > 0:
        sum += (x % 10)
        x //= 10
    return sum

input_1 = int(input(":"))
input_2 = int(input(":"))
sum_of_digits_all = 0
for i in range(input_1, input_2 + 1):
    sum_of_digits_all += sum_of_digits(i)
print(sum_of_digits_all)






