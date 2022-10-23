# Семинар 4:
# git checkout Sem4Task2 - Задача 2 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from re import I


num = int(input('Введите число: '))
i = 2 
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f'Простые множители числа {old}: {lst}')