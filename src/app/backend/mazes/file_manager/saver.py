from typing import List

from loguru import logger

from app.backend.mazes.validators import MazeValidators


class MazeSaver:
    """
    Class for saving mazes in file
    """

    def __init__(
        self,
        file_path: str,
        rows: int,
        cols: int,
        right_walls: List,
        lower_walls: List,
    ):
        MazeValidators(
            rows=rows,
            cols=cols,
            right_walls=right_walls,
            lower_walls=lower_walls,
        )
        self.file_path = file_path
        self.rows = rows
        self.cols = cols
        self.right_walls = right_walls
        self.lower_walls = lower_walls

    def save_maze(self):
        try:
            with open(self.file_path, "w") as file:
                file.write(f"{self.rows} {self.cols}\n")
                for row in self.right_walls:
                    file.write(" ".join(map(str, row)) + "\n")
                file.write("\n")
                for row in self.lower_walls:
                    file.write(" ".join(map(str, row)) + "\n")
        except Exception as e:
            logger.error(f"Ошибка при сохранении лабиринта в файл: {e}")
            raise e
