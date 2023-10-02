from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        check_list = []
        check_list.append(True) if self.wait_element(*self.locator.returning_picker) else False
        check_list.append(True) if self.wait_element(*self.locator.departing_picker) else False
        check_list.append(True) if self.wait_element(*self.locator.promotion_text_box) else False
        check_list.append(True) if self.wait_element(*self.locator.search_button) else False
        check_list.append(True) if self.wait_element(*self.locator.logo) else False
        check_list.append(True) if self.wait_element(*self.locator.background_image) else False
        return all(check_list)

    def search_with_valid_dates(self):
        depart_date = 1
        return_date = 6
        return self.search_with_date(depart_date, return_date)

    def search_with_valid_promotion_code(self):
        promotion_code = "XX3-XXX-418"
        depart_date = 1
        return_date = 6
        promotion_textbox = self.find_element(*self.locator.promotion_text_box)
        promotion_textbox.send_keys(promotion_code)
        result = self.search_with_date(depart_date, return_date)
        return result

    def search_with_date(self, depart_date, return_date):
        select_depart_date = Select(self.find_element(*self.locator.departing_picker))
        select_depart_date.select_by_index(depart_date)

        select_return_date = Select(self.find_element(*self.locator.returning_picker))
        select_return_date.select_by_index(return_date)

        search_button = self.find_element(*self.locator.search_button)
        search_button.click()

        result = self.find_element(*self.locator.search_result)
        paragraphs = result.find_elements(By.TAG_NAME, "p")
        paragraph_texts = []
        for paragraph in paragraphs:
            paragraph_texts.append(paragraph.text)
        result_text = " ".join(paragraph_texts)

        return result_text

    @staticmethod
    def check_valid_search_result(result):
        if "Seats available!" in result \
                or "Sorry, there are no more seats available." in result:
            return True
        else:
            return False

    @staticmethod
    def check_valid_promotion_result(result):
        if "discount!" in result:
            return True
        else:
            return False
