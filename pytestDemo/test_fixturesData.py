import pytest

@pytest.mark.usefixtures("dataload")
class TestExample2():

    def test_ProfileData(self,dataload):
        print(dataload)