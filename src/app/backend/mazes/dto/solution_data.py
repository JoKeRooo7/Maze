from dataclasses import dataclass
from typing import Tuple, List, Optional


@dataclass
class SolutionData:
    start_point: Tuple[int, int]
    end_point: Tuple[int, int]
    solution_coordinates: Optional[List[Tuple[int, int]]] = None
