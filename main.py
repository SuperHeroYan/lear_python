
"""multidownloadXkcd00.py - Downloads XKCD comics using multiple threads."""

import bs4
import os
import requests
import sys
import threading

os.makedirs('xkcd', exist_ok=True)     # Store comics in XKCD


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        try:
            url = 'http://xkcd.com/%s/' % (url_number)
            # Download the page
            print('Downloading page %s...' % url)
            res = requests.get(url)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'html.parser')

            # Find the URL of the comic image.
            # Only select img within element with id attribute set to comic
            comic_elem = soup.select('#comic img')
            if comic_elem == []:
                print('Could not find comic image.')
            else:
                comic_url = 'http:' + comic_elem[0].get('src')
                # Download the image.
                print('Downloading the image %s...' % (comic_url))
                res = requests.get(comic_url)
                res.raise_for_status()

                # Save the image to xkcd
                with open(os.path.join('xkcd',
                                       os.path.basename(comic_url)),
                          'wb') as image_file:
                    for chunk in res.iter_content(100000):
                        image_file.write(chunk)
        except Exception:
            print('Error: ', sys.exc_info()[0], ' - ', sys.exc_info()[1])


# Создание и щапуску потоков
dowloadThreads = []
for i in range(0, 1400, 100):
    dowloadThread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    dowloadThreads.append(dowloadThread)
    dowloadThread.start()

# Ожидание всех потоков
for dowloadThread in dowloadThreads:
    dowloadThread.join()
print('Готов.')
