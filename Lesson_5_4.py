src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# ВЫвод через list comprehions
# Элементы берутся по индексу начиная с 1го (т.к. 0 элемент не будет выведен никогда)
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(result)
