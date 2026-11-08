import sys


def process_arguments() -> None:
    # Обработка аргументов

    need_sort = False

    # Получение всех переданных аргументов
    raw_args = sys.argv[1:]

    # Проверка наличия флага сортировки
    if '--sort' in raw_args:
        need_sort = True
        raw_args.remove('--sort')

    parsed_data = []

    # Обработка оставшихся аргументов
    for arg in raw_args:
        # Разделение строки на ключ и значение по символу '='
        key, value = arg.split('=')
        parsed_data.append((key, value))

    # Сортировка списка, если был передан флаг --sort
    if need_sort:
        parsed_data.sort()

    # Вывод результатов на экран
    for key, value in parsed_data:
        print(f"Key: {key} Value: {value}")


if __name__ == '__main__':
    process_arguments()
