
"""stopwatch_vers_2.py - Прогамма хронометр."""

import time
import pyperclip

# Отображение инструкции по использовани. прогаммы.
print('Чтобы неачать отсчет, нажмите клавигу Enter. \nДля выхода <ctrl+c>')
input()

print('Отсчет начат')
startTime = time.time()

lastTime = startTime
lapNum = 1

# Отслежевание замеров
try:
    while True:
        input()
        lapTime = str(round(time.time() - lastTime, 2))
        totalTime = str(round(time.time() - startTime, 2))

        result = 'Замер # ' + str(lapNum) + ':' + \
            totalTime.rjust(len(totalTime) + 2) + \
            ' (' + lapTime.rjust(len(lapTime) + 4) + ')'
        print(result)

        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    pyperclip.copy(result)
    print('\nГотово')
