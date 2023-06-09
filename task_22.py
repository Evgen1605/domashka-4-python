# Задача 22: Даны два неупорядоченных набора целых чисел(может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующей строке второй список.

# Даны два неупорядоченных набора целых чисел(может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


from random import randint
n_set = set(randint(1, 20) for i in range(
    int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(randint(1, 20) for i in range(
    int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(*s_set)

# Эталонное решение
mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
  set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
  set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
  print(i, end=' ')


# решение преподавателя
nums1 = [1,2,1,3,4]
nums2 = [1,10,5,3]
print(set(nums1).intersection(set(nums2)))