import argparse


def format_text_block(frame_height: int, frame_width: int, file_name: str) -> str:
    # Считывание файла, форматирование и вывод результата
    # Построчное чтение файла
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except Exception as error:
        return str(error)

    formatted_lines = []

    # Построчная обработка содержимого файла
    for line in lines:
        # Удаление символа переноса строки в конце
        line = line.rstrip('\r\n')

        # Если строка пустая
        if not line:
            formatted_lines.append('')
        else:
            # Нарезание строки на куски длиной frame_width
            for i in range(0, len(line), frame_width):
                formatted_lines.append(line[i:i + frame_width])

        if len(formatted_lines) >= frame_height:
            break

    # Обрезка списка строк до указанной высоты
    formatted_lines = formatted_lines[:frame_height]

    # Объединение итоговых строк через символ переноса и возврат результата
    return '\n'.join(formatted_lines)


def main():
    parser = argparse.ArgumentParser()

    # Добавление параметров
    parser.add_argument('--frame-height', type=int, required=True)
    parser.add_argument('--frame-width', type=int, required=True)
    parser.add_argument('file_name', type=str)

    # Разбор аргументов
    args = parser.parse_args()

    # Вызов функции с логикой форматирования
    result = format_text_block(
        frame_height=args.frame_height,
        frame_width=args.frame_width,
        file_name=args.file_name
    )

    # Вывод результата
    print(result)


if __name__ == '__main__':
    main()
