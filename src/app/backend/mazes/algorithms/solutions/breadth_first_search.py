import random
import numpy as np
from collections import deque
from app.backend.mazes.dto import MazeData
from app.backend.mazes.dto import SolutionData
from app.backend.mazes.algorithms.solutions.base import IBasesSolutionMaze


class BFS(IBasesSolutionMaze):

    def __init__(self, maze_data=None, solution_data=None):
        """
        Конструктор. Инициализирует объект класса `BFS`.
        Алгоритм обхода в ширину для лабиринта

        Аргументы:
            maze_data (MazeData, optional): Данные о лабиринте. Значение по умолчанию - None.
            solution_data (solution_data, optional): Данные с точками старта и конца.  Значение по умолчанию - None.
        """
        self.maze_data = maze_data
        self.solution_data = solution_data

    @property
    def solution_data(self) -> MazeData:
        """
        Получает данные о лабиринте.

        Возвращает:
            MazeData: Данные о лабиринте.
        """
        return self.__solution_data

    @solution_data.setter
    def solution_data(self, solution_data) -> None:
        """
        Устанавливает данные о лабиринте.

        Аргументы:
            maze_data (MazeData): Данные о лабиринте для установки.
        """
        if solution_data is not None:
            self.__solution_data = solution_data

    @property
    def maze_data(self) -> MazeData:
        """
        Получает данные о лабиринте.

        Возвращает:
            MazeData: Данные о лабиринте.
        """
        return self.__maze_data

    @maze_data.setter
    def maze_data(self, maze_data) -> None:
        """
        Устанавливает данные о лабиринте.

        Аргументы:
            maze_data (MazeData): Данные о лабиринте для установки.
        """
        if maze_data is not None:
            self.__maze_data = maze_data

    def finding_way(self, maze_data=None, solution_data=None):
        self.maze_data = maze_data
        self.solution_data = solution_data
        start = self.solution_data.start_point
        end = self.solution_data.end_point
        rows, cols = self.maze_data.right_walls.shape
        way = deque([(start, [start])])
        visited = set()
        while way:
            (i, j), path = way.popleft()
            if (i, j) == end:
                self.solution_data.solution_coordinates = path
                return self.solution_data

            visited.add((i, j))
            directions = []

            if j + 1 < cols and self.maze_data.right_walls[i, j] == 0:
                directions.append((i, j + 1))

            if i + 1 < rows and self.maze_data.lower_walls[i, j] == 0:
                directions.append((i + 1, j))

            if j - 1 >= 0 and self.maze_data.right_walls[i, j - 1] == 0:
                directions.append((i, j - 1))

            if i - 1 >= 0 and self.maze_data.lower_walls[i - 1, j] == 0:
                directions.append((i - 1, j))

            for new_i, new_j in directions:
                if (new_i, new_j) not in visited:
                    way.append(((new_i, new_j), path + [(new_i, new_j)]))

        self.solution_data.solution_coordinates = None
        return self.solution_data.solution_coordinates
