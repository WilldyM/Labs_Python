import random
import math

n = input('Введите размерность массива: ')
while n.isdigit() == False:
    n = input('INPUT FALSE!\nВведите размерность массива: ')

n = int(n)
items = [random.randint(1, 10000) for i in range(n)]

nulls = int(math.log2(n))+1
nulls = 2 ** nulls - n

for i in range(nulls):
    items.append(0)

print('Должно быть добавлено '+str(nulls)+' нулей в массив.')
print('Итоговый массив со случайными числами от 1 до 10000: ')
print(items)
