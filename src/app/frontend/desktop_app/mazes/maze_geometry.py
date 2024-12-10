from typing import List, Tuple

from loguru import logger


class MazeGeometry:

    def __init__(self):
        self._rows: int = 1
        self._cols: int = 1
        self._right_walls: List[List[int]] = []
        self._lower_walls: List[List[int]] = []
        self._right_segments: List[Tuple[float, float, float, float]] = []
        self._lower_segments: List[Tuple[float, float, float, float]] = []

    @property
    def right_walls(self) -> List[List[int]]:
        return self._right_walls

    @right_walls.setter
    def right_walls(self, value: List[List[int]]):
        if self._validate_walls(value):
            self._right_walls = value
            self._rows = len(self._right_walls)
        else:
            raise ValueError("Неверный формат right_walls")

    @property
    def lower_walls(self) -> List[List[int]]:
        return self._lower_walls

    @lower_walls.setter
    def lower_walls(self, value: List[List[int]]):
        if self._validate_walls(value):
            self._lower_walls = value
            self._cols = len(self._right_walls[0])
        else:
            raise ValueError("Неверный формат lower_walls")

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value: int):
        self._rows = value

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, value: int):
        self._cols = value

    @staticmethod
    def _validate_walls(walls: List[List[int]]) -> bool:
        if not walls or not all(isinstance(row, list) for row in walls):
            return False
        num_cols = len(walls[0])
        return all(len(row) == num_cols for row in walls)

    def _from_matrix_in_segments(self, cell_width: float, cell_height: float):
        self._right_segments.clear()
        self._lower_segments.clear()
        logger.debug(
            f"Количество строк: {self._rows} Количество столбцов: {self._cols}")

        for row in range(self._rows):
            y = row * cell_height
            for col in range(self._cols):
                x = col * cell_width

                if self._right_walls[row][col] == 1:
                    self._right_segments.append(
                        (x + cell_width, y, x + cell_width, y + cell_height))

                if self._lower_walls[row][col] == 1:
                    self._lower_segments.append(
                        (x, y + cell_height, x + cell_width, y + cell_height))
        logger.success("Матрица перерисована в сегменты")
