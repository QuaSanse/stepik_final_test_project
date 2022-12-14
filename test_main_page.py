from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest

# главная страница
link_main_page = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_guest_can_go_to_login_page(self, browser):
        # Гость открывает главную страницу
        page = MainPage(browser, link_main_page)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_guest_should_see_login_link(self, browser):
        # Гость открывает главную страницу
        page = MainPage(browser, link_main_page)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    page = MainPage(browser, link_main_page)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_cart()
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_no_items_in_the_cart()
