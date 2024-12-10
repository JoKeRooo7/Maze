from typing import Optional

import numpy as np
from pydantic import BaseModel, conint, field_validator


class MazeValidators(BaseModel):
    """
    Class to validate the maze
    """

    rows: conint(ge=1, le=50)
    cols: conint(ge=1, le=50)
    right_walls: Optional[np.ndarray] = None
    lower_walls: Optional[np.ndarray] = None

    class Config:
        arbitrary_types_allowed = True

    @field_validator("rows", "cols")
    def validate_rows_cols(cls, value):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("Поля rows и cols должны быть целыми числами.")
            if not (1 <= value <= 50):
                raise ValueError(
                    "Поля rows и cols должны быть в диапазоне от 1 до 50.")
            return value

    @field_validator("right_walls", "lower_walls", mode="before")
    def validate_and_convert_walls(cls, value):
        if isinstance(value, list):
            array = np.array(value, dtype=int)
            if array.size == 0:
                raise ValueError("Массив стен не должен быть пустым")
            if not issubclass(array.dtype.type, np.integer):
                raise TypeError(
                    "Массив стен должен содержать только целочисленные данные")
            return array
        return value
