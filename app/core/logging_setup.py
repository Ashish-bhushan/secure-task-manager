import logging
import sys
from pythonjsonlogger import jsonlogger

def setup_logging():
    # Create a logger with name "app"
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)  # Show ALL log levels

    # Handler = where to SEND the logs (terminal in our case)
    handler = logging.StreamHandler(sys.stdout)

    # Formatter = what FORMAT the log should be in
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

# Create the logger object
# We import THIS in all files: from app.core.logging_setup import logger
logger = setup_logging()