from Tests.base_test import BaseTest
from time import sleep

class LoginTest(BaseTest):
    def setUp(self):
        super().setUp() #wywołanie z klasy nadrzędnej
        # dodatkowy warunek wstępny - wejście na stronę logowania
        self.login_page = self.home_page.click_log_in()
        #sleep(4)

    def testEmptyLogin(self):
        # (nie wpisujemy nic)
        # 1. kliknij LogIn
        self.login_page.click_log_in()
        # Sprawdź, czy pojawił się alert: "Please fill out Username and Password."
        self.assertEqual("Please fill out Username and Password.", self.login_page.get_alert_message())
        self.login_page.confirm_alert()
        sleep(2)

    def testValidLogin(self):
        username = "tester_alk"
        # 1. Wpisz login
        self.login_page.enter_username("tester_alk")
        # 2. Wpisz hasło
        self.login_page.enter_password("haslo")
        # 3. Kliknij Log In
        self.login_page.click_log_in()
        # 4. zmiana Log in na Log out // czy jest "Welcome tester_alk"
        welcome_text_act = self.home_page.get_welcome_username_text()
        self.assertEqual(f"Welcome {username}", welcome_text_act)
        # 5. (Sprawdź czy można kliknąć LogOut)
        sleep(1.5)