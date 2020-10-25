
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://vk.com/')

email = browser.find_element_by_id('index_email')
password = browser.find_element_by_id('index_pass')
button = browser.find_element_by_id('index_login_button')

try:
	print('Входим в аккаунт..')
	email.send_keys('***')
	password.send_keys('***')
	button.click()
	print('Добро пожаловать !')
except:
	print('Не удалось войти в аккаунт')

# Проверяет загрузилась ли страница
try:
	wait = WebDriverWait(browser, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, 'l_msg')))
except:
	print('Не загрузилась')

browser.get('https://vk.com/im')
# Отправляем сообщение серьге
chatid = browser.find_element_by_css_selector('[data-list-id="****"]')
chatinput = browser.find_element_by_id('im_editable0')

chatid.click()
chatinput.send_keys('****')
chatinput.send_keys(Keys.ENTER)