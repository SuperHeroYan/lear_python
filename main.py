def collatz(num):
    if num % 2 == 0:
        print('Число ',num,' четное')
    elif num % 2 == 1:
        print('Число ',3 * num + 1,' нечетное')

print('Введите число')
answer = int(input())

collatz(answer)