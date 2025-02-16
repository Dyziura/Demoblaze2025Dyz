from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPageLocators:
    LOG_IN_BUTTON = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]') # //button[@onclick="logIn()"]
    USERNAME_INPUT = (By.ID, 'loginusername')
    PASSWORD_INPUT = (By.ID, 'loginpassword')

class LoginPage(BasePage):
    """
    Login page object
    """
    def enter_username(self, username):
        """
        Enters username
        :param username:
        """
        el = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
        el.send_keys(username)

    def enter_password(self, password):
        """
        Enters password
        :param password:
        """
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_log_in(self):
        """
        Waits max 5 seconds for Log in button and clicks it
        """
        el = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.click()

    def get_alert_message(self):
        """
        Wait max 5 seconds for alert and returns its text
        :return: alert text
        """
        self.wait_5s.until(EC.alert_is_present())
        return self.alert.text

    def confirm_alert(self):
        """
        Confirms alert (Clicks OK)
        """
        self.alert.accept()

    def _verify_page(self):
        print("Weryfikacja strony logowania")
        self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.USERNAME_INPUT))
        self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
        log_in_button = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(log_in_button))

