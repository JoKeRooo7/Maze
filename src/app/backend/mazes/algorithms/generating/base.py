from typing import Protocol

from app.backend.mazes.dto import MazeData


class IBaseGeneratingMaze(Protocol):
    """
    Интерфейс базового генератора лабиринта
    """

    def create_maze(self, maze_data: MazeData) -> MazeData:
        """
        Функция создания лабиринта с заданными параметрами
        :param maze_data: Данные для создания лабиринта
        :return: новый созданный лабиринт
        """
        ...
