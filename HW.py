# git checkout Sem1Task4 - Задача 4 - Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).
restart = True
while restart:
    restart = False
    num = int(input("Введите номер четверти: "))
    if num > 4 or num <= 0:
        print("Введите корректный номер четверти от одного до четырех")
        restart = True

if num == 1: print("X = 1...N, Y = 1...N")
if num == 2: print("X = -1...-N, Y = 1...N")
if num == 3: print("X = -1...-N, Y = -1...-N")
if num == 4: print("X = 1...N, Y = -1...-N")