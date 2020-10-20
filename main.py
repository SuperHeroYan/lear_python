
# mapInt prog запускает карту в браузере

import sys, pyperclip
import webbrowser

if len(sys.argv) > 1:
	addres = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
