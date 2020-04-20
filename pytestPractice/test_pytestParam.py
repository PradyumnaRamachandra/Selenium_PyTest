import pytest

@pytest.mark.usefixtures("crossbrowser")
class TestSample2():
    def test_crossbrowser(self,crossbrowser):
        print(crossbrowser)