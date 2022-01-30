from abc import abstractmethod, ABC


class Cloth(ABC):
    def __init__(self, name=None, type=None):
        self.name = name
        self.__type = type

    @abstractmethod
    def get_size(self):
        pass


class suit():
    def __init__(self, h=0, name='Пальто'):
        super().__init__()
        self.name = name
        self.type = 'Пальто'
        self.h = h

    @property  # делаем h методом-свойством
    def h(self):
        return self.__h

    @h.setter  # создаём setter, чтобы h всегда была положительна
    def h(self, H):
        self.__H = H if H >= 0 else abs(H)

    def get_size(self):
        return (self.h * 2 * 0.3)


class coat():
    def __init__(self, V=0, name='Пальто', ):
        super().__init__()
        self.name = name
        self.type = 'Пальто'
        self.v = V

    @property  # делаем v методом-свойством
    def v(self):
        return self.__v

    @v.setter  # создаём setter, чтобы v всегда была положительна
    def v(self, V):
        self.__v = V if V >= 0 else abs(V)

    def get_size(self):
        return (self.v / 6.5 + 0.5)


order = [suit(5), coat(5)]
size_of_order = 0
for item in order:
    print(f'{item.name} имеет размер {item.get_size()}')
    size_of_order += item.get_size()
print(size_of_order)
