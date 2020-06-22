def preobraz(some):
    some[-1] = 'and ' + some[-1]
    kekes = ", ".join(some)
    return kekes

spam = ['apples','banana', 'qugirt','koper']

print(preobraz(spam))