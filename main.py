import time


class TimeCount:
    def __init__(self):
        self.beginTime = 0

    def __enter__(self):
        self.beginTime = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.result = time.time() - self.beginTime
        print(f'Время выполнения: {self.result} микросек')


asss = 11
bs = 12

with TimeCount() as timer:
    concat = 'asd' + str(asss) + 'Bobeer ' + str(bs)
    # concat = f'asd{str(asss)}Bobeer {str(bs)}'
    print(concat)
