# Семинар 4:
# git checkout Sem4Task1 - Задача 1 -  Вычислить число c заданной точностью d

from cmath import pi


d = int(input('Введите точность числа Пи '))
print(f'Число Пи с заданной точностью {d} равно {round(pi,d)}')