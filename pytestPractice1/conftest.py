import pytest


@pytest.fixture()
def browser_Setup():
    print("Setup")

    yield
    print("Teardown")