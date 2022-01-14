def odd_nums(n):  # Генератор нечётных чисел с yield
    for i in range(1, n + 1, 2): yield i


def odd_nums_adv(n):  # Генератор нечётных чисел без yield
    return (i for i in range(1, n + 1, 2))
