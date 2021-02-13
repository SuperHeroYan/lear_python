def apply(product, discount):
    price = int(product['цена']) * (1.0 - discount)
    assert 0 <= price <= product['цена'], 'Цена ниже нуля'
    print(price)


shoes = {'Имя': 'Туфли', 'цена': 14900}

apply(shoes, 2.0)

# Бед практис всегда возращает Труе
assert(100 == 111)

me = ('fdsfdsfdsfdsfdsf ,'
      'fsdfsdfdsfsdfsdfffffffffffffff'
      'dfsfdsfsdfsd')


# Использование Витх
with open('hello.txt') as f:
    f.close()


# Менеджер контекста
class Manage:
    def __init__(self, name):
        self.name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class Intendter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)


with Intendter() as ints:
    ints.print('Привет')
    with ints:
        ints.print('Хей')
        with ints:
            ints.print('Бонжур')
    ints.print('Эй')
