#task_3
#По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.
x1 = float(input("Enter abscissa x1 for the first point: "))
y1 = float(input("Enter ordinate y1 for the first point: "))
x2 = float(input("Enter abscissa x2 for the second point: "))
y2 = float(input("Enter ordinate y2 for the second point: "))
#y1 = k*x1 + b
#y2 = k*x2 + b
#y2 = k*x2 + y1 - k*x1
k = (y2 - y1)/(x2 - x1)
print(round(k, 2))
b = y1 - k*x1
print(round(b, 2))
print('y = {:01.2f}*x + {:01.2f}'.format(k, b))
