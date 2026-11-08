import argparse


def calculate_sum() -> None:
    # Обработка аргументов и вывод суммы

    parser = argparse.ArgumentParser()

    # Сбор всех переданных позиционных аргументов
    parser.add_argument('args_list', nargs='*')

    # Разбор аргументов
    parser_args = parser.parse_args()
    params = parser_args.args_list

    # Проверка количества переданных параметров и вывод сообщений на экран
    if len(params) == 0:
        print("NO PARAMS")
        return
    elif len(params) == 1:
        print("TOO FEW PARAMS")
        return
    elif len(params) > 2:
        print("TOO MANY PARAMS")
        return

    # Нахождение суммы
    try:
        # Попытка преобразовать строки в целые числа и вычислить сумму
        result = int(params[0]) + int(params[1])
        print(result)

    except Exception as error:
        # Вывод имени класса исключения на экран в случае любой ошибки
        print(error.__class__.__name__)


if __name__ == '__main__':
    calculate_sum()
