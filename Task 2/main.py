# найдите сумму цифр трехзначного числа
print ("Введите число: ")
n = int(input())
a = n // 100
b = n % 10
c = n // 10 % 10
print(a + b + c)