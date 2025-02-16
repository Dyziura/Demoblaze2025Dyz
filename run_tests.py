import unittest
from Tests.login_tests import LoginTest

# Ładujemy testy do Test Suity - klasa TestLoader
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Lista testów do uruchomienia
tests_for_run = [
    login_tests,
    # ...
    # ...
]

# Łączymy testy w Test Suit
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)