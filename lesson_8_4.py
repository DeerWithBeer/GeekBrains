def val_checker(funkс_checker):
    def _val_checker(func):
        def wrapper(*args):
            for arg in args:
                if not funkс_checker(arg): raise ValueError(f'{arg} is bad argument')
            result = func(*args)
            return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-3))
