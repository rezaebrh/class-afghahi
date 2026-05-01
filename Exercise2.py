print ('اعداد زوج دورقمی')
i = 10
a = 0
m = 0
while i < 100:
    if i % 2 == 0:
        a = a + 1
        m = m + i
        print(i)
    i = i + 1
print('END')
print ('تعداد اعداد بدست اومده :' , a)
print ('جمع اعداد بدست اومده :' , m)



print('اعداد مضرب ۵ بین ۱۰۰ تا ۲۰۰')
i = 100
while 100 <= i <= 200:
    if i % 5 == 0:
        print (i)
    i = i + 5
print ('END')



print('اعداد فرد بین ۱۰۰ تا ۲۰۰')
i = 100
while 100 <= i < 200:
    if i % 2 == 0:
        i = i + 1
        print(i)
    i = i + 1
print ('END')


print ('اعداد مضرب ۱۰ تا ۱۰۰۰')
i = 0
while i <= 1000:
    if i % 10 == 0:
        print (i)
    i = i + 10
print ('END')