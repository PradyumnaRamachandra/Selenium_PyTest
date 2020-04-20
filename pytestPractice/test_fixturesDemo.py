import pytest

@pytest.mark.usefixtures("setup")
class TestSample():

    def test_TC1(self):
        print("Executing Tc1")

    def test_TC2(self):
        print("Executing TC2")