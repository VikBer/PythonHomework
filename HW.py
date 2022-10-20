# Семинар 2:
# git checkout Sem2Task2 - Задача 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.    состоящий из элементов последовательности 3n + 1.

n = int(input("Введите число n \n"))
arr = [1]
factorial = 1
for i in range(2, n+1):
    factorial *= i
    arr.append(factorial)

print(arr)