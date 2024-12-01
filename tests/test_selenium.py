from selenium import webdriver
import unittest
from unittest import TestCase


class TestAuthYAwithSelenium(TestCase):
    def setUp(self):
        self.url = 'https://passport.yandex.ru/auth/'
        self.browser = webdriver.Chrome()
        self.connection = self.browser.get(self.url)

    def tearDown(self):
        self.browser.quit()

    def test_auth_ya_find_login_field(self):
        name_input = self.browser.find_element('id', 'passp-field-login')
        self.assertEqual(name_input.tag_name, 'input')

    def test_auth_ya_find_login_input_button(self):
        button = self.browser.find_element('id', 'passp:sign-in')
        self.assertEqual(button.tag_name, 'button')

    def test_auth_ya_send_login(self):
        name_input = self.browser.find_element('id', 'passp-field-login')
        name_input.send_keys('79158732788@yandex.ru')
        name_input = self.browser.find_element('id', 'passp-field-login')
        self.assertEqual(name_input.get_property('value'), '79158732788@yandex.ru')
