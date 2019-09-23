from selenium.webdriver.common.by import By


class LocatorsPage(object):
    search_box          = (By.ID, "text")
    search_suggest      = (By.XPATH, "//*[@class='suggest2__content suggest2__content_theme_normal']")
    table_result        = (By.CLASS_NAME, "content__left")
    valid_link          = (By.XPATH, "//*[@class = 'serp-item']//*[@href='https://tensor.ru/']")

















