from selenium import webdriver #Подключаем библиотеку Selenium
import time #Для задания времени бездействия
import requests #для запросов к серверу и обработки ответов




browser = webdriver.Chrome() #Получаем в переменную browser указатель на браузер
browser.get("https://yandex.ru/") #Переходим на нужный сайт

#Ищем вкладку картинки, нажимаем
search = browser.find_element_by_xpath("//*[@data-id = 'images'][@href = '//yandex.ru/images/']")
search.click()

# Проверяем, что перешли
url = browser.current_url
assert url == 'https://yandex.ru/images/', ('URL не соответствует https://yandex.ru/images/')

#Открываем первую картинку
first_image = browser.find_element_by_xpath("(//*[@class = 'cl-teaser__link'])[1]")
first_image.click()

#Проверяем, что картинка открылась
opened_image = browser.find_element_by_xpath("//*[contains(@class, 'cl-layout__wrap__i')]")
time.sleep(2)
first_img_url = browser.current_url

#Нажимаем "Вперед"
next_button = browser.find_element_by_xpath("//*[@class = 'cl-layout__nav__right']")
next_button.click()
time.sleep(2)
second_img_url = browser.current_url

#Проверяем, что картинка изменяется
if first_img_url == second_img_url:
    raise Exception('Картинка не изменилась!')

#Нажимаем "Назад"
previous_button = browser.find_element_by_xpath("//*[@class = 'cl-layout__nav__left']")
previous_button.click()
time.sleep(1)

#Проверяем, что появилась первая картинка
first_img_url_back = browser.current_url
if first_img_url != first_img_url_back:
    raise Exception('Не первая картинка!')

#Забираем url картинки
img_src = browser.find_element_by_xpath("//*[@class = 'image__image']")
attrib = img_src.get_attribute('src')

#Переходим по нему (не через Селениум, а с помощью requests)
resp = requests.get(attrib)

#Если ответ 200 - считаем, что картинка существует
if resp.status_code != 200:
    raise Exception('Что не так с источником картинки!')

browser.close()


