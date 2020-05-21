import time

from Practice.BaseTest import TestSetup


class TestSample(TestSetup):

    def test_TC1(self):
        # time.sleep(3)
        self.driver.find_element_by_name("name").send_keys("abc")
        self.driver.find_element_by_name("email").send_keys("abc@email.com")

    def test_TC2(self):
        # time.sleep(3)
        self.driver.find_element_by_name("name").send_keys("xyz")
        self.driver.find_element_by_name("email").send_keys("abc@email.com")