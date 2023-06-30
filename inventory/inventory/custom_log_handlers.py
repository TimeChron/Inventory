import logging.handlers
from pathlib import Path
import os

# BASE LOG DIRECTORY
LOG_FILE_PATH = Path(__file__).resolve().parent.parent

# Function to create log file if it doesn't exist
def create_log_file(log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    open(log_file, 'a').close()

# Function to set app log file
def set_app_log_file(logger_name, filename):
    logger = logging.getLogger(logger_name)
    handler = logger.handlers[0]  # Assumes only one handler is defined
    log_file = handler.baseFilename

    if not os.path.exists(log_file):
        create_log_file(log_file)

    handler.baseFilename = filename
    handler.stream = open(filename, 'a')

# Define the AppFileHandler class outside of the logging configuration
class AppFileHandler(logging.handlers.RotatingFileHandler):
    def __init__(self, filename, *args, **kwargs):
        full_filename = os.path.join(LOG_FILE_PATH, filename)
        create_log_file(full_filename)
        super().__init__(full_filename, *args, **kwargs)

    def emit(self, record):
        try:
            record.msg = f"[AF] {record.msg}"
            super().emit(record)
        except Exception:
            self.handleError(record)

