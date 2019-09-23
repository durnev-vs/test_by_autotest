from selenium import webdriver #Подключаем библиотеку Selenium
#from selenium.webdriver.common.keys import Keys #Имитация нажатия клавиш на клавиатуре
#import time #Для задания времени бездействия
import unittest
from .pages.functions import *
from webdriver_manager.chrome import ChromeDriverManager #должен подрубать вебдрайвер хрома
#from .pages.locators import *



class YandexSearch(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("https://yandex.ru/") #Переходим на нужный сайт

    def test_search_link_tensor(self):
        page = SearchPage()
        page.check_search_box() #Ставим курсор в нужное поле(сейчас это - поле поиска)
        page.enter_tensor_in_search_box("Тензор") #Пишем запрос
        page.check_search_result()  #Проверяем наличие таблицы с подсказками
        page.button_enter() #Нажимаем Enter
        page.click_tensor_link()  #Проверяем, что есть ссылка - tensor.ru




        # def test_search_text(self):
    #     browser = self.browser
    #     search_pls = browser.find_element_by_css_selector("#text") #Ставим курсор в нужное поле(сейчас это - поле поиска)
    #     search_pls.send_keys("Тензор")  #пишем запрос
    #
    #     time.sleep(2)
    #
    #     #Проверяем наличие таблицы с подсказками
    #     suggest_list = browser.find_element_by_xpath("//*[@class='suggest2__content suggest2__content_theme_normal']")
    #     search_pls.send_keys(Keys.ENTER) #Нажимаем Enter
    #
    #     time.sleep(2)
    #
    #     #Проверяем наличие поисковой выдачи
    #     results_of_search = browser.find_element_by_xpath("//*[contains(@class, 'serp-list serp-list_left_yes')]")
    #
    #     #Проверяем, что есть ссылка - tensor.ru
    #     result = browser.find_element_by_xpath("//*[@class = 'serp-item']//*[@href='https://tensor.ru/']")



        browser.close()



if __name__ == "__main__":
    unittest.main()






