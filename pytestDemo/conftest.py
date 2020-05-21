import pytest

@pytest.fixture()
def setup():
    print("I am Executing first")
    yield
    print("I am Executed Last")

@pytest.fixture()
def dataload():
    print("Setting up Data for Testing")
    return ["Pradyumna","Ramachandra","prady07@gmail.com"]

@pytest.fixture(params=[("Chrome","Prady","xxx"),("Firefox","Sandy"),"IE"])
def crossbrowser(request):
    return request.param