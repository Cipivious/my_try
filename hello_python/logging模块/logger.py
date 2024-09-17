import logging

logger = logging.getLogger("applog")
logger.setLevel(logging.DEBUG)

consoleHander = logging.StreamHandler()
consoleHander.setLevel(logging.WARNING)

fileHander = logging.FileHandler(filename="new_demo.log")

formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
flt = logging.Filter("appm")
consoleHander.setFormatter(formatter)
fileHander.addFilter(flt)
fileHander.setFormatter(formatter)

logger.addHandler(consoleHander)
logger.addHandler(fileHander)

logger.debug("this is a debug log")
logger.info("this is an info log")
logger.warning("this ia a warning log")
logger.error("this is an error log")
logger.critical("this is a critical log")
