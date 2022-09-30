# git checkout Sem1Task3 - Задача 3 - Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
#                                     и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
restart = True
while restart :
    restart = False
    x = int(input(f'Введите координату точки Х: '))
    if x == 0: 
        print("Введите число отличное от нуля")
        restart = True
        continue 

restart = True
while restart :
    restart = False
    y = int(input(f'Введите координату точки Y: '))
    if y == 0: 
        print("Введите число отличное от нуля")
        restart = True
        continue 

if x > 0 and y > 0: print(f"X = {x}, Y = {y} это 1 четверть")
if x < 0 and y > 0: print(f"X = {x}, Y = {y} это 2 четверть")
if x < 0 and y < 0: print(f"X = {x}, Y = {y} это 3 четверть")
if x > 0 and y < 0: print(f"X = {x}, Y = {y} это 3 четверть")