# git checkout Sem1Task5 - Задача 5 - Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

from math import sqrt

a = []
for i in range(2):
    num = int(input(f"Введите {i+1} координату точки А: "))
    a.append(num)

b = []
for i in range(2):
    num = int(input(f"Введите {i+1} координату точки B: "))
    b.append(num)

d = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

print(f"A = {a}, B = {b}, расстояние = {d:.2f}")