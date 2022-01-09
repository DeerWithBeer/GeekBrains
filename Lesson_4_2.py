import datetime  # Библиотека для работы со временем

import requests  # Библиотека для работы со запросами типа GET и POST


def currency_rates(code_name_in):
    if code_name_in==None:
        print("Не задан код валюты") # На случай вызова без аргументов
        exit(1)
    code = str(code_name_in).upper() # приводим аргумент к верхне му регистру
    code = code.replace('{', '').replace("'", '').replace('}', '')
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")  # Запрашиваем страницу с курсами
    if (response.status_code != 200):   # Проверяем доступна ли страница
        print("Ошибка подключаения")
        exit(2)
    response = response.text   # Получаем содержимое страницы
    position = response.find(f'<CharCode>{code}</CharCode>')   # Ищещ ту часть XML где описана требуемая валюта
    if position == -1: # Если такой участок не найден, то выдаём ошибку
        print("Неверный код валюты")
        return None
    # Поиск значения валюты от позиции кода валюты
    position = [response.find('<Value>', position) + 7, response.find('</Value>', position)]
    # Здесь мы извлекаем дату запроса из заголовка XML файла и перевёд в ормат даты
    date_of_curse = response[response.find('" name') - 10:response.find('" name')]
    date_of_curse = datetime.datetime.strptime(date_of_curse, '%d.%m.%Y').date()
    # Получаем значение курса валюты и приводим к float
    value=float(response[position[0]:position[1]].replace(',', '.'))
    # Возращаем кортеж из курса в виде float и date
    return (value, date_of_curse)

#Если модуль вызван как основной (через командную строку например)
if __name__ == '__main__':
    import sys
    # На случай вызова без аргументов
    if len(sys.argv)<2:
        print("Не задан код валюты")
        exit(1)
    # То взять первый переданный аргумент в переменную мфе
    var = sys.argv[1]
    # Вызвать функцию currency_rates с входным аргументом и напечатать результат
    print(f'Курс {var}:{currency_rates({var})[0]} на {currency_rates({var})[1]}')
