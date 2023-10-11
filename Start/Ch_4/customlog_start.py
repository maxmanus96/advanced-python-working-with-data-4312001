# Demonstrate how to customize logging output

import logging

def another_function():
    logging.debug("This is a debug-level log message")

# TODO: add another function to log from
fmtstrng = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
datestrng = "%m/%d/%Y %I:%M:%S %p"
extdata = {"user":"Tom", "name":"Tommy"}
# set the output file and debug level, and
# TODO: use a custom formatting specification
logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=fmtstrng,
                    datefmt=datestrng)

logging.info("This is an info-level log message", extra=extdata)
logging.warning("This is a warning-level message", extra=extdata)
another_function()
