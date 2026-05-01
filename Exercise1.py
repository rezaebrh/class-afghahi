side1 = int(input(':'))
side2 = int(input(':'))
side3 = int(input(':'))
if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
    print('مثلث است.')
else:
    print('مثلث نیست.')
if side1 == side2 == side3:
    print('نوع مثلث : متساوی الاضلاع.')
if side1 == side2 or side1 == side3 or side2 == side3:
    print('نوع مثلث : متساوی الساقین.')
if side1 ** 2 + side2 ** 2 == side3 ** 2 or side3 ** 2 + side2 ** 2 == side1 ** 2 or side3 ** 2 + side1 ** 2 == side2 ** 2:
    print('نوع مثلث : قائم الزاویه.')
elif side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2 and side1 != side2 != side3:
    print('نوع مثلث : مختلف الاضلاع.')

