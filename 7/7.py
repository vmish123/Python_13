import argparse


def process_arguments() -> None:
    # Обработка аргументов

    parser = argparse.ArgumentParser()

    # Сбор всех переданных позиционных аргументов
    parser.add_argument('parameters', nargs='*')

    # Разбор аргументов
    parsed_args = parser.parse_args()

    # Проверка списка параметров на пустоту
    if not parsed_args.parameters:
        # Вывод сообщения об отсутствии аргументов на экран
        print("no args")
    else:
        # Поочередный вывод каждого параметра на экран с новой строки
        for param in parsed_args.parameters:
            print(param)


if __name__ == '__main__':
    process_arguments()
