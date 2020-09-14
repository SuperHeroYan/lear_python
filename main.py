# Рандомайзер для экзамена по географии
import random

# Ключи назвагте штатов а значения столицы
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
            'Idaho': 'Boie', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisina': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oaklahoma': 'Oaklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}

# Генерация 35 файлов билетов
for quizNum in range(35):

	# Создагте билетов и ответов к ним
	quizFile = open('cap/capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('cap/capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')

	#Запись заголовка билетов
	quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
	quizFile.write( (' ' * 15) + 'Проверка знаний столиц штатов (Билет %s)'
				% (quizNum + 1))
	quizFile.write('\n\n')

	#Перемешивание порядка следования столиц щтаово
	states = list(capitals.keys())
	random.shuffle(states)

	#Цикл по всем штататм с созданием вопроса к кажому
	for questionNum in range(50):

		#Получение прав и неправ ответов
		correctAnswer = capitals[states[questionNum]]
		wrongAnswer = list(capitals.values())
		del wrongAnswer[wrongAnswer.index(correctAnswer)]
		wrongAnswer = random.sample(wrongAnswer, 3)
		answerOptions = wrongAnswer + [correctAnswer]
		random.shuffle(answerOptions)
		
		#Запись вариантов ответов в файл
		quizFile.write('%s. Выберите столицу штата %s.\n' % 
			(questionNum + 1, states[questionNum]))
		quizFile.write('\n')

		for i in range(4):
			quizFile.write('%s. %s\n' % ('ABCD'[i], answerOptions[i]))
			quizFile.write('\n')

		#Запись ключа ответа в файл.
		answerKeyFile.write('%s. %s\n' % ((questionNum + 1), 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()
