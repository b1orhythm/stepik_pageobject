from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_PRODUCTS_LIST), "Product list displayed"

    def should_be_text_about_what_basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty"
