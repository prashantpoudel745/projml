# import logging
# import os
# from datetime import datetime


# def create_logger(name: str, log_file: str = "app.log", level: int = logging.DEBUG):

#     # Create a logger instance
#     logger = logging.getLogger(name)
#     logger.setLevel(level)

#     # Prevent duplicate logging
#     logger.propagate = False

#     # Create log directory if it doesn't exist
#     log_dir = os.path.dirname(log_file)
#     if log_dir and not os.path.exists(log_dir):
#         os.makedirs(log_dir)

#     # File Handler - Logs to a file
#     file_handler = logging.FileHandler(log_file)
#     file_handler.setLevel(level)

#     # Console Handler - Logs to the console
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(level)

#     # Log format
#     log_format = logging.Formatter(
#         fmt="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S",
#     )

#     # Set format for both handlers
#     file_handler.setFormatter(log_format)
#     console_handler.setFormatter(log_format)

#     # Add handlers to the logger
#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)

#     return logger


# # Example usage
# if __name__ == "__main__":
#     # Create a logger instance
#     logger = create_logger(
#         name="MyAppLogger", log_file="logs/app.log", level=logging.DEBUG
#     )

#     # Log messages
#     logger.info("Application started.")
#     try:
#         # Intentionally trigger an exception
#         result = 10 / 0
#     except Exception as e:
#         logger.error("An exception occurred:", exc_info=True)  # Log exception details

#     logger.info("Application finished.")

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
