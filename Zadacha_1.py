# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import random


def sumElem(elem):
    result = 0
    massElem = str(elem)
    for i in range(len(massElem)):
        if massElem[i] != ",":
            result += int(massElem[i])
        else:
            continue
    print(result)


number= input("Введите вещественное число: ")
sumElem(number)