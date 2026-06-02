import logging
from pathlib import Path

LOG_DIR = Path("logs")

LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("laf_ai")

if not logger.handlers:

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(LOG_DIR / "laf_ai.log", encoding="utf-8")

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


def log_generation(business, ai_mode):

    logger.info(f"Generation | Business={business} | Mode={ai_mode}")


def log_error(error):

    logger.error(f"Error | {error}")


def log_provider(provider):

    logger.info(f"Provider={provider}")
