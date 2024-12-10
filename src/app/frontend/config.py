import os
import sys


def resource_path(relative_path, base_path=None):
    """
    Получение абсолютного пути к ресурсам
    """
    if not relative_path:
        return None

    if os.path.isabs(relative_path):
        result_path = relative_path

    else:
        base_path = os.getcwd()
        result_path = os.path.normpath(os.path.join(base_path, relative_path))

        if os.path.isfile(result_path):
            pass

        else:
            try:
                base_path = sys._MEIPASS

            except Exception as err:
                if base_path is None:
                    base_path = os.getcwd()

        result_path = os.path.normpath(os.path.join(base_path, relative_path))

    return result_path

IMAGE_ICON_PATH = resource_path('statics/maze.ico')