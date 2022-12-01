# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def fill(a):
    if a == 1:
        return 1
    else:
        return a * fill(a-1)


def nabor(elem):
    result = []
    for i in range(1, elem + 1):
        result.append(fill(i))
    print(result)

number = int(input("Введите число: "))
nabor(number)