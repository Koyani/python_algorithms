#task_9
#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input("Enter the first number: "))
b = int(input("Enter the first second: "))
c = int(input("Enter the third number: "))
if (a < b < c) or (c < b < a):
    middle = b
    print('Middle number is {}'.format(middle))
elif (a < c < b) or (b < c < a):
    middle = c
    print('Middle number is {}'.format(middle))
else:
    middle = a
    print('Middle number is {}'.format(middle))