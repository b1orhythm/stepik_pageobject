from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_TITLE = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class='price_color']")
    BASKET_PRICE = (By.XPATH, "//div[contains(@class, 'basket-mini')]")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form")
    MESSAGE_WITH_PRODUCT_TITLE = (By.XPATH, "//div[contains(@class, 'alert-success')]/div[@class='alertinner ']/strong")
    MESSAGE_WITH_PRICE_BASKET = (By.XPATH, "//div[contains(@class, 'alert-info')]/div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div/div[contains(@class, 'alert-success')][1]/div[@class='alertinner ']")

