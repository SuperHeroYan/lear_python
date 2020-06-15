def collatz(num):
    if num % 2 == 0:
        print('Число ',num,' четное')
        return num % 2
    elif num % 2 == 1:
        print('Число ',3 * num + 1,' нечетное')
        return 3 * num + 1

print('Введите число')

res = 0

while res != 1:
    answer = int(input())
    res = collatz(answer)