
"""countdown.py Простой сценарий обратного отсчета."""

import time, subprocess

timeLeft = 60

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# Воспроизведение звук файла по оконачанию
subprocess.Popen(['see', 'alarm.wav'])
