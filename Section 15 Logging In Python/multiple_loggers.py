import logging

logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARN)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger1.debug("logger 1 debug message")
logger1.warning("logger 1 warn message")
logger1.error("logger 1 error message")
logger1.critical("logger 1 critical message")


logger2.debug("logger 2 debug message")
logger2.warning("logger 2 warn message")
logger2.error("logger 2 error message")
logger2.critical("logger 2 critical message")
