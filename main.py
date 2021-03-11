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

import functools


def trace(func):
    # Обретка для того что бы не терять мета-данные
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
              f'с {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'ТРАССИРОВКА: {func.__name__}() '
              f'вернула {original_result!r}')
        return original_result
    return wrapper


@trace
def say(name, line):
    """Возвращает трейсбек."""
    return f'{name}: {line}'


say('Kolya', 'Jane')

print(say.__name__)
print(say.__doc__)
