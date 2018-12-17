#task_7
#По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. 
#Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
x = float(input("Enter length of first segment a: "))
y = float(input("Enter length of first segment b: "))
z = float(input("Enter length of third segment c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Segments a, b, and c can form a triangle")
    if a==b==c:
        print("The triangle is equilateral")
    elif (a==b) or (a==c) or (b==c):
        print("The triangle is isosceles")
    else:
        print("The triangle is versatile")
else:
    print("Segments a, b, and c cannot form a triangle")