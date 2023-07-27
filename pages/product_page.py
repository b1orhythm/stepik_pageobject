from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()
        self.should_be_message_about_added_product()
        self.should_be_same_price_in_basket()


    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "\"Add to basket\" button is not presented"

    def should_be_message_about_added_product(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert product_title == self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRODUCT_TITLE).text, "The name of the added product is different from the product name on the page"

    def should_be_same_price_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE_BASKET).text, "The price of the cart does not match the price of the product"