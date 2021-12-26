input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
result = ""
while i < len(input_list):
    if (input_list[i].startswith(('+', '-')) and input_list[i][1:].isdigit()) or input_list[i].isdigit():
        input_list[i] = input_list[i].zfill(2 + 0 ** (abs(input_list[i].find('-') + input_list[i].find('+') + 1)))
        input_list.insert(i, '"')
        i += 1
        input_list.insert(i + 1, '"')
        i += 1
    i += 1
i = 0
while i < len(input_list) - 1:
    result += input_list[i]
    if (((input_list[i].startswith(('+', '-')) and input_list[i][1:].isdigit()) or input_list[i].isdigit()) or
        input_list[i] == '"') != True:
        result += ' '
    i += 1
result += input_list[i]
print(result)
