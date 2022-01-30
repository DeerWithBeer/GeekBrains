
class Matrix:
    def __init__(self, lines=[]):
        self.items = lines

    def __setitem__(self, key, value):
        if not isinstance(key,tuple):
            raise TypeError (f'Ожидался {tuple}, получен {type(key)}')
        self.__items[key[0]][key[1]]=value
    def __getitem__(self, item):
        if not isinstance(item,tuple):
            raise TypeError(f'Ожидался {tuple}, получен {type(item)}')
        return self.__items[item[0]][item[1]]

    @property
    def collumns(self):
        return self.__collumns
    @property
    def rows(self):
        return self.__rows
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, lines=[]):
        if not isinstance(lines, list):
            raise TypeError (f'Ожидался {list}, получен {type(lines)}')
        for line in lines:
            if not isinstance(line, list):
                raise TypeError (f'Ожидался {list}, получен {type(line)}')
        self.__items = lines
        if len(lines)!=0:
            self.__collumns= len(lines[0])
            self.__rows=len(lines)
        else:
            self.__collumns =0
            self.__rows = 0
        for line in  self.__items:
            if len(line)!=self.__collumns:
                raise ValueError(f'Несовпадающие размеры строк')
    def __len__(self):
        return self.__collumns
    def __str__(self):
        return '\n'.join([f'|{",".join(map(str,line))}|' for line in self.__items])
    def __add__(self, other):
        if not isinstance(other,Matrix):
            raise TypeError (f'Ожидался {Matrix}, получен {type(other)}')
        if self.rows!=other.rows:
            raise ValueError(f'Несовпадение количества строк')
        if self.collumns!=other.collumns:
            raise ValueError(f'Несовпадение длины строк')
        return Matrix([[self[i,j]+other[i,j] for j in range(self.__collumns)] for i in range(self.__rows)])
test=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(test+test+test)

