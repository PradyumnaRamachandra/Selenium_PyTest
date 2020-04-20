
import logging

def test_logger():

    logger=logging.getLogger(__name__)

    filehandler=logging.FileHandler("../Logs/logfile.log")
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("Debug executed")
    logger.info("Test Executed")
    logger.warning("There is a warning")
    logger.error("There is an error")
    logger.critical("Critical Error")
