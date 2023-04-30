# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые - гербом.
# Определить минимальное число монеток, которое нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которое нужно перевернуть

from random import randint
print("Введите число: ")
n = int(input())

one_side = 0
two_side = 0
count = 0
for i in range(n):
    a = randint(0, 1)
    if a == 0:
        one_side += 1
    else: 
        two_side += 1
    print(a)

if one_side >= two_side:
    count = n - one_side
else:
    count = n - two_side

print()
print("Перевернуть нужно", n, "раз")