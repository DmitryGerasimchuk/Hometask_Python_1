# Задача № 4:
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# Проверка:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
#
# Решение:
sumBirds = int(input("Введите итоговое число бумажных журавликов, которые сделали ребята: "))
print(sumBirds)
# pBirds + kBirds + sBirds = sumBirds
# pBirds = sBirds
# kBirds = 2*(pBirds + sBirds)
pBirds = sumBirds // 6
print("Петя сделал", pBirds, "бумажных журавликов.")
sBirds = pBirds
print("Сережа сделал", sBirds, "бумажных журавликов.")
kBirds = 2 * (pBirds + sBirds)
print("А, Катя - большая молодец сделала", kBirds, "бумажных журавликов.")
