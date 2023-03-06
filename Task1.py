# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

len_one = int(input("Введите количество элементов первого множества: "))
len_two = int(input("Введите количество элементов второго множества: "))

list_one = []
list_two = []

for i in range(len_one):
    list_one.append(random.randint(0, 9))
print(list_one)

for i in range(len_two):
    list_two.append(random.randint(0, 9))
print(list_two)

set_one = set(list_one)
set_two = set(list_two)

new_set = set_one.intersection(set_two)
new_set = sorted(new_set)
print(new_set)







