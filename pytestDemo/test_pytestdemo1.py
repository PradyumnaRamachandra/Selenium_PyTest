import pytest

def test_TC1():
    msg="Hello"
    assert msg=="Test","Test Failed since not equal"

@pytest.mark.smoke
def test_TC2(setup):
    a=4
    b=6
    assert a+2==6,"Test failed since addition not equal"