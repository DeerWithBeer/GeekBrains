import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# Функция getjokes
# Типы аргументов указаны для избежания неправильного вызова
# Аргументы именные, так как явно указано их имя и тип, а также для одной из них указано значение по умолчанию
# Хотя именные аругменты могут использоваться и как позиционные
def getjokes(number_of_jokes: int, repeat_word: bool = True):
    if repeat_word:
        # Возращаем список шуток из случайных слов, выбирая слова с помощью функции choise модуля random
        return ['{} {} {}'.format(random.choice(nouns), random.choice(adverbs), random.choice(adjectives)) for joke in
                range(0, number_of_jokes)]
    else:
        # Мы сохраняем условие СЛУЧАЙНОГО ВЗЯТИЯ, так как фактическик аждый список перемещивается, а далее просто берём их по порядку (исключая повторения)
        # Перемешиваем списки слов для шуток
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        # Вставялем перемешанные слова в шутку и возращаем список шуток
        return ['{} {} {}'.format(nouns[joke], adverbs[joke], adjectives[joke]) for joke in range(0, number_of_jokes)]


print(getjokes(2))
