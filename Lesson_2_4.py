input_list=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for word in input_list:
    print(f"Привет, {word[word.rfind(' ')+1:].capitalize()}")