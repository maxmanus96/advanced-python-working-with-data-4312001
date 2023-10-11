# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging


# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")

# TODO: Try out each of the log levels
logging.debug("This is a debug-level log message")
logging.info("This is an info-level log message")
logging.error("This is an error-level log message")
logging.critical("This is a critical-level log message")
logging.warning("This is a warning-level log message")

# TODO: Output formatted strings to the log
x="string"
y=10
logging.info("Here's a {} variable and an int: {}".format("string", 10))

