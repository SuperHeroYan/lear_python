
# quieckWeather - Вывод погоды на несклько дней
import sys, json, requests

appid = 'fc6db0aefab0febb25a54174bf9ce65f'
# Определение название населенного пунката из cmd
if len(sys.argv) < 2:
	print('Использование: QueckWeather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])

# Заполс на сайт за погодой
url = 'https://api.openweathermap.org/data/2.5/weather/daily?q=%s&cnt=3&appid=%s'\
	% (location, appid)
response = requests.get(url)
response.raise_for_status()

# Загрузка JSON-данных в переменную Python
weatherData = json.loads(response.text)
w = weatherData['list']
print('Погода сегодня в %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()

print('Завтра:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()

print('Послезавтра:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
