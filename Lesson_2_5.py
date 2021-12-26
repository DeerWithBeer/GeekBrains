def print_price(price_argument):
    return "{rub} руб {copies:0<2} коп".format(rub=int(price_argument),copies=int(100*round(price_argument%1,2)))
price_list=[57.8, 46.51, 97,43,23.5,6.5,45.2,77.1]
print('Вывод цен в строку:')
print(*[print_price(price) for price in price_list],sep=' ,')
id_before_sort=id(price_list)
price_list.sort()
id_after_sort=id(price_list)
if id_before_sort==id_after_sort: print("ID списка не изменился")
else: print("ID списка изменился")
print('Цены по возрастанию:')
print(*[print_price(price) for price in price_list],sep=' ,')
lowest_price_list= price_list[-1:-len(price_list)-1:-1]
print('Пять самых дорогих товаров:')
print(*[print_price(price) for price in lowest_price_list[0:5]],sep=' ,')
