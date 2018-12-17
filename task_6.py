#task_6
#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
nl = int(input("Enter a letter of English alphabet from 1 - 26: "))
l = chr(nl + 96)
print(l)
print('The letter with number {} is  {}.'.format(nl, l))