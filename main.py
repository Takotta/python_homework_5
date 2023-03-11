# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод
#
# 8-5+2-1
# Вывод
# 4

# numbers = input('Введите пример: ')
# print(numbers)
# count = 1
# numbers_summ = int(numbers[0])
# while count < len(numbers):
#     if numbers[count] == "+":
#         numbers_summ += int(numbers[count+1])
#     elif numbers[count] == "-":
#         numbers_summ -= int(numbers[count+1])
#     count +=2
# print(numbers_summ)

# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)
#
# Формат ввода
# Вводится строка.
#
# Формат вывода
# Выведите слова из строки по одному.
#
# Пример 1
# Ввод
#
# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод
#
# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland

numbers = input('Введите пример: ')
print(numbers)

numbers_summ = ""
for num in numbers:
    if num == " ":
        print(numbers_summ)
        numbers_summ = ''
    elif num != " ":
        numbers_summ += num
print(numbers_summ)