import logging

class LogClass():

    def getlogger(self):
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler("./Logs/logfile.log")
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

