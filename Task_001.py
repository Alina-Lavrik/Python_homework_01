# 1 Напишите программу, которая принимает на вход цифру, обозначающую день
# недели и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

print('Введите цифру, которая обозначает день недели: ')
N = int(input())

if N <= 5 and N >= 1:
    print('Это будний день')
elif N == 6 or N == 7:
    print('Это выходной день')
else:
    print('Такого дня недели нет')
