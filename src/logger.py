import logging
import os
from datetime import datetime


def create_logger(name: str, log_file: str = "app.log", level: int = logging.DEBUG):
    """
    Creates a custom logger with specified name, log file, and logging level.

    Parameters:
        name (str): Name of the logger.
        log_file (str): Path to the log file. Default is "app.log".
        level (int): Logging level. Default is DEBUG.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger instance
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate logging
    logger.propagate = False

    # Create log directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # File Handler - Logs to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Console Handler - Logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Log format
    log_format = logging.Formatter(
        fmt="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Set format for both handlers
    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Example usage
if __name__ == "__main__":
    # Create a logger instance
    logger = create_logger(
        name="MyAppLogger", log_file="logs/app.log", level=logging.DEBUG
    )
    # Log messages
    logger.debug("This is a DEBUG message.")
    logger.info("This is an INFO message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
    logger.critical("This is a CRITICAL message.")
