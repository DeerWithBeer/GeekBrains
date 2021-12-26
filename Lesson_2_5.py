# Функция преобразования float в рубли и копейки
# Копейки превращаются в целое число, и дополняются нулями, если их длина меньше 2х символов
def print_price(price_argument):
    return "{rub} руб {copies:0<2} коп".format(rub=int(price_argument), copies=int(100 * round(price_argument % 1, 2)))


price_list = [57.8, 46.51, 97, 43, 23.5, 6.5, 45.2, 77.1, 225.15, 0.43, 34.1, 11.65, 15.44, 42.42, 96.1, ]
print('Вывод цен в строку:')
print(*[print_price(price) for price in price_list], sep=' ,')
# Получение id листа до сортировки
id_before_sort = id(price_list)
# Сортировка
price_list.sort()
# Получение id списка после сортировки
id_after_sort = id(price_list)
# Сравнение списков
if id_before_sort == id_after_sort:
    print("ID списка не изменился")
else:
    print("ID списка изменился")
# Вывод цен по возрастанию
print('Цены по возрастанию:')
print(*[print_price(price) for price in price_list], sep=',')
# Список по убыванию
# Фактически копия базового списка (он отсортирвоан по возрастанию) в обратном порядке
lowest_price_list = price_list[-1:-len(price_list) - 1:-1]
print('Пять самых дорогих товаров по возрастанию:')
# Пять самых дорогих товаров, это пять первых товаров в списке по убыванию
# Чтобы взять их по возрастанию ,мы простов выводим их в обратном порядке
print(*[print_price(price) for price in lowest_price_list[5:0:-1]], sep=',')
