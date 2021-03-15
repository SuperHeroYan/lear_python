# # Декоратора оперкейса
# def lows(func):
#     def wrapper():
#         orig_res = func()
#         mod_res = orig_res.lower()
#         return mod_res
#     return wrapper
#
#
# def upp(func):
#     def wrapper():
#         orig_res = func()
#         mod_res = orig_res.upper()
#         return mod_res
#     return wrapper
#
#
# @upp
# @lows
# def greet():
#     return 'qwerty'
#
#
# print(greet())

# import functools


# def trace(func):
#     # Обретка для того что бы не терять мета-данные
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
#               f'с {args}, {kwargs}')
#         args = args + ('sex',)
#         original_result = func(*args, **kwargs)

#         print(f'ТРАССИРОВКА: {func.__name__}() '
#               f'вернула {original_result!r}')
#         return original_result
#     return wrapper


# @trace
# def say(name, line, val):
#     """Возвращает трейсбек."""
#     return f'{name}: {line} {val}'


# say('Kolya', 'Jane')

# print(say.__name__)
# print(say.__doc__)


# def psrint(x, y, z):
#     print('<%s, %s, %s>' % (x, y, z))


# tro = ('sex', 'bex', 'bexs')
# bro = {'x': 'sex', 'y': 'bex', 'z': 'bexs'}

# psrint(**bro)

# Методы форматирования строки ввыода из класса __str__ __repr__
class Car():
    def __init__(self, color, mil):
        self.color = color
        self.mil = mil
    """Репр для разработчиков они выводят однозначную информацию."""
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mil!r})')

    """Стр для пользователя удобочитаемые."""
    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.mil!r})')


car = Car('red', 2282)
print(car)
