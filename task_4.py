#task_4
#Написать программу, которая генерирует в указанных пользователем границах:
#случайное целое число;
#случайное вещественное число;
#случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. 
#Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
#Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import *
x=int(input("Enter first integer number: "))
y=int(input("Enter second integer number: "))
if x > y:
    n = randint(y,x)
    print(n)
else:
    n = randint(x,y)
    print(n)
if x > y:
    n = randint(y*100,x*100)/100
    print(n)
else:
    n = randint(x*100,y*100)/100
    print(n)
l1 = input("Enter first symbol: ")
l2 = input("Enter second symbol: ")
x1 = ord(l1)
y1 = ord(l2)
if x1 > y1:
    n = randint(y1,x1)
    print(n)
else:
    n = randint(x1,y1)
    print(n)
