class cell:
    def checker(func):
        def check_type(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, cell):
                    raise TypeError(f'Ожидался {cell} получен {type(arg)}')
            return func(*args, **kwargs)

        return check_type

    def __init__(self, count=0):
        self._count = count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if isinstance(value, int):
            raise TypeError(f'Ожидался {int} получен {type(value)}')
        self._count = value

    @checker
    def __add__(self, other):
        return cell(self.count + other.count)

    @checker
    def __sub__(self, other):
        return cell(self.count - other.count)

    @checker
    def __mul__(self, other):
        return cell(self.count * other.count)

    @checker
    def __floordiv__(self, other):
        return cell(self.count // other.count)

    @checker
    def __truediv__(self, other):
        return cell(self.count // other.count)

    def make_order(self, n):
        return '\n'.join([''.join(['*' for i in range(j, j + n if j + n <= self.count else self.count)]) for j in
                          range(0, self.count, self.count // n)])


# мне  хочется побаловаться с eval, и лень писать отдельный вызов каждого оператора
operations = ['+', '-', '*', '/', '//']
cell_1 = cell(10)
cell_2 = cell(8)
for operation in operations:
    print(f'cell_1{operation}cell_2={eval(f"cell_1{operation}cell_2").count}')
print(cell(10).make_order(3))
