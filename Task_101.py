# Задача №2:
# Найдите сумму цифр трехзначного числа.
#
# Проверка:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
#
# Решение:
a = int(input("Введите трехзначное число: "))
# print(a)
if (a > 99 and a < 1000):
    b = a % 10
    c = a // 10 % 10
    d = a // 100 % 10
    sumNumbers = b + c + d
    print("Сумма чисел указанного числа равна", sumNumbers)
else:
    print("Вы ввели не трехзначное число.")
