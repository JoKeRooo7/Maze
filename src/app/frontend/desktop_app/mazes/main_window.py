from typing import List
from loguru import logger

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from controller.maze import ControllerMaze
from frontend.desktop_app.ui import Ui_MainWindow, Ui_Dialog


# TODO поменять название классов и его методов в ui
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller_maze = ControllerMaze()

        self.btn_cave_generation.clicked.connect(self._open_dialog_window_caves)
        self.btn_choose_file.clicked.connect(self._choose_file)
        self.btn_save_maze.clicked.connect(self._save_maze)
        self.btn_generate_maze.clicked.connect(self._generate_maze)
        self.btn_solve_maze.clicked.connect(self._solve_maze)
        self.btn_ml_reinfocement.clicked.connect(self._ml_reinforcement_learning)

        self.sb_entry_x.valueChanged.connect(self._update_entry_point)
        self.sb_entry_y.valueChanged.connect(self._update_entry_point)
        self.sb_exit_x.valueChanged.connect(self._update_exit_point)
        self.sb_exit_y.valueChanged.connect(self._update_exit_point)

    def _open_dialog_window_caves(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        logger.info("Открытие окна 'Caves'")
        self.new_window.exec_()
        logger.info("Закрытие окна 'Caves'")

    def _choose_file(self):
        filter_files: str = "All Files (*);;Text Files (*.txt)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", filter_files)

        if file_path is None:
            logger.error(f"Файл не выбран")
            return

        logger.info(f"Файл для открытия выбран: {file_path}")

        try:
            rows, cols, right_walls_list, lower_walls_list = self.controller_maze.load_maze(file_path)
        except Exception as e:
            logger.error(f"Ошибка при чтении файла с лабиринтом:\n{e}")
            return

        self.window_opengl.right_walls = right_walls_list
        self.window_opengl.lower_walls = lower_walls_list

        try:
            self.window_opengl.draw_maze()
        except Exception as e:
            logger.error(f"Ошибка при отрисовке лабиринта:\n{e}")
            return

        self.sb_rows_maze.setValue(rows)
        self.sb_colm_maze.setValue(cols)

    def _save_maze(self):
        filter_files: str = "Text Files (*.txt);;All Files (*)"
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", filter_files)

        logger.info(f"Файл для сохранения лабиринта выбран: {file_path}")

        rows = self.window_opengl.rows
        cols = self.window_opengl.cols
        right_walls = self.window_opengl.right_walls
        lower_walls = self.window_opengl.lower_walls

        try:
            self.controller_maze.save_maze(file_path, rows, cols, right_walls, lower_walls)
        except Exception as e:
            logger.error(f"Ошибка при сохранении лабиринта:\n{e}")
            return

        logger.info(f"Лабиринт сохранен в {file_path}")

    def _generate_maze(self):
        row_maze: int = self.sb_rows_maze.value()
        column_maze: int = self.sb_colm_maze.value()
        logger.info(f"Размер лабиринта для генерации: {row_maze}x{column_maze}")

        right_walls_list: List[int]
        lower_walls_list: List[int]
        try:
            right_walls_list, lower_walls_list = self.controller_maze.create_maze(
                rows=row_maze,
                columns=column_maze
            )
        except Exception as e:
            logger.error(f"Ошибка при создании лабиринта: {e}")
            return

        self.window_opengl.right_walls = right_walls_list
        self.window_opengl.lower_walls = lower_walls_list

        try:
            self.window_opengl.draw_maze()
        except Exception as e:
            logger.error(f"Ошибка при отрисовке лабиринта:\n{e}")
            return

    def _solve_maze(self):
        logger.info(f"Начало поиска решения лабиринта размером {self.window_opengl.rows}x{self.window_opengl.cols}")
        logger.debug(
            f"Начальная точка {self.window_opengl.get_entry_index()} Конечка {self.window_opengl.get_exit_index()}"
        )
        try:
            result = self.controller_maze.solve_maze(
                rows=self.window_opengl.rows,
                columns=self.window_opengl.cols,
                right_walls=self.window_opengl.right_walls,
                lower_walls=self.window_opengl.lower_walls,
                entry_index=self.window_opengl.get_entry_index(),
                exit_index=self.window_opengl.get_exit_index(),
            )
        except Exception as e:
            logger.error(f"Ошибка при поиске решения лабиринта:\n{e}")
            return

    def _update_entry_point(self):
        x = self.sb_entry_x.value()
        y = self.sb_entry_y.value()
        self.window_opengl.entry_point = (x, y)

    def _update_exit_point(self):
        x = self.sb_exit_x.value()
        y = self.sb_exit_y.value()
        self.window_opengl.exit_point = (x, y)

    def _ml_reinforcement_learning(self):
        pass
