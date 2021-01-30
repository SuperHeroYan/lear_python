
"""downBitcoinAlert 2.0 - издает жеский звук если биткоинт падает.

Dependens:
    'Play_mp3' install from 'https://pypi.org/project/play-mp3/'
    'beautifulsoup4' install from 'https://pypi.org/project/beautifulsoup4/'
"""

try:
    import bs4
    import Play_mp3 as mp3
    import requests
    import os
except Exception:
    print('Ошибка! Не установлены модули "Play_mp3" и "beautifulsoup4" ')

path = os.path.abspath('bitcointDB.txt')

if os.path.exists(path):

    url = 'https://fortrader.org/quotes/bitcoinusd'
    site = requests.get(url)
    site.raise_for_status()

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    rawData = soup.select('div .rates_box1 .pid-bitcoinusd-bid')

    priceBitkoin = rawData[0].text

    if priceBitkoin:

        dataBaseReader = open('bitcointDB.txt', 'r+')
        if dataBaseReader.read() == '':
            dataBaseReader.write('111,1111')

        dataBaseReader.seek(0)
        oldPriceSTR = dataBaseReader.read()
        dataBaseReader.close()

        oldPriceFLOAT = float(oldPriceSTR[:-2].replace(',', '.').replace(' ', ''))
        currentPrice = float(priceBitkoin.replace(',', '.').replace(' ', ''))

        if currentPrice < oldPriceFLOAT:
            mp3.play('rrrr.mp3')

            # Вывод на склько биткоин подешевел
            differencePrice = str(oldPriceFLOAT - currentPrice)
            print(f'Биткоинт упал на {differencePrice}\n \
                  Текущий курс: {currentPrice}')

            # запись текущего значения биткоинта в БД
            dataBaseWriter = open('bitcointDB.txt', 'w')
            dataBaseWriter.write(str(currentPrice))
            dataBaseWriter.close()
        else:
            print(f'Растет как сука\n*******\n{str(currentPrice)}\n*******')
            # Запись в бд последней цены
            dataBaseWriter = open('bitcointDB.txt', 'w')
            dataBaseWriter.write(str(currentPrice))
            dataBaseWriter.close()
    else:
        print('No found elem')
else:
    makebd = open('bitcointDB.txt', 'w')
    makebd.close()
    print('Создалась база данных для хранения цены Биткоина.\n',
          '\n!!! Перезапустите программу !!!')
