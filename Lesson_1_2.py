def sum_number_divided_7(numbers):
    # Входной аргумент - последовательность чисел. Возращает число, если сумма цифр делится на 7, иначе возращает 0
    result = 0 # Переменная для хранения результата функции
    for number in numbers: #Для каждого числа в последовательности
        sum_of_digit = 0 #Переменаня для хранения суммы цифр (обнуление)
        digit=number #Т.к. INT Immutable, а нам нужно менять значение текущей цифры, то вводим временую переменную DIGIT
        while digit != 0: #Пока взятая цифра не равна 0
            sum_of_digit = sum_of_digit + digit % 10 #Прибавление последней цифры DIGIT к сумме цифр
            digit = digit // 10 #Отсечение последней цифры DIGIT
        if not(sum_of_digit % 7): result+=number #Прибавление числа к результату, если сумма цифр делиться нацело на 7
    return result #Возращенте резхультата


#Точка 1:
List_of_Numbers= [x**3 for x in range(1, 1001, 2)] # Формирование списка по пункту A
Result_A=sum_number_divided_7(List_of_Numbers)  # Поулчение суммы чисел, сумма цифр которых делится на 7 нацело
List_of_Numbers=[x+17 for x in List_of_Numbers] # Формирование списка по пункту B без создания нового списка, фактически путём изменения изначального
Result_B= sum_number_divided_7(List_of_Numbers)  # Получение суммы чисел, сумма цифр которых делится на 7 нацело
print("Часть A:{}".format(Result_A)) # Вывод результата по заданию A
print("Часть B:{}".format(Result_B)) # Вывод результата по заданию И
# Фактически мы можем не создавать переменные для хранения результата, а сразу выводить, и тогда код с Точка 1  будет выглядеть так:
    # List_of_Numbers= [x**3 for x in range(1,1001,2)]
    # print("Часть A:{}".format(Sum_Number_divided_Digit_7(List_of_Numbers)))
    # List_of_Numbers=[x+17 for x in List_of_Numbers]
    # print("Часть B:{}".format(Sum_Number_divided_Digit_7(List_of_Numbers)))
