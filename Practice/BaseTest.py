import pytest
from selenium import webdriver
import time


@pytest.mark.usefixtures("browser_setup")
class TestSetup():


    @pytest.fixture()
    def browser_setup(request):
        driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.implicitly_wait(20)
        # setattr(cls,"driver",driver)
        request.driver=driver
        # request.cls.driver=driver


        yield
        time.sleep(2)
        driver.close()





