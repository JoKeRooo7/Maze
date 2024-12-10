from typing import Tuple, List

from loguru import logger
from pydantic import ValidationError

from backend.mazes.validators import MazeValidators


class MazeManager:
    def create_maze(self, rows: int, columns: int) -> Tuple[List, List]:

        try:
            maze_validator = MazeValidators(rows=rows, cols=columns)
        except ValidationError as e:
            logger.error(f"Ошибка валидации при создании лабиринта:\n{e}")
            raise

        # TODO поставить алгоритм создание лабиринта
        right_walls = [
            [0, 0, 0, 1],
            [1, 0, 1, 1],
            [0, 1, 0, 1],
            [0, 0, 0, 1]
        ]
        lower_walls = [
            [1, 0, 1, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]

        return right_walls, lower_walls

    def solve_maze(self, right_walls: List, lower_walls: List, rows: int, columns: int, entry_index: Tuple[int],
                   exit_index: Tuple[int]) -> List[List]:
        try:
            maze_validator = MazeValidators(
                rows=rows,
                cols=columns,
                right_walls=right_walls,
                lower_walls=lower_walls,
                entry_index=entry_index,
                exit_index=exit_index
            )
        except ValidationError as e:
            logger.error(f"Ошибка валидации при поиске решения лабиринта:\n{e}")
            raise
        # TODO: Реализуйте алгоритм решения лабиринта
        result = []

        return result
