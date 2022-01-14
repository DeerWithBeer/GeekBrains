tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Елена', 'Елена', 'Елена', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
nums_gen = ((tutors[i], klasses[i] if i < len(klasses) else None) for i in range(len(tutors)))
# Генерато списка по игдексу элемента, но если в листе klasses закончились элементы, то возращает None
print(type(nums_gen))
