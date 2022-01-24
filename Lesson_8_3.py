def p_wrapper(func):
    def tag_wrapper(*args, **kwargs):
        args_s=[f"{arg} :{type(arg)}" for arg in args] # формируем список строк для позиционных аргументов
        # формируем список строк для именных и дополняем им список аргументов
        args_s.extend([f"{key}={value} :{type(value)}" for key, value in kwargs.items()])
        args_s=", ".join(args_s) # формируем рузльтатирующую строку
        markup = func(*args, **kwargs) #ыполняем функию
        print(f'{func.__name__}({args_s}):{type(markup)}') # выводит работа логгера
        return markup
    return tag_wrapper


@p_wrapper
def calc_cube(x,*args, **kwargs):
    return x**3


a = calc_cube(2)
print(a)
