# mouse_now.py - Отображает текущее положение курсора
import pyautogui
print('Для выхода нажмите CNTRL+C')

try:
    while True:
        x, y = pyautogui.position()
        pixel_color = pyautogui.screenshot().getpixel((x, y))

        positionStr = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)} RGB: ({str(pixel_color[0]).rjust(3)}, {str(pixel_color[1]).rjust(3)}, {str(pixel_color[2]).rjust(3)})'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nВыход выполнене успешно')
