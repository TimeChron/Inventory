from .custom_log_handlers import AppFileHandler, LOG_FILE_PATH
import os

# Log Configuration
def configure_logger():
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '%(name)-12s %(levelname)-8s %(message)s'
            },
            'app-file': {
                'format': '%(asctime)s %(funcName)s%(name)-12s %(levelname)-8s %(message)s'
            },
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'app_file': {
                'level': 'DEBUG',
                'class': 'inventory.custom_log_handlers.AppFileHandler',
                'filename': str(os.path.join(LOG_FILE_PATH, 'inventory.log')),
                'maxBytes': 1024 * 1024 * 5,
                'backupCount': 5,
                'formatter': 'app-file',
            },
        },
        'loggers': {
            'inventory': {
                'handlers': ['app_file', 'console'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }
    return LOGGING_CONFIG
