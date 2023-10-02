import unittest
from tests.base_test import BaseTest
from pages.home_page import *


class HomeTest(BaseTest):

    def test_check_items(self):
        page = HomePage(self.driver)
        all_elements_shown = page.check_page_loaded()
        self.assertTrue(all_elements_shown)

    def test_valid_search(self):
        page = HomePage(self.driver)
        search_result = page.search_with_valid_dates()
        self.assertTrue(page.check_valid_search_result(search_result))

    def test_valid_promotion_code(self):
        page = HomePage(self.driver)
        search_result = page.search_with_valid_promotion_code()
        print("SEARCH_RESULT: ", search_result)
        self.assertTrue(page.check_valid_promotion_result(search_result))
