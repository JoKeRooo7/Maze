import pytest
import numpy as np
# import logging
from collections import deque
from backend.mazes.dto import MazeData
from backend.mazes.dto import SolutionData
from backend.mazes.algorithms.solutions.breadth_first_search import BFS
from backend.mazes.algorithms.generating.generating_maze import GeneratingMaze

params = [(i, j) for i in range(2, 51) for j in range(2, 51)]

@pytest.mark.parametrize("rows, cols", params)
def test_for_insulation(rows, cols):
    """
    Данный текст сначала создает по заданному размеру rows, cols лабиринт,
    Потом от самой левой верхней точки пытается пройти до каждой другой точки в лабиринте.
    """
    data = MazeData(rows=rows, cols=cols)

    labirint = GeneratingMaze(data)
    data = labirint.create_maze()
    solution_data = SolutionData(start_point=(0,0), end_point=(0,0), solution_coordinates=None)
    solution = BFS()

    for i in range(rows):
        for j in range(cols):
            if solution_data.start_point == (i, j):
                continue

            solution_data.end_point=(i, j)
            result = solution.finding_way(maze_data=data,
                solution_data=solution_data).solution_coordinates
            assert result != None

def _get_count_way(data, start, end):
    """
    Алгоритм обхода BFS - учитываюший повтор координат в только текущем пути
    """
    way = deque([(start, [start])])
    all_paths = []
    # visited = set()

    rows = data.rows
    cols = data.cols
    
    while way:
        (i, j), path = way.popleft()
        
        if (i, j) == end:
            all_paths.append(path)
            continue
        # visited.add((i, j))
        directions = []
        if j + 1 < cols and data.right_walls[i, j] == 0:
            directions.append((i, j + 1))
        if i + 1 < rows and data.lower_walls[i, j] == 0:
            directions.append((i + 1, j))
        if j - 1 >= 0 and data.right_walls[i, j - 1] == 0:
            directions.append((i, j - 1)) 
        if i - 1 >= 0 and data.lower_walls[i - 1, j] == 0:
            directions.append((i - 1, j))

        for new_i, new_j in directions:
            # if (new_i, new_j) not in visited:

            if (new_i, new_j) not in path:
                way.append(((new_i, new_j), path + [(new_i, new_j)]))
    return len(all_paths)


@pytest.mark.parametrize("rows, cols", params)
def test_for_counting_the_number_of_paths(rows, cols):
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

    assert _get_count_way(data, start_coord, end_coord) == 1

# python3.12 -m pytest -s -v  --durations=10 test_generate.py
# python3.12 -m pytest -s -v --benchmark-only test_generate.py