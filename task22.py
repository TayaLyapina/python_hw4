# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n, m = int(input('Введите количество элементов первого множества: ')), int(input('Введите количество элементов второго множества: '))

set_1 = set()
set_2 = set()

for i in range(n):
    num = int(input('Введите элемент первого множества: '))
    set_1.add(num)

for i in range(m):
    num = int(input('Введите элемент второго множества: '))
    set_2.add(num)

print(*sorted(set_1.intersection(set_2)))


