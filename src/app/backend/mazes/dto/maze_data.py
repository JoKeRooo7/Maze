from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass
class MazeData:
    rows: Optional[int] = None
    cols: Optional[int] = None
    right_walls: Optional[np.ndarray] = None
    lower_walls: Optional[np.ndarray] = None
