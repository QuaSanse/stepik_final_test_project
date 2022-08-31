from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "form#login_form")
    FORM_REGISTER = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSEGE_ADDAD_TO_BASKET = (
        By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSEGE_BASKET_TOTAL = (
        By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    # MESSEGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div.alert-info > div > p:nth-child(1) > strong")

    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    PRODUCT_NAME_IN_MESSEGE = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    PRODUCT_MESSEGE_TEXT = (
        By.XPATH, "//*[@id='messages']/div[1]/div/text()[2]")

    PRICE_PRODUCT_ON_PAGE = (By.CSS_SELECTOR, "div.col-sm-6 p.price_color")
    PRICE_PRODUCT_IN_MESSEGE = (By.CSS_SELECTOR, ".alertinner p strong")
