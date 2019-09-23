from selenium import webdriver #Подключаем библиотеку Selenium
from webdriver_manager.chrome import ChromeDriverManager #должен подрубать вебдрайвер хрома
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys #Имитация нажатия клавиш на клавиатуре

from selenium.webdriver.common.keys import Keys
from .locators import *




class SearchPage():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://yandex.ru/")  # Переходим на нужный сайт

    def check_search_box(self):
        #Ставим курсор в нужное поле(сейчас это - поле поиска)
        try:
            self.browser.find_element(*LocatorsPage.search_box)
            return True
        except NoSuchElementException:
            return False



    def enter_tensor_in_search_box(self, text):
        # пишем запрос
        return self.browser.find_element(*LocatorsPage.search_box).send_keys(text)
        #self.find_element(*LocatorsPage.search_box).send_keys(text)

    def check_search_result(self):
        # Проверяем наличие таблицы с подсказками
        return self.browser.find_element(*LocatorsPage.search_suggest)
        #self.is_element_present(*LocatorsPage.search_suggest)

    def button_enter(self):
        #Нажимаем Enter и Проверяем наличие поисковой выдачи
        self.browser.find_element(*LocatorsPage.search_box).send_keys(Keys.ENTER)
        #self.is_element_present(*LocatorsPage.table_result)

    def click_tensor_link(self):
        # Проверяем, что есть ссылка - tensor.ru
        self.browser.find_element(*LocatorsPage.valid_link).click()
