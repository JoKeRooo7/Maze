import random
import numpy as np
from app.backend.mazes.dto import MazeData
from app.backend.mazes.algorithms.generating.base import IBaseGeneratingMaze


class GeneratingMaze(IBaseGeneratingMaze):
    """
    Класс для генерации лабиринтов.

    Атрибуты:
        :attr:`maze_data` (MazeData): Данные о лабиринте.

        Переменная храниться и инициалируется в методе setter :meth:`maze_data`

        Пример обращения к переменной:

        >>> maze = GeneratingMaze()
        >>> maze.maze_data

        Пример создания лабиринта:

        >>> maze = GeneratingMaze()
        >>> maze.create_maze(data)

    Методы:
        :meth:`__init__`: Конструктор класса GeneratingMaze
        :meth:`maze_data`: Getter-setter класса GeneratingMaze
        :meth:`create_maze` : Создание лабиринта

    Примечания:
        В атрибуте `maze_data` хранится и инициализируется значение через метод-сеттер `maze_data`.
    """

    def __init__(self, maze_data: MazeData = None):
        """
        Конструктор. Инициализирует объект класса `GeneratingMaze`.

        Аргументы:
            maze_data (MazeData, optional): Данные о лабиринте. Значение по умолчанию - None.
        """
        self.maze_data = maze_data

    @property
    def maze_data(self) -> MazeData:
        """
        Получает данные о лабиринте.

        Возвращает:
            MazeData: Данные о лабиринте.
        """
        return self.__maze_data

    @maze_data.setter
    def maze_data(self, maze_data) -> None:
        """
        Устанавливает данные о лабиринте.
        Зануляет исходные данные

        Аргументы:
            maze_data (MazeData): Данные о лабиринте для установки.
        """
        if maze_data is not None:
            self.__maze_data = maze_data
            self.__maze_data.right_walls = np.zeros(
                (self.__maze_data.rows, self.__maze_data.cols), dtype=int)
            self.__maze_data.lower_walls = np.zeros(
                (self.__maze_data.rows, self.__maze_data.cols), dtype=int)

    def create_maze(self, maze_data: MazeData = None) -> MazeData:
        """
        Создает лабиринт на основе предоставленных данных.

        Сначала подготавливается двумерный массив, где к каждой ячеке присвоено уникальное множество. (метод :meth:`.__creating_an_array_with_sets()`)

        В цикле, проходимся по каждой строке, сначала создавая правые стены (в методе :meth:`__creating_right_walls`)
        и потом создаем нижние стенки (в методе :meth:`__creating_right_walls`).

        Аргументы:
            maze_data (MazeData, optional): Данные о лабиринте. Значение по умолчанию - None.

        Возвращает:
            MazeData: Обновленные данные о лабиринте после создания.
        """
        self.maze_data = maze_data

        array_with_sets = self.__creating_an_array_with_sets()
        rows, cols = array_with_sets.shape

        for i in range(rows):
            self.__creating_right_walls(i=i,
                                        array_with_sets=array_with_sets,
                                        cols=cols)
            self.__creating_lower_walls(i=i,
                                        array_with_sets=array_with_sets,
                                        cols=cols,
                                        rows=rows)
        return self.maze_data

    def __creating_right_walls(self, i, array_with_sets, cols) -> None:
        """
        Создание правых стенок.

        Передвигаясь по каждой ячейке, начиния с первой случано решаем ставить ли стенку.
            * Ставим стенку в конце лабиринта справа всегда.
            * Если поставили стенку - ставим стенку, и двигаемся дальше.
            * Если не поставили стенку:
                * Если текущая ячейка и ячейка с права находястя в одном множестве - ставим стентку.
                * Если никакой пункт сверху не подошел, множество ячейки справа становится таким же как и у текущей.

        Аргументы:
            i (int): Индекс текущей строки.
            cols (int): Указатель на количество элементов в строке
            array_with_sets (np.ndarray): Массив с множествами

        """
        for j in range(cols):
            if j == cols - 1:
                self.__maze_data.right_walls[i, j] = 1
            else:
                need_right_wals = random.choice([True, False])
                if need_right_wals:
                    self.__maze_data.right_walls[i, j] = 1
                else:
                    if array_with_sets[i, j] == array_with_sets[i, j + 1]:
                        self.__maze_data.right_walls[i, j] = 1
                    else:
                        self.__replace_set(array_with_sets, i, j + 1,
                                           array_with_sets[i, j])

    def __creating_lower_walls(self, i, array_with_sets, cols, rows) -> None:
        """
        Создание нижних стенок.

        Передвигаясь по каждой ячейке, начиния с первой случано решаем ставить ли стенку.
            * Если ставим стенку, проверяем ряд условий:
                * В данной строке, среди текущего множества проверить, является ли данная ячейка одна
                без ниэне границы, если она не одна - можно ставить нижнюю стенку
            * Если не поставили ячеку и если текущая строка не последняя - присваиваем текущее множество,
              элементу в следующей строки
            * Если текущая строка последняя:
                * ставим нижнюю стенку
                * Если у текущей ячейки и ячейки справа, множества не совпадают, убираем стенку если есть
                и присваиваем множеству справа такое же, как и у текущей йчейки.

        Аргументы:
            i (int): Индекс текущей строки.
            cols (int): Указатель на количество элементов в строке
            rows (int): Указатель на количество строк
            array_with_sets (np.ndarray): Массив с множествами

        """
        for j in range(cols):
            need_lower_wals = random.choice([True, False])

            if need_lower_wals and self.__cell_is_not_one_without_lower_border(
                    array_with_sets, i, j):
                self.__maze_data.lower_walls[i, j] = 1
            elif i != rows - 1:
                array_with_sets[i + 1, j] = array_with_sets[i, j]
            elif i == rows - 1:
                self.__maze_data.lower_walls[i, j] = 1
                if j != cols - 1:
                    if array_with_sets[i, j] != array_with_sets[i, j + 1]:
                        self.__maze_data.right_walls[i, j] = 0
                    self.__replace_set(array_with_sets, i, j + 1,
                                       array_with_sets[i, j])

    def __creating_an_array_with_sets(self) -> np.ndarray:
        """
        Функция для создания массива с множествами.

        Изначально создается одномерный массив массив, заполенный цифрами
        от 1 д rows * cols + 1. Каждая отдельная цифра - отдельное множество.
        После из него формируем думерный массив и возращаем.

        Аргументы:
            maze_data(MazeData): Массив c входными параметрами.

        Возвращает:
            np.darray: Двумерный массив с множествами.
        """

        need_rows = self.maze_data.rows
        need_cols = self.maze_data.cols
        flat_atray = np.arange(1, need_rows * need_cols + 1)
        new_array = flat_atray.reshape(need_rows, need_cols)
        return new_array

    def __replace_set(self, array_with_sets, i, j, value) -> None:
        """
        Функция для того, чтобы пересвоить множество.

        Переприсваивает по индексам массива.

        Аргументы:
            i (int): Индекс текущей строки.
            j (int): Индекс текущей строки.
            value (int): Значение, на которое будет переприсваиватся
                все множество в строке, по текущему индексу.
            array_with_sets (np.ndarray): Массив с множествами

        """
        j_indices = np.argwhere(array_with_sets[i, :] == array_with_sets[i, j])
        for idx_j in j_indices:
            array_with_sets[i, idx_j] = value

    def __cell_is_not_one_without_lower_border(self, array_with_sets, i,
                                               j) -> bool:
        """
        Функция для подсчета количество ячеек без нижней границы.

        Переприсваивает по индексам массива.

        Аргументы:
            i (int): Индекс текущей строки.
            j (int): Индекс текущей строки.
            value (int): Значение, на которое будет переприсваиватся
                все множество в строке, по текущему индексу.
            array_with_sets (np.ndarray): Массив с множествами

        Возвращает:
            bool: Возращает True если количество ячеек по индексу i и j больше 1
        """
        j_indices = np.argwhere(array_with_sets[i, :] == array_with_sets[i, j])

        count_cell = 0
        for idx_j in j_indices:
            if self.__maze_data.lower_walls[i, idx_j] != 1:
                count_cell += 1

        if count_cell > 1:
            return True
        return False
