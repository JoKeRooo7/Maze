from typing import Tuple, List
from loguru import logger
from pydantic import ValidationError

from app.backend.mazes.algorithms.generating import GeneratingMaze
from app.backend.mazes.algorithms.solutions import BFS
from app.backend.mazes.dto import MazeData, SolutionData
from app.backend.mazes.validators import MazeValidators, SolutionPathValidator


class MapperSchem:
    """
    Class for mapping maze data to tuple of lists
    """

    @staticmethod
    def from_data_to_tuple_of_lists(maze_data: MazeData) -> Tuple[List, List]:
        return maze_data.right_walls.tolist(), maze_data.lower_walls.tolist()


class MazeManager:
    """
    The `MazeManager` class to manage the maze generation and solving processes.
    It provides a high-level interface for working with mazes, encapsulating complex validation, generation,
    and solving logic, and providing convenient methods for creating and solving mazes.
    """

    @staticmethod
    def _from_maze_validators_in_dto(
            maze_validator: MazeValidators) -> MazeData:
        return MazeData(
            rows=maze_validator.rows,
            cols=maze_validator.cols,
            right_walls=maze_validator.right_walls,
            lower_walls=maze_validator.lower_walls,
        )

    @staticmethod
    def _from_solution_validator_in_dto(
            solution_validator: SolutionPathValidator) -> SolutionData:
        return SolutionData(
            start_point=solution_validator.start_point,
            end_point=solution_validator.end_point,
        )

    def create_maze(self, rows: int, columns: int) -> Tuple[List, List]:
        """
        Creates a maze with the given parameters.
        :param rows: Number of rows in the maze.
        :param columns: Number of columns in the maze.
        :return: Tuple of lists mazes:
                1. List: 2D list representing walls on the right side of each cell.
                                Each inner list represents a row, where 1 indicates a wall and 0 indicates no wall.
                2. List: 2D list representing walls on the bottom side of each cell.
                        Each inner list represents a column, where 1 indicates a wall and 0 indicates no wall.
        """

        try:
            maze_validator = MazeValidators(rows=rows, cols=columns)
        except ValidationError as e:
            logger.error(f"Ошибка валидации при создании лабиринта:\n{e}")
            raise

        maze_dto = self._from_maze_validators_in_dto(maze_validator)
        maze = GeneratingMaze()
        maze.create_maze(maze_dto)
        right_walls, lower_walls = MapperSchem.from_data_to_tuple_of_lists(
            maze_dto)
        logger.info(f"Лабиринт отстроен")
        return right_walls, lower_walls

    def solve_maze(
        self,
        right_walls: List,
        lower_walls: List,
        rows: int,
        columns: int,
        start_point: Tuple[int, int],
        end_point: Tuple[int, int],
    ) -> List[Tuple[int, int]]:
        """
        Class for solving the maze.
        :param right_walls: Walls on the right side of each cell.
        :param lower_walls: Walls on the bottom side of each cell.
        :param rows: Number of rows in the maze.
        :param columns: Number of columns in the maze.
        :param start_point: Starting point coordinates.
        :param end_point: Ending point coordinates.
        :return: Path from start to end as a list of coordinates.
        """
        try:
            maze_validator = MazeValidators(
                rows=rows,
                cols=columns,
                right_walls=right_walls,
                lower_walls=lower_walls,
            )
            solve_validator = SolutionPathValidator(
                rows=maze_validator.rows,
                cols=maze_validator.cols,
                start_point=start_point,
                end_point=end_point,
            )
        except ValidationError as e:
            logger.error(f"Ошибка валидации при поиске решения лабиринта:\n{e}")
            raise
        maze_dto = self._from_maze_validators_in_dto(maze_validator)
        solution_dto = self._from_solution_validator_in_dto(solve_validator)
        algorithm_bfs = BFS(maze_data=maze_dto, solution_data=solution_dto)
        algorithm_bfs.finding_way()
        return solution_dto.solution_coordinates
