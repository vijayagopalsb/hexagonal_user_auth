# File: app/utils/logger.py
# app/utils/logger.py

import logging
import sys

def setup_logger(name: str = "hex_user_auth") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set desired level

    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(name)s: %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

