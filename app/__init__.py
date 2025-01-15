from app import app_functions as app_func


def lib_app() -> None:

    print("""Программа для создания, управления и редактирования собственной библиотеки. 
Для начала работы введите /start.""")

    try:
        while True:
            start = input("> ").strip()
            if start.strip() == "/start":
                print("Приложение запущено. Добро пожаловать!")
                break
            else:
                print("Некорректный ввод. Для запуска приложения введите /start.")

            # булевая переменная для проверки того, выводилась ли подсказка о команде /help

        help_displayed = False

        while True:
            if not help_displayed:
                print("""Для того, чтобы узнать список команд - введите /help""")
            help_displayed = True

            message = input("> ").strip()

            if message == "/help":
                app_func.app_help()

            elif message == "/add_book":
                app_func.app_add_book()

            elif message == "/delete_book":
                app_func.app_delete_book()

            elif message == "/get_book":
                app_func.app_get_book()

            elif message == "/get_books":
                app_func.app_get_books()

            elif message == "/update_status":
                app_func.app_update_status()

            elif message == "/end":
                app_func.app_exit()
                break

            else:
                print("Некорректный ввод. Попробуйте ещё раз.")

    except KeyboardInterrupt:
        app_func.app_exit()

    finally:
        app_func.app_close_database()

    return None
