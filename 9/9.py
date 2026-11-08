import argparse


def process_arguments() -> None:
    # Обработка аргументов

    parser = argparse.ArgumentParser()

    # Добавление необязательного аргумента --sort
    parser.add_argument('--sort', action='store_true')

    # Сбор всех переданных позиционных аргументов
    parser.add_argument('pairs', nargs='*')

    # Разбор аргументов
    parsed_args = parser.parse_args()

    parsed_data = []

    # Обработка собранных пар
    for item in parsed_args.pairs:
        # Разделение строки на ключ и значение по символу "="
        key, value = item.split('=')
        parsed_data.append((key, value))

    # Сортировка списка кортежей, если был передан флаг --sort
    if parsed_args.sort:
        parsed_data.sort()

    # Вывод результатов на экран
    for key, value in parsed_data:
        print(f"Key: {key} Value: {value}")


if __name__ == '__main__':
    process_arguments()
