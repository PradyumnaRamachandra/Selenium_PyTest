import pytest

@pytest.mark.smoke
# @pytest.mark.skip

def test_FirstProgram():
    print("First Pytest")

def test_SecondProgram(setup):
    print("Good Morning")