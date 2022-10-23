# Семинар 4:
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

k = int(input('Введите степень k:'))

fact = []
for i in range (1, k +2):
    fact.append(randint(1,101))

itog = []
for i in range(len(fact)):
    if k == 1:
        itog.append(f'{fact[i]}*x')
    elif k == 0:
        itog.append(f'{fact[i]}')
    else:
        itog.append(f'{fact[i]}*x^{k}')
    signs = randint(0,1)
    if signs == 1:
        itog.append('+')
    elif signs == 0:
        itog.append('-')
    k -= 1

itog.pop(-1) 
itog.append('=0')

record = open('task4.txt', 'w')
record.write(''.join(itog))
record.close()