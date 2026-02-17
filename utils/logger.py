import logging
import os


class Logger:

    @staticmethod
    def get_logger():
        log_dir = "reports/logs"
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)

        # جلوگیری از duplicate handlers
        if not logger.handlers:

            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s",
                "%Y-%m-%d %H:%M:%S"
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
