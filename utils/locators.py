from selenium.webdriver.common.by import By


class MainPageLocators(object):
    departing_picker = (By.ID, 'departing')
    returning_picker = (By.ID, 'returning')
    promotion_text_box = (By.ID, 'promotional_code')
    search_button = (By.XPATH, '//*[@id="content"]/form/dl[4]/dd/input')
    search_result = (By.ID, 'content')
    logo = (By.LINK_TEXT, 'MarsAir')
    background_image = (By.ID, 'app')
