import heapq
import pytest
import numpy as np
from collections import deque
from backend.mazes.dto import MazeData
from backend.mazes.dto import SolutionData
from backend.mazes.algorithms.solutions.breadth_first_search import BFS
from backend.mazes.algorithms.generating.generating_maze import GeneratingMaze


params = [(i, j) for i in range(2, 51) for j in range(2, 51)]

def __dijkstra_shortest_path_length(maze_data, start, end):
    """Находит короткий путь в лабиринте (Алгоритм Дейкстры)."""
    rows = maze_data.rows
    cols = maze_data.cols
    distances = np.full((rows, cols), float('inf')) # все веса inf
    distances[start[0], start[1]] = 0 #  0 (расстояние) на координате старта
    priority_queue = [(0, start)]  # приоритетная очередь с расстоянием 0 и координатами старта
    visited = set()

    while priority_queue:
        # минимальная куча c весом и координатами
        current_distance, (i, j) = heapq.heappop(priority_queue)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        
        # Если достигли конечной точки, возвращаем расстояние
        if (i, j) == end:
            return current_distance

        directions = []
        if j + 1 < cols and maze_data.right_walls[i, j] == 0:
            directions.append((i, j + 1))
        if i + 1 < rows and maze_data.lower_walls[i, j] == 0:
            directions.append((i + 1, j))
        if j - 1 >= 0 and maze_data.right_walls[i, j - 1] == 0:
            directions.append((i, j - 1))
        if i - 1 >= 0 and maze_data.lower_walls[i - 1, j] == 0:
            directions.append((i - 1, j))

        for new_i, new_j in directions:
            # тк не нашлась конечная координата - добавляем расстояние 1
            distance = current_distance + 1  # Все перемещения имеют единичный вес прибавляется к пути
            if distance < distances[new_i, new_j]:
                distances[new_i, new_j] = distance # заносися в матрицу инфгормация о весе
                heapq.heappush(priority_queue, (distance, (new_i, new_j)))
    
    return float('inf')  # Возвращаем бесконечность, если путь не найден


@pytest.mark.parametrize("rows, cols", params)
def test_comparison_of_two_algorithms(rows, cols):
    """
    Данный текст сначала создает по заданному размеру rows, cols лабиринт,
    и потом по рандомным точкам в нем ищет все возможные путидо точки.
    """
    data = MazeData(rows=rows, cols=cols)
    labirint = GeneratingMaze(data)
    data = labirint.create_maze()

    start_coord = (np.random.randint(0, data.rows),
        np.random.randint(0, data.cols))
    end_coord = (np.random.randint(0, data.rows),
        np.random.randint(0, data.cols))
    
    labirint = GeneratingMaze(data)
    data = labirint.create_maze()
    solution_data = SolutionData(
        start_point=start_coord, 
        end_point=end_coord, 
        solution_coordinates=None)
    solution = BFS()

    bfs_result = solution.finding_way(
        maze_data=data,
        solution_data=solution_data).solution_coordinates

    dijkstra_result = __dijkstra_shortest_path_length(
        maze_data=data,
        start=start_coord, 
        end=end_coord
    ) 
    
    assert bfs_result != dijkstra_result