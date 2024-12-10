import sys

from PySide6.QtWidgets import QApplication

from frontend.desktop_app.mazes.main_window import MainWindow
from logger import configure_logger
from loguru import logger


def main():
    configure_logger()
    app = QApplication(sys.argv)
    logger.info("Инициализация приложения")
    window = MainWindow()
    logger.info("Открытие окна 'Mazes And Caves'")
    window.show()
    logger.info("Закрытие окна 'Mazes And Caves'. Выход из программы")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()