# напишите программу, которая на вход принимает два числа A и B,
# и возводит число A в целую степень B с помощью рекурсии

print("Введите значение А:")
a = int(input())
print("Введите значение B:")
b = int(input()) 

def pov(i, n):
    if (n == 1):
        return i
    else:
        return i * pow(a, n - 1)
print(pov(a, b))