from selenium import webdriver #Подключаем библиотеку Selenium
from selenium.webdriver.common.keys import Keys #Имитация нажатия клавиш на клавиатуре
import time #Для задания времени бездействия
import unittest #для исполнения юниттестов


class YandexSearch(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome() #Получаем в переменную browser указатель на браузер
        self.browser.get("https://yandex.ru/") #Переходим на нужный сайт

    def test_search_text(self):
        browser = self.browser
        search_pls = browser.find_element_by_css_selector("#text") #Ставим курсор в нужное поле(сейчас это - поле поиска)
        search_pls.send_keys("Тензор")  #пишем запрос

        time.sleep(2)

        #Проверяем наличие таблицы с подсказками
        suggest_list = browser.find_element_by_xpath("//*[@class='suggest2__content suggest2__content_theme_normal']")
        search_pls.send_keys(Keys.ENTER) #Нажимаем Enter

        time.sleep(2)

        #Проверяем наличие поисковой выдачи
        results_of_search = browser.find_element_by_xpath("//*[contains(@class, 'serp-list serp-list_left_yes')]")

        #Проверяем, что в первых 5-ти ссылка есть - tensor.ru
        result = browser.find_element_by_xpath("//*[@class = 'serp-item']//*[@href='https://tensor.ru/']")



        browser.close()



if __name__ == "__main__":
    unittest.main()






