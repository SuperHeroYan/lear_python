def collatz(num):
    if num % 2 == 0:
        print('Число ',num,' четное')
        return num % 2
    elif num % 2 == 1:
        print('Число ',3 * num + 1,' нечетное')
        return 3 * num + 1

print('Введите число')


while True:
    answer = int(input())
    res = collatz(answer)
    if res == 1:
        break
    else:
        continue