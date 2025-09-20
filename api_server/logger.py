import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging(log_dir="logs", log_file="app.log", level=logging.INFO):
    """
    Sets up the logging configuration for the application.

    Args:
        log_dir (str): Directory where log files will be stored.
        log_file (str): Name of the log file.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_filepath = os.path.join(log_dir, log_file)

    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create file handler (rotating)
    # Max 5MB per file, keep 5 backup files
    file_handler = RotatingFileHandler(log_filepath, maxBytes=5 * 1024 * 1024, backupCount=5)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Example usage (can be removed or modified based on how you want to initialize)
if __name__ == "__main__":
    logger = setup_logging()
    logger.info("Logger initialized successfully.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
