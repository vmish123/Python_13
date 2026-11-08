from datetime import datetime
import schedule


def say_ku() -> None:
    # Определение часа и вывод соответствующей строки "Ку"
    # Получение текущего часа в 24-часовом формате
    current_hour = datetime.now().hour

    # Перевод времени в 12-часовой формат
    count = current_hour % 12

    # Замена 0 на 12
    if count == 0:
        count = 12

    # Формирование строки
    result_string = " ".join(["Ку"] * count)

    # Вывод сформированной строки
    print(result_string)


if __name__ == '__main__':
    # Запуск каждый час ровно в 00 минут
    schedule.every().hour.at(":00").do(say_ku)

    # Бесконечный цикл для проверки и запуска запланированных задач
    while True:
        schedule.run_pending()
