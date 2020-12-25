
# stopwatch.py - Прогамма хронометр

import time

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
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Замер #%s: %s (%s)' %
			(lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time()
except KeyboardInterrupt:
	print('\nГотово')
