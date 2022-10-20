# Семинар 2:
# git checkout Sem2Task5 - Задача 5 - Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
import os
list = [0,1,2,3,4,5,6,7,8,9]
print ("Начальный список: " + str(list))
lst2 = sorted(list, key=os.urandom)
print ("Перемешанный список: " + str(lst2))

