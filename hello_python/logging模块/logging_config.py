import logging
import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger("applog")

logger.debug("this is a debug log")
logger.info("this is an info log")
logger.warning("this ia a warning log")
logger.error("this is an error log")
logger.critical("this is a critical log")
