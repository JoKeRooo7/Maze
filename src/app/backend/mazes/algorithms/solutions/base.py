from typing import Protocol

from app.backend.mazes.dto import MazeData, SolutionData


class IBasesSolutionMaze(Protocol):
    """
    Интерфейс базового метода решения лабиринта
    """

    def finding_way(self, maze_data: MazeData,
                    sulution_data: SolutionData) -> SolutionData:
        """
        Функция создания решения лабиринта с заданными параметрами
        :param maze_data: Данные лабиринта и сам лабиринт
        :param sulution_data: Данные решения
        :return: индексы матрицы с решением
        """
        ...
