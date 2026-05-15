#تمام اعدادی که تمام ارقام آن‌ها زوج هستند، در بازه داده شده.
a = int(input(':'))
b = int(input(':'))
for i in range(a, b+1):
    temp = i
    while temp % 2 != 1:
        temp = temp // 10
        if temp == 0:
            print(i)
            break

#خروجی: تمام اعداد زیگ زاگی، در بازه داده شده.