# mouse_now.py - Отображает текущее положение курсора
import pyautogui

print('Для выхода нажмите CNTRL+C')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + \
                      ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nВыход выполнене успешно')
