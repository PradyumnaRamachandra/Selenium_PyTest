import pytest

@pytest.fixture(scope="class")
def setup():
    print("I am executing first")
    yield
    print("I am executing Last")


@pytest.fixture()
def loaddata():
    return ["Prady","Rama","xxxx"]

@pytest.fixture(params=[("Chrome","Prady","xxxx"),("Firefox","Prady","yyyy")])
def crossbrowser(request):
    return request.param