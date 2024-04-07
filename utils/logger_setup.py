import logging
import datetime
import os


def setup_logger():
    # generate filename with date nof{} datetime.datetime.now()
    generate_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_directory = "logs"
    log_application = f"{log_directory}/application-{generate_date}"
    log_info = f"{log_application}/info"
    log_debug = f"{log_application}/debug"
    log_error = f"{log_application}/error"

    # Check if logs directory exists, if not, create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Check if application directory exists, if not, create it
    if not os.path.exists(log_application):
        os.makedirs(log_application)

    # Check if info directory exists, if not, create it
    if not os.path.exists(log_info):
        os.makedirs(log_info)

    # Check if debug directory exists, if not, create it
    if not os.path.exists(log_debug):
        os.makedirs(log_debug)

    # Check if error directory exists, if not, create it
    if not os.path.exists(log_error):
        os.makedirs(log_error)

    # Create handler for each log level
    info_handler = logging.FileHandler(f"{log_info}/{generate_date}-info.log")
    debug_handler = logging.FileHandler(f"{log_debug}/{generate_date}-debug.log")
    error_handler = logging.FileHandler(f"{log_error}/{generate_date}-error.log")

    # Set log levels for each handler
    info_handler.setLevel(logging.INFO)
    debug_handler.setLevel(logging.DEBUG)
    error_handler.setLevel(logging.ERROR)

    # Set format for each handler
    formatter_info = logging.Formatter("%(asctime)s info %(message)s")
    formatter_debug = logging.Formatter("%(asctime)s debug %(message)s")
    formatter_error = logging.Formatter("%(asctime)s error %(message)s")
    info_handler.setFormatter(formatter_info)
    debug_handler.setFormatter(formatter_debug)
    error_handler.setFormatter(formatter_error)

    # Create logger object
    logger = logging.getLogger()

    # Add handlers to the logger
    logger.addHandler(info_handler)
    logger.addHandler(debug_handler)
    logger.addHandler(error_handler)

    # Now we are going to Set the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    return logger
