import logging

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

## log messages with different severity levels
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical messgae")
