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


def get_files_info() -> str:
    # Получение информации о файлах в текущей директории в одну строку
    files_data = []

    # Получение списка элементов в текущей директории
    for item in os.listdir('.'):
        # Проверка, является ли текущий элемент файлом
        if os.path.isfile(item):
            file_size = os.path.getsize(item)
            formatted_size = get_human_readable_size(file_size)
            files_data.append(f"{item} {formatted_size}")

    # Формирование единой строки
    return '\n'.join(files_data)


if __name__ == '__main__':
    result_string = get_files_info()
    print(result_string)
