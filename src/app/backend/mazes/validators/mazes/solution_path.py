from typing import Optional, Tuple

from pydantic import BaseModel, field_validator


class SolutionPathValidator(BaseModel):
    """
    Class to validate the solution path
    """

    rows: int
    cols: int
    start_point: Optional[Tuple[int, int]] = None
    end_point: Optional[Tuple[int, int]] = None

    class Config:
        arbitrary_types_allowed = True

    @field_validator("start_point", "end_point")
    def validate_indices(cls, value, info):
        if value is not None:
            row, col = value
            rows = info.data.get("rows")
            cols = info.data.get("cols")
            if rows is None or cols is None:
                raise ValueError(
                    "Необходимо задать количество строк и столбцов для валидации индексов"
                )
            if not (0 <= row < rows) or not (0 <= col < cols):
                raise ValueError(
                    f"Индекс {value} выходит за пределы матрицы размером {rows}x{cols}"
                )
        return value
