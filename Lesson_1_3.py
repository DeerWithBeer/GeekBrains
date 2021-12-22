def completion(number): # Функция для формирования окончания
    if 10<number < 15  or number % 10 >=5 or number % 10==0:
    # Если число лежит от 11 до 14, или больше 5, или кратно 0, то окончание ОВ
        return 'ов'
    elif number % 10==1:
    # Если последняя цифира числа 1, то нулевое окончание
        return ''
    else:
    #  Во всех остальных случаях окончание а
        return 'а'


for number in range(1,101):
    print(f'{number} процент{completion(number)}')
