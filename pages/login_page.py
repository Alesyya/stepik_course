import random
import string

from data import DOMAIN
from helpers import BasePage
from selenium.webdriver.common.by import By
from data.users import USER_AlESYA


class LoginPage(BasePage):
    ENTER_BUTTON_LOCATOR = "//button[@data-testid='loginButton']"
    REGISTRATION_BUTTON_LOCATOR = "//button[@class='Button-module__button Button-module__blue-inline']"
    EMAIL_LOCATOR = "//input[@type='text' and @label='Электронная почта']"
    PASSWD_LOCATOR = "//input[@type='password']"
    visible_email_locator = "//span[@class='userToolsSubtitle' and text()='lukasheviich03@gmail.com']"
    ENTER_IN_ACCOUNT_LOCATOR = "//div[text()='Войти']"
    COUNTINUE_LOCATOR = "//button[@class='Button-module__button Button-module__blue-primary']"
    OBRABOTKA_LOCATOR = "//div[@class='Button-module__buttonText' and text()='Соглашаюсь']"
    SUCCESS_MESSAGE_LOCATOR = "//h5[@class='styles_successTitle__YoP7v']"
    INVALID_MESSAGE = "//span[@class='ErrorMessage-module__message']"
    ACCOUNT_LOCATOR = "//span[@class='userToolsText']"

    def open(self):
        self.driver.get(DOMAIN)

    def click_on_enter_button(self):
        self.wait_for_visible(self.ENTER_BUTTON_LOCATOR)
        self.click_on(self.ENTER_BUTTON_LOCATOR)

    def click_on_registration_button_locator(self):
        self.wait_for_visible(self.REGISTRATION_BUTTON_LOCATOR)
        self.click_on(self.REGISTRATION_BUTTON_LOCATOR)

    def click_on_emai_locator(self):
        self.click_on(self.EMAIL_LOCATOR)

    def click_on_countinue_button_locator(self):
        self.click_on(self.COUNTINUE_LOCATOR)

    def click_on_obrabotka_locator(self):
        self.wait_for_visible(self.OBRABOTKA_LOCATOR)
        self.click_on(self.OBRABOTKA_LOCATOR)

    def click_on_success_message_locator(self):
        self.click_on(self.SUCCESS_MESSAGE_LOCATOR)

    def randletters(self, x, y, n):
        return ''.join(random.choices(string.ascii_letters, k=n))

    def enter_email_random(self):
        email_input = self.driver.find_element(By.XPATH, self.EMAIL_LOCATOR)
        email_input.clear()
        email = self.randletters('a', 'z', 3) + self.randletters('A', 'Z', 3) + "@gmail.com"
        email_input.send_keys(email)

    def assert_access_registration(self):
        assert self.driver.find_element(By.XPATH, self.SUCCESS_MESSAGE_LOCATOR).text == "Вы зарегистрированы"

    def fill_email(self, email):
        self.fill(self.EMAIL_LOCATOR, email)

    def fill_password(self, password):
        self.fill(self.PASSWD_LOCATOR, password)

    def click_on_enter_in_account_locator_for_login(self):
        self.click_on(self.ENTER_IN_ACCOUNT_LOCATOR)
        self.wait_for_invisibility_of_element_located(self.ENTER_IN_ACCOUNT_LOCATOR)

    def click_on_enter_in_account_locator(self):
        self.click_on(self.ENTER_IN_ACCOUNT_LOCATOR)

    def assert_text_success_login(self):
        self.assert_text_in_element(self.visible_email_locator, USER_AlESYA['email'])

    def assert_massage_invalid_email(self):
        self.assert_text_in_element(self.INVALID_MESSAGE, "Неправильный формат электронной почты")

    def assert_massage_no_such_account(self):
        text_in_button = self.driver.find_element(By.XPATH, self.INVALID_MESSAGE).text
        assert "Нет такого аккаунта" in text_in_button

    def login(self, user):
        self.open()
        self.click_on(self.ACCOUNT_LOCATOR)
        self.click_on_enter_button()
        self.fill_email(user['email'])
        self.fill_password(user['email'])
        self.click_on_enter_in_account_locator()