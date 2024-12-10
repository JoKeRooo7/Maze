from typing import Tuple, List

from loguru import logger


class MazeSolution:

    def __init__(self):
        self._start_point: Tuple[float, float] = (250.0, 100.0)
        self._end_point: Tuple[float, float] = (100.0, 250.0)
        self._path_solution: List[Tuple[int, int]] = []
        self._path_segments: List = []

    @property
    def start_point(self) -> Tuple[float, float]:
        return self._start_point

    @start_point.setter
    def start_point(self, value: Tuple[float, float]):
        self._start_point = value

    @property
    def end_point(self) -> Tuple[float, float]:
        return self._end_point

    @end_point.setter
    def end_point(self, value: Tuple[float, float]):
        self._end_point = value

    @property
    def path_solution(self) -> List[Tuple[int, int]]:
        return self._path_solution

    @staticmethod
    def _validate_path_solution(path: List[Tuple[int, int]], rows: int,
                                cols: int) -> bool:
        if not path or not all(isinstance(point, tuple) for point in path):
            return False
        if all((i >= rows) or (j >= cols) for i, j in path):
            return False
        num_cols = len(path[0])
        return all(len(point) == num_cols for point in path)

    def _from_path_in_segments(self, cell_width: float, cell_height: float):
        self._path_segments.clear()

        x_start, y_start = self.start_point
        x_end, y_end = self.end_point

        for i in range(len(self._path_solution) - 1):
            start_row, start_col = self._path_solution[i]
            end_row, end_col = self._path_solution[i + 1]

            x1: int = round(start_col * cell_width + cell_width / 2)
            y1: int = round(start_row * cell_height + cell_height / 2)
            x2: int = round(end_col * cell_width + cell_width / 2)
            y2: int = round(end_row * cell_height + cell_height / 2)

            self._path_segments.append((x1, y1, x2, y2))

        if self._path_solution:
            first_row, first_col = self._path_solution[0]
            x_first = round(first_col * cell_width + cell_width / 2)
            y_first = round(first_row * cell_height + cell_height / 2)
            self._path_segments.insert(0, (x_start, y_start, x_first, y_first))

            last_row, last_col = self._path_solution[-1]
            x_last = round(last_col * cell_width + cell_width / 2)
            y_last = round(last_row * cell_height + cell_height / 2)
            self._path_segments.append((x_last, y_last, x_end, y_end))

        logger.success("Решение лабиринта перерисовано в сегменты")

    @staticmethod
    def _pixel_to_grid(x: float, y: float, width: int, height: int, cols: int,
                       rows: int) -> Tuple[int, int]:
        cell_width = width / cols
        cell_height = height / rows
        i = int(y // cell_height)
        j = int(x // cell_width)
        return i, j

    def clear_solution(self):
        self._path_solution.clear()
        self._path_segments.clear()
