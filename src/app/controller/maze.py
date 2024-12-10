from typing import Tuple, List

from app.backend.mazes import MazeManager, MazeLoader, MazeSaver


class ControllerMaze:

    def __init__(self):
        self.maze_manager: MazeManager = MazeManager()

    def create_maze(self, rows: int, columns: int) -> Tuple[List, List]:
        """
        Create maze

        :param rows: Number of rows in the maze.
        :param columns: Number of columns in the maze.
        :return: Tuple of lists mazes:
                1. List: 2D list representing walls on the right side of each cell.
                                Each inner list represents a row, where 1 indicates a wall and 0 indicates no wall.
                2. List: 2D list representing walls on the bottom side of each cell.
                        Each inner list represents a column, where 1 indicates a wall and 0 indicates no wall.
        """
        return self.maze_manager.create_maze(rows, columns)

    def solve_maze(
        self,
        right_walls: List[List],
        lower_walls: List[List],
        rows: int,
        columns: int,
        start_point: Tuple[int, int],
        end_point: Tuple[int, int],
    ) -> List[Tuple[int, int]]:
        """
        Get solve from maze

        :param right_walls: Walls on the right side of each cell.
        :param lower_walls: Walls on the bottom side of each cell.
        :param rows: Number of rows in the maze.
        :param columns: Number of columns in the maze.
        :param start_point: Starting point coordinates.
        :param end_point: Ending point coordinates.
        :return: Path from start to end as a list of coordinates.
        """
        return self.maze_manager.solve_maze(right_walls, lower_walls, rows,
                                            columns, start_point, end_point)

    def load_maze(self, path: str) -> Tuple[int, int, List, List]:
        """
        Load maze from a file.

        :param path: file path of maze
        :return: A tuple containing four elements:
                1. int: Number of rows in the maze.
                2. int: Number of columns in the maze.
                3. List: 2D list representing walls on the right side of each cell.
                        Each inner list represents a row, where 1 indicates a wall and 0 indicates no wall.
                4. List: 2D list representing walls on the bottom side of each cell.
                        Each inner list represents a column, where 1 indicates a wall and 0 indicates no wall.
        """
        return MazeLoader(path).load_maze()

    def save_maze(
        self,
        path: str,
        rows: int,
        columns: int,
        right_walls: List[List],
        lower_walls: List[List],
    ):
        """
        Save maze data to a file.

        :param path: Path to the file where maze data will be saved.
        :param rows: Number of rows in the maze.
        :param columns: Number of columns in the maze.
        :param right_walls: 2D list representing walls on the right side of each cell.
                                 Each inner list represents a row, where 1 indicates a wall and 0 indicates no wall.
        :param lower_walls:  2D list representing walls on the bottom side of each cell.
                                 Each inner list represents a column, where 1 indicates a wall and 0 indicates no wall.
        """
        MazeSaver(path, rows, columns, right_walls, lower_walls).save_maze()
