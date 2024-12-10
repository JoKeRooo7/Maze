from typing import Tuple

from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import (
    GL_POINTS,
    glPointSize,
    glClearColor,
    glClear,
    GL_COLOR_BUFFER_BIT,
    glBegin,
    glEnd,
    GL_LINES,
    glVertex2f,
    glColor3f,
    glOrtho,
    glMatrixMode,
    GL_PROJECTION,
    GL_MODELVIEW,
    glLoadIdentity,
    glLineWidth,
    glViewport,
)
from loguru import logger


class MazeRenderer:

    def __init__(self):
        self._line_width = 2.0
        self._size_points_size = 5.0

    @staticmethod
    def _draw_segments(segments):
        glBegin(GL_LINES)
        for segment in segments:
            x1, y1, x2, y2 = segment
            glVertex2f(x1, y1)
            glVertex2f(x2, y2)
        glEnd()

    def _draw_walls(self, right_segments, lower_segments):
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(0.5)
        self._draw_segments(right_segments)
        self._draw_segments(lower_segments)

    def _draw_path(self, path_segments):
        glColor3f(1.0, 0.0, 0.0)
        glLineWidth(0.5)
        self._draw_segments(path_segments)

    def _draw_points(
        self,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ):
        glColor3f(0.0, 1.0, 0.0)
        glPointSize(self._size_points_size)
        glBegin(GL_POINTS)
        glVertex2f(*start_point)
        glEnd()

        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_POINTS)
        glVertex2f(*end_point)
        glEnd()

    def _draw_border(self, width: int, height: int):
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(self._line_width)
        glBegin(GL_LINES)

        # Верхняя граница
        glVertex2f(0, 0)
        glVertex2f(width, 0)

        # Нижняя граница
        glVertex2f(0, height)
        glVertex2f(width, height)

        # Левая граница
        glVertex2f(0, 0)
        glVertex2f(0, height)

        # Правая граница
        glVertex2f(width, 0)
        glVertex2f(width, height)

        glEnd()
