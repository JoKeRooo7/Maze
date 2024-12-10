from typing import Optional, List, Tuple

import numpy as np
from pydantic import BaseModel, conint, conlist, field_validator, model_validator


class MazeValidators(BaseModel):
    rows: conint(ge=1, le=50)
    cols: conint(ge=1, le=50)
    right_walls: Optional[np.ndarray] = None
    lower_walls: Optional[np.ndarray] = None
    entry_index: Optional[Tuple[int, int]] = None
    exit_index: Optional[Tuple[int, int]] = None

    class Config:
        arbitrary_types_allowed = True

    @field_validator('right_walls', 'lower_walls', mode='before')
    def validate_and_convert_walls(cls, value):
        """
        Проверяет, что входящие данные являются списком списков целых чисел и конвертирует их в numpy массив
        """
        if isinstance(value, list):
            array = np.array(value, dtype=int)
            if array.size == 0:
                raise ValueError("Массив стен не должен быть пустым")
            if not issubclass(array.dtype.type, np.integer):
                raise TypeError("Массив стен должен содержать только целочисленные данные")
            return array
        return value

    @field_validator('entry_index', 'exit_index')
    def validate_indices(cls, value, info):
        """
        Проверяет, что координаты входа и выхода находятся в пределах матрицы.
        """
        if value is not None:
            row, col = value
            rows = info.data.get('rows')
            cols = info.data.get('cols')
            if rows is None or cols is None:
                raise ValueError("Необходимо задать количество строк и столбцов для валидации индексов")
            if not (0 <= row < rows) or not (0 <= col < cols):
                raise ValueError(f"Индекс {value} выходит за пределы матрицы размером {rows}x{cols}")
        return value

# Нужна проверка массива
# Много проверок
# @dataclass
# class MazeData:
#     rows: Optional[int] = None
#     cols: Optional[int] = None
#     right_walls: Optional[np.ndarray] = None
#     lower_walls: Optional[np.ndarray] = None

#     def __post_init__(self):
#         if self.right_walls is not None and self.lower_walls is not None:
#             self._validate_arrays()
#             self._autosize()
#         elif (self.right_walls is not None) ^ (self.lower_walls is None):
#             raise ValueError("Specify two arrays")
#         else:
#             self.rows = 0 if self.rows is None else self.rows
#             self.cols = 0 if self.cols is None else self.cols

#     def _validate_size(self):
#         if not isinstance(self.rows) or not isinstance(self.cols):
#             raise TypeError("dimensions of the incorrect type")

#     def _validate_arrays(self):
#         if not isinstance(self.right_walls, np.ndarray) or \
#            not isinstance(self.lower_walls, np.ndarray):
#             raise TypeError("Arrays do not match the np type np.darray")

#         if not issubclass(self.right_walls.dtype.type, np.integer):
#             raise TypeError(
#                 "The right_walls array contains a non-integer data type")

#         if not issubclass(self.lower_walls.dtype.type, np.integer):
#             raise TypeError(
#                 "The lower_walls array contains a non-integer data type")

#         if self.right_walls.shape != self.lower_walls.shape:
#             raise TypeError(
#                 "right_walls and lower_walls must have the same size")

#     def _autosize(self):
#         self.rows, self.cols = self.right_walls.shape

#     def _autoarray(self):
#         self.right_walls = np.zeros((self.rows, self.cols), dtype=int)
