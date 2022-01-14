src = [2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unq = set()
tmp = set()
for el in src:
    if el not in tmp:
        unq.add(el)
    else:
        unq.discard(el)
    tmp.add(el)
unique_number = [i for i in src if i in unq]
print(unique_number)
