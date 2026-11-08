import zipfile


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


def build_file_tree(archive_path: str) -> dict:
    # Построение древовидной структуры файлов и каталогов из архива
    tree = {}

    # Открытие zip-архива для чтения
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            for info in zip_ref.infolist():
                if not info.filename:
                    continue

                # Разбиение пути на составляющие
                path_parts = info.filename.strip('/').split('/')
                current_node = tree

                # Проход по частям пути для формирования дерева
                for i, part in enumerate(path_parts):
                    is_last_part = (i == len(path_parts) - 1)

                    if is_last_part and not info.is_dir():
                        # Запись размера, если это конечный файл
                        current_node[part] = info.file_size
                    else:
                        # Создание узла для каталога, если его еще нет
                        if part not in current_node:
                            current_node[part] = {}
                        current_node = current_node[part]

    except OSError:
        print("Путь не существует, или у пользователя недостаточно прав")

    return tree


def print_file_tree(node: dict, indent_level: int = 0) -> None:
    # Рекурсивный вывод файловой структуры
    # Определение отступа
    indent = "  " * indent_level

    # Проход по отсортированным элементам
    for name, content in sorted(node.items()):
        if isinstance(content, dict):
            # Вывод имени каталога на экран
            print(f"{indent}{name}")
            # Рекурсивный вызов для вложенного содержимого
            print_file_tree(content, indent_level + 1)
        else:
            # Получение форматированного размера файла
            size_str = get_human_readable_size(content)
            # Вывод имени файла и его размера на экран
            print(f"{indent}{name} {size_str}")


if __name__ == '__main__':
    archive_name = input("Укажите путь до архива: ")

    file_tree = build_file_tree(archive_name)

    if file_tree:
        print_file_tree(file_tree)
