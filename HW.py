# Семинар 2:
# git checkout Sem2Task1 - Задача 1 -  Для натурального n создать словарь индекс-значение, 
#                                       состоящий из элементов последовательности 3n + 1.

n = int(input("Введите число n \n"))
dictionary = {}
for i in range(1,n):
    dictionary.update({i:3*i+1})

print(dictionary)