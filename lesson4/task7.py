"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле
необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from itertools import count


def fact(num):
    factorial = 1

    for x in count(1):
        if x > num:
            break

        factorial = factorial * x
        yield factorial


n = int(input("Введите число: "))
i = 0

for y in fact(n):
    i += 1
    print(f"{i}! = {y}")
