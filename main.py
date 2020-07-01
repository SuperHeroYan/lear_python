# pw.py - Программа для  установки звездочек
import sys, pyperclip

text = pyperclip.paste()
# Разделяет строку на список и добавляет звезды в начало
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
