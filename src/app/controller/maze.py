from typing import Tuple, List

from backend.mazes.facade import MazeManager
from backend.mazes.file_manager import MazeLoader, MazeSaver


class ControllerMaze:
    def __init__(self):
        self.maze_manager: MazeManager = MazeManager()

    def create_maze(self, rows: int, columns: int) -> Tuple[List, List]:
        return self.maze_manager.create_maze(rows, columns)

    def solve_maze(self, right_walls: List[List], lower_walls: List[List], rows: int, columns: int,
                   entry_index: Tuple[int], exit_index: Tuple[int]) -> List[List]:
        return self.maze_manager.solve_maze(right_walls, lower_walls, rows, columns, entry_index, exit_index)

    def load_maze(self, path: str) -> Tuple[int, int, List, List]:
        return MazeLoader(path).load_maze()

    def save_maze(self, path: str, rows: int, columns: int, right_walls: List[List], lower_walls: List[List]):
        return MazeSaver(path, rows, columns, right_walls, lower_walls).save_maze()
