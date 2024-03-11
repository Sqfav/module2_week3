from functools import reduce


def process_numbers(numbers):
    # Фильтрация положительных четных чисел
    filtered_numbers = filter(lambda x: x > 0 and x % 2 == 0, numbers)

    # Возведение каждого числа в квадрат
    squared_numbers = map(lambda x: x ** 2, filtered_numbers)

    # Суммирование всех чисел в списке,
    # начальное значение 0 обрабатывает случаи пустого списка и 1 числа в списке
    result = reduce(lambda x, y: x + y, squared_numbers, 0)

    return result

if __name__ == '__main__':
    print(process_numbers([1, 2, 3, 4, 5, -2, -4]))  # 20
    print(process_numbers([]))                       # 0 - пустой список
    print(process_numbers([1, 3, 5, 7]))             # 0 - без четных
    print(process_numbers([2]))                      # 4 - с одним числом
