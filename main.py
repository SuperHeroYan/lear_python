
# Програма которая открывает несколько первых вкладок из google

import requests, sys, webbrowser, bs4

print('Гуглим...')

res = requests.get('https://yandex.ru/search/?text=' +
	' '.join(sys.argv[1:]))

res.raise_for_status()

# Извелечение первых ссылко
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Отдельное отркытие для каждой вкладки
linkElems = soup.select('ul.search-result')
numOpen = min(5, len(linkElems))


for i in range(numOpen):
	print('Открыта')
	webbrowser.open('http://google.com' + linkElems[i].get('href'))