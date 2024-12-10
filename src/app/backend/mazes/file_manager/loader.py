from typing import List, Tuple

from loguru import logger

from backend.mazes.validators import MazeValidators


class MazeLoader:
    """
    Класс для загрузки матрицы из файла
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    @staticmethod
    def _read_matrix(lines: List[str], start_index: int, num_rows: int) -> List[List[int]]:
        return [
            list(map(int, lines[start_index + i].strip().split()))
            for i in range(num_rows)
        ]

    def load_maze(self) -> Tuple[int, int, List, List]:
        """
        Функция для загрузки матрицы из файла
        :return: rows, cols, right_walls, lower_walls
        """
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        i = 0
        try:
            rows, cols = map(int, lines[i].strip().split())
            i += 1

            right_walls = self._read_matrix(lines, i, rows)
            i += rows + 1

            lower_walls = self._read_matrix(lines, i, rows)
            i += rows
        except Exception as e:
            logger.error(f"Файл {self.file_path} не соотвествует формату")
            raise e

        MazeValidators(rows=rows, cols=cols, right_walls=right_walls, lower_walls=lower_walls)
        return rows, cols, right_walls, lower_walls
