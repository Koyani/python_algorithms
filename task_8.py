#task_8
#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input('Enter year number to check if it\'s leap year: '))
if year % 4 != 0:
    print("usual year")
elif year % 100 == 0:
    if year % 400 == 0:
        print("leap year")
    else:
        print("usual year")
else:
    print("leap year")
