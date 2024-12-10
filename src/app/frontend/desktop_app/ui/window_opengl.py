from typing import Tuple, List

from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import GL_POINTS, glPointSize, glClearColor, glClear, GL_COLOR_BUFFER_BIT, glBegin, glEnd, GL_LINES, \
    glVertex2f, glColor3f, glOrtho, glMatrixMode, GL_PROJECTION, GL_MODELVIEW, glLoadIdentity, glLineWidth
from loguru import logger


class MazeOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._right_walls: List[List[int]] = []
        self._lower_walls: List[List[int]] = []
        self._right_segments = []
        self._lower_segments = []
        self.rows: int = 1
        self.cols: int = 1
        self._entry_point: Tuple[float, float] = (250.0, 100.0)
        self._exit_point: Tuple[float, float] = (100.0, 250.0)

    @property
    def entry_point(self) -> Tuple[float, float]:
        return self._entry_point

    @entry_point.setter
    def entry_point(self, value: Tuple[float, float]):
        self._entry_point = value
        self.update()

    @property
    def exit_point(self) -> Tuple[float, float]:
        return self._exit_point

    @exit_point.setter
    def exit_point(self, value: Tuple[float, float]):
        self._exit_point = value
        self.update()

    @property
    def right_walls(self) -> List[List[int]]:
        return self._right_walls

    @right_walls.setter
    def right_walls(self, value: List[List[int]]):
        if self._validate_walls(value):
            self._right_walls = value
        else:
            raise ValueError("Неверный формат right_walls")

    @property
    def lower_walls(self) -> List[List[int]]:
        return self._lower_walls

    @lower_walls.setter
    def lower_walls(self, value: List[List[int]]):
        if self._validate_walls(value):
            self._lower_walls = value
        else:
            raise ValueError("Неверный формат lower_walls")

    @staticmethod
    def _validate_walls(walls: List[List[int]]) -> bool:
        if not walls or not all(isinstance(row, list) for row in walls):
            return False
        num_cols = len(walls[0])
        return all(len(row) == num_cols for row in walls)

    def _from_matrix_in_segments(self):
        self._right_segments = []
        self._lower_segments = []
        self.rows = len(self._right_walls)
        self.cols = len(self._right_walls[0])
        logger.debug(f"Количество строк: {self.rows} Количество столбцов: {self.cols}")

        window_width = self.width()
        window_height = self.height()
        logger.debug(f"Ширина окна: {window_width} Высота окна: {window_height}")

        cell_width = window_width / self.cols
        cell_height = window_height / self.rows
        logger.debug(f"Ширина клетки: {cell_width} Высота клетки: {cell_height}")

        for row in range(self.rows):
            for col in range(self.cols):
                x = col * cell_width
                y = row * cell_height

                if self._right_walls[row][col] == 1:
                    self._right_segments.append((x + cell_width, y, x + cell_width, y + cell_height))

                if self._lower_walls[row][col] == 1:
                    self._lower_segments.append((x, y + cell_height, x + cell_width, y + cell_height))

        logger.success("Матрица перерисована в сегменты")

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
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(2.0)
        glBegin(GL_LINES)
        for segment in self._right_segments:
            self._draw_segment(segment)
        glEnd()

        glBegin(GL_LINES)
        for segment in self._lower_segments:
            self._draw_segment(segment)
        glEnd()
        self._draw_points()
        self._draw_border()

    def _draw_segment(self, segment):
        x1, y1, x2, y2 = segment
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)

    def _draw_border(self):
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(4.0)
        glBegin(GL_LINES)

        # Верхняя граница
        glVertex2f(0, 0)
        glVertex2f(self.width(), 0)

        # Нижняя граница
        glVertex2f(0, self.height())
        glVertex2f(self.width(), self.height())

        # Левая граница
        glVertex2f(0, 0)
        glVertex2f(0, self.height())

        # Правая граница
        glVertex2f(self.width(), 0)
        glVertex2f(self.width(), self.height())

        glEnd()

    def _draw_points(self):
        """
        Отрисовывает точки входа и выхода.
        """
        glColor3f(0.0, 1.0, 0.0)  # Зеленый цвет
        glPointSize(10.0)  # Размер точки
        glBegin(GL_POINTS)
        glVertex2f(self.entry_point[0], self.entry_point[1])
        glEnd()

        glColor3f(0.0, 0.0, 1.0)  # Синий цвет
        glBegin(GL_POINTS)
        glVertex2f(self.exit_point[0], self.exit_point[1])
        glEnd()
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(10.0)

    def _pixel_to_grid(self, x: float, y: float) -> Tuple[int, int]:
        cell_width = self.width() / self.cols
        cell_height = self.height() / self.rows
        row = int(y // cell_height)
        col = int(x // cell_width)
        return col, row

    def get_entry_index(self) -> Tuple[int, int]:
        return self._pixel_to_grid(*self.entry_point)

    def get_exit_index(self) -> Tuple[int, int]:
        return self._pixel_to_grid(*self.exit_point)

    def draw_maze(self):
        self._from_matrix_in_segments()
        self.update()
        logger.success(f"Лабиринт отрисован с размером {self.cols}x{self.rows}")
