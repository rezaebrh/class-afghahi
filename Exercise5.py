#1
r_s = int(input()) #radif setare
for i in range(r_s):
    print("*" * (i + 1))
#2
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
#3
number = int(input())
#به جوابی برای جدا کردن رقم نرسیدم
while 1<= number <= 100:
    if number % 2 == 0:
        number = number // 2
        continue
    if number == 1:
        print("YES")
        break
    else:
        print("NO")
        break
#4
#نتونستم حل کنم
#5
#متوجه سوال نشدم
