from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class SolutionData:
    start_point: Tuple[int, int]
    end_point: Tuple[int, int]
    solution_coordinates: List[Tuple[int, int]]
