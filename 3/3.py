import os


def get_human_readable_size(size_in_bytes: float) -> str:
    # Получение размера файла в человекочитаемом формате
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']

    # Перевод размера в старшие единицы измерения
    for unit in units[:-1]:
        if round(size_in_bytes) < 1024:
            return f"{round(size_in_bytes)}{unit}"
        size_in_bytes /= 1024

    # Возврат размера в максимальной единице
    return f"{round(size_in_bytes)}{units[-1]}"


def get_path_size(path: str) -> int:
    # Рассчёт суммарного размера файла или каталога
    total_size = 0

    # Если путь является файлом
    if os.path.isfile(path):
        try:
            return os.path.getsize(path)
        except OSError:
            return 0

    # Рекурсивный обход каталога
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if not os.path.islink(file_path):
                try:
                    total_size += os.path.getsize(file_path)
                except OSError:
                    pass

    return total_size


def print_largest(target_path: str) -> None:
    # Вывод 10 самых больших объектов по указанному пути
    items_sizes = []

    try:
        # Получение списка всех элементов в указанной директории
        dir_contents = os.listdir(target_path)
    except OSError:
        # Вывод сообщения об ошибке на экран, если путь неверный
        print("Путь не существует, или у пользователя недостаточно прав")
        return

    # Подсчет размеров всех вложенных элементов
    for item_name in dir_contents:
        full_path = os.path.join(target_path, item_name)
        item_size = get_path_size(full_path)
        items_sizes.append((item_name, item_size))

    # Сортировка элементов по убыванию размера
    items_sizes.sort(key=lambda x: x[1], reverse=True)

    top_10 = items_sizes[:10]

    # Вывод результата
    for name, size in top_10:
        formatted_size = get_human_readable_size(size)
        print(f"{name:<50} - {formatted_size}")


if __name__ == '__main__':
    path_to_scan = input("Укажите путь: ")

    print_largest(path_to_scan)
