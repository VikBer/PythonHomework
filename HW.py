# Семинар 4:
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
from itertools import chain
import itertools
from math import degrees
import re

file1 = 'Mnogochlen1.txt'
file2 = 'Mnogochlen2.txt'
fileSum = "sum.txt"

def readFile(file):
    with open (str(file), "r") as data:
        text = data.read()
    return text

def convertFile(text):
    text = text.replace('= 0', '')
    text = re.sub("[*|^| ]", " ", text).split('+')
    text = [char.split(' ') for char in text]
    text = [[x for x in list if x] for list in text]
    for i in text:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    text = [tuple(int(x) for x in j if x != 'x') for j in text]
    return text

def foldText(text1, text2):
    x = [0] * (max(text1[0][1], text2[0][1] + 1))
    for i in text1 + text2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort (key = lambda r: r[1], reverse = True)
    return res

def getSum(text):
    var = ['*x^'] * len(text)
    coefs = [x[0] for x in text]
    degrees = [x[1] for x in text]
    newText = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in newText:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    newText = list(itertools.chain(*newText))
    newText[-1] = ' = 0'
    return ''.join(map(str, newText))

def writeToFile(file, text):
    with open(file, 'w') as data:
        data.write(text)

text1 = readFile(file1)
text2 = readFile(file2)
text1_1 = convertFile(text1)
text2_2 = convertFile(text2)
text3 = foldText(text1_1, text2_2)
textSum = getSum(foldText(text1_1, text2_2))
writeToFile(fileSum, textSum)

print(f'Первый многочлен:\n{text1}')
print(f'Второй многочлен:\n{text2}')
print()
print(f'Конвертация первого многочлена в список:\n {text1_1}')
print(f'Конвертация второго многочлена в список:\n {text2_2}')
print()
print(f'Список суммы многочленов с равными коэффициентами:\n {text3}')
print()
print(f'Итоговая запись многочлена:\n{textSum}')