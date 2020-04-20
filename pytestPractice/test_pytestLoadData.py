import pytest

from pytestPractice.LogClass import LogClass


@pytest.mark.usefixtures("loaddata")
class TestSample2(LogClass):

    def test_loaddata(self,loaddata):
        log=self.getlogger()
        log.info(loaddata)
        # print(loaddata)

