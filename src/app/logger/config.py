from pathlib import Path

from loguru import logger
from datetime import datetime
import sys


def configure_logger():
    log_folder = Path.cwd() / "log"
    log_folder.mkdir(exist_ok=True)
    root_folder = Path.cwd()
    now = datetime.now()
    log_filename = log_folder / now.strftime("log_%Y-%m-%d_%H-%M-%S.log")

    logger.remove()

    logger.add(
        log_filename,
        rotation="1 week",
        retention="1 month",
        level="INFO",
        format=lambda record: format_record(record, root_folder),
        backtrace=True,
        diagnose=True
    )

    logger.add(
        sys.stdout,
        level="DEBUG",
        colorize=True,
        format=lambda record: format_record(record, root_folder),
        backtrace=True,
    )


def format_record(record, root: Path) -> str:
    file_path = Path(record["file"].path).resolve()
    relative_path = str(file_path.relative_to(root))
    relative_path = relative_path.replace("\\", ".")
    return f"<cyan>{record['time'].strftime('%Y-%m-%d %H:%M:%S')}</cyan> | <green>{relative_path}</green> | <level>{record['message']}</level>\n"