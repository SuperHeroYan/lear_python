import random

secret_num = random.randint(1,20)
print('Я задумал число от 1 до 20, попробуй угадай суука!!')

for guesTaken in range(1,7):
    print('Ваш вариант')
    guess = int(input())

    if guess < secret_num:
        print('Число меньше задуманого')
    elif guess > secret_num:
        print('Число больше задуманого')
    else:
        break

if guess == secret_num:
    print('Верно, угадал с ',str(guesTaken),'поптыки')
else:
    print('Неа, было число', str(secret_num))