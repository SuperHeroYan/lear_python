# Декоратора оперкейса
def upp(func):
    def wrapper():
        orig_res = func()
        mod_res = orig_res.upper()
        return mod_res
    return wrapper


@upp
def greet():
    return 'hello'


greet()
