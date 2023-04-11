# Задача № 6:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# Проверка:
# 385916 -> yes
# 123456 -> no
#
# Решение:
numberTicket = int(input("Введите номер Вашего билета: "))
print(numberTicket)
firstNumbers = numberTicket // 1000
# print(firstNumbers)
secondNumbers = numberTicket % 1000
# print(secondNumbers)
firstNumbersOne = firstNumbers % 10
firstNumbersTwo = firstNumbers // 10 % 10
firstNumbersThree = firstNumbers // 100 % 10
sumFirstNumbers = firstNumbersOne + firstNumbersTwo + firstNumbersThree
# print(firstNumbersOne)
# print(firstNumbersTwo)
# print(firstNumbersThree)
# print(sumFirstNumbers)
secondNumbersOne = secondNumbers % 10
secondNumbersTwo = secondNumbers // 10 % 10
secondNumbersThree = secondNumbers // 100 % 10
sumSecondNumbers = secondNumbersOne + secondNumbersTwo + secondNumbersThree
# print(secondNumbersOne)
# print(secondNumbersTwo)
# print(secondNumbersThree)
# print(sumSecondNumbers)
if (sumFirstNumbers == sumSecondNumbers):
    print("Ура! У тебя в руках счастливый билет.")
else:
    print("Увы и ах! У тебя в руках обычный билет.")
