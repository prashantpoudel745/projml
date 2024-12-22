import sys  # Provides functions and utilities for interacting with the Python runtime environment.

# Used here to get exception details using sys.exc_info().

import logging  # A built-in Python module for logging error messages, warnings, or other information.

# Used to log errors into a file (app.log), making it easier to analyze issues later.
# Configure logging
logging.basicConfig(
    filename="app.log",  # Specifies the name of the file where logs will be written.
    level=logging.ERROR,  # Only messages with the level ERROR or higher (e.g., CRITICAL) will be logged.
    # This ensures you don’t clutter the log file with unnecessary details.
    format="%(asctime)s - %(levelname)s - %(message)s",  # %(asctime)s: Adds a timestamp to the log entry
    # %(levelname)s: Indicates the severity of the message (e.g., ERROR)
    # %(message)s: The actual message being logged
)


class CustomError(Exception):
    """Custom exception class for handling specific errors."""

    def __init__(self, message):
        super().__init__(message)


def error_message_detail(error, error_detail: sys):
    """Extracts and formats detailed error information."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in file '{file_name}' at line {line_number}: {str(error)}"


def handle_error(error):
    """Handles errors by logging and optionally re-raising."""
    error_details = error_message_detail(error, sys)
    logging.error(error_details)  # Log the error
    print(
        "An error occurred. Please check the log file for more details."
    )  # Notify the user


# Example Usage
try:
    # Intentionally trigger an error
    x = int("invalid")
except Exception as e:
    handle_error(e)
