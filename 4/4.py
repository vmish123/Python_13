import os
import shutil
from datetime import datetime


def make_reserve_arc(source: str, dest: str) -> None:
    # Создание ZIP-архива
    # Получение текущей даты и времени
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Извлечение имени исходного каталога для добавления его в название архива
    source_folder_name = os.path.basename(os.path.normpath(source))

    # Защита от случая, если source указывает на корень диска
    if not source_folder_name:
        source_folder_name = "archive"

    # Формирование итогового имени архива
    archive_filename = f"{source_folder_name}_{current_time}"

    # Создание каталога dest, если он еще не существует
    os.makedirs(dest, exist_ok=True)
    archive_full_path = os.path.join(dest, archive_filename)

    # Создание ZIP-архива
    shutil.make_archive(base_name=archive_full_path, format='zip', root_dir=source)


if __name__ == '__main__':
    make_reserve_arc('./test', '.')
