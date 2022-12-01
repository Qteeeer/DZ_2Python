# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)


# Реализуйте алгоритм перемешивания списка.

# from random import randint

# def list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(-n, n))
#     return list

# n = int(input('Введите число чтобы указать число элементов: '))
# numbers = list(n)
# print(numbers)
# for i in range (len(numbers)):
#     random_num = randint(i, n-1)
#     temp = numbers[i]
#     numbers[i] = numbers[random_num]
#     numbers[random_num] = temp

# print(numbers)