# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]


def subsequence(n):
    result = []
    sum = 0
    for i in range(0, n):
        result.append((1+1/(i+1))**(i+1))
        sum += result[i-1]
    print(result)
    print(f"Сумма последовательности равна: {sum}")


number = int(input("Введите число: "))
subsequence(number)