#task_5
#Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
l1 = input("Enter the first letter: ")
l2 = input("Enter the second letter: ")
x = ord(l1)
y = ord(l2)
print('The position of {} is {}.'.format(l1, x - 96))
print('The position of {} is {}.'.format(l2, y - 96))
if x > y:
    d = x - y
    print('The distance between {} and {} is {} letters'.format(l1, l2, d))
else:
    d = y - x
    print('The distance between {} and {} is {} letters'.format(l2, l1, d))