from typing import Tuple, List

from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import (
    glClearColor,
    glClear,
    GL_COLOR_BUFFER_BIT,
    glOrtho,
    glMatrixMode,
    GL_PROJECTION,
    GL_MODELVIEW,
    glLoadIdentity,
)
from loguru import logger

from app.frontend.desktop_app.mazes.maze_geometry import MazeGeometry
from app.frontend.desktop_app.mazes.maze_renderer import MazeRenderer
from app.frontend.desktop_app.mazes.solution_path import MazeSolution


class MazeOpenGLWidget(QOpenGLWidget, MazeGeometry, MazeSolution, MazeRenderer):

    def __init__(self, parent=None):
        super().__init__(parent)
        MazeGeometry.__init__(self)
        MazeSolution.__init__(self)
        MazeRenderer.__init__(self)

    def _calculating_size_of_cell(self) -> Tuple[float, float]:
        window_width = self.width()
        window_height = self.height()
        logger.debug(
            f"Ширина окна: {window_width} Высота окна: {window_height}")

        cell_width = window_width / self._cols
        cell_height = window_height / self._rows
        logger.debug(
            f"Ширина клетки: {cell_width} Высота клетки: {cell_height}")

        return cell_width, cell_height

    def initializeGL(self):
        logger.debug("Инициализация OpenGL")
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width(), self.height(), 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def paintGL(self):
        logger.debug("Перерисовка OpenGL")
        glClear(GL_COLOR_BUFFER_BIT)
        self._draw_border(self.width(), self.height())
        self._draw_walls(self._right_segments, self._lower_segments)
        self._draw_path(self._path_segments)
        self._draw_points(self.start_point, self.end_point)

    def draw_maze(self):
        self._from_matrix_in_segments(*self._calculating_size_of_cell())
        self.clear_solution()
        self.update()
        logger.success(
            f"Лабиринт отрисован с размером {self._cols}x{self._rows}")

    def draw_path_solution(self):
        self._from_path_in_segments(*self._calculating_size_of_cell())
        self.update()
        logger.success(
            f"Решение лабиринта отрисован с размером {len(self.path_solution)}")

    def draw_points(self):
        self.update()

    def get_start_point(self) -> Tuple[int, int]:
        return self._pixel_to_grid(*self.start_point, self.width(),
                                   self.height(), self.cols, self.rows)

    def get_end_point(self) -> Tuple[int, int]:
        return self._pixel_to_grid(*self.end_point, self.width(), self.height(),
                                   self.cols, self.rows)

    def set_path_solution(self, path: List[Tuple[int, int]]):
        if self._validate_path_solution(path, self.rows, self.cols):
            self._path_solution = path
        else:
            raise ValueError("Неверный формат path_solution")
