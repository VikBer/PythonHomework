# Семинар 2:
# git checkout Sem2Task4 - Задача 4 - Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.




n = int(input("Введите число n \n"))
lst = [i for i in range(-n, n)]
print(lst)

file = open('file.txt', 'r')
res = lst[int(file.readline())]*lst[int(file.readline(2))]*lst[int(file.readline(3))]*lst[int(file.readline(4))]
print(res)
