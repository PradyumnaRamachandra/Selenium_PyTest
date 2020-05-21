import pytest


@pytest.fixture()
def browser_setup(self):
    print("Setup")
    yield
    print("Teardown")

@pytest.mark.usefixtures("browser_Setup")
class TestSample():


    def test_TC1(self):
        print("TC1")

    def test_TC2(self):
        print("TC2")