import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    'Базовая страница'

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ метод открытия страницы """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """ проверка доступности элемента """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """ метод проверяет, что элемент не появляется на странице в течение заданного времени """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """ метод проверяет, что элемент исчезает на странице в течение заданного времени """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """ результат математического выражения для получения проверочного кода """

        if check_alert(self.browser):
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")

    def go_to_login_page(self):
        """ метод входа для авторизации и регистрации"""
        login_link = self.browser.find_element(
            *BasePageLocators.LOGIN_LINK)
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        """ проверка ссылки для авторизации """
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_cart(self):
        """ метод переходита в корзину по кнопке из шапки сайта """
        self.browser.find_element(
            *BasePageLocators.BUTTON_VIEW_TO_CART).click()

    def should_be_authorized_user(self):
        """ метод проверки об успешной авторизации """
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"


def check_alert(browser):
    """ метод проверки отображения alert """
    try:
        browser.switch_to.alert
    except NoAlertPresentException:
        return False
    return True
