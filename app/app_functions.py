import library_database as lib_db


Library = lib_db.Library


def app_help() -> None:
    """Вывод списка доступных команд."""

    print("""
    Доступные команды:
    1. /add_book         - Добавить книгу (параметры: title, author, year).
    2. /delete_book      - Удалить книгу по ID.
    3. /get_book         - Найти книгу по title, author или year.
    4. /get_books        - Показать все книги в библиотеке.
    5. /update_status    - Обновить статус книги ('в наличии' или 'выдана').
    6. /end              - Завершить работу приложения.
        """)

    return None


def app_add_book() -> None:
    """
    Добавление новой книги в библиотеку.
    """

    title = input("Введите название книги:\n> ")
    author = input("Введите автора книги:\n> ")
    year = input("Введите год написания книги:\n> ")

    book_id = lib_db.add_book(connection=Library, title=title, author=author, year=year)

    if book_id:
        print("Книга успешно добавлена!")
        print(f"ID книги: {book_id}")

    else:
        print("Не удалось добавить книгу.")

    return None


def app_delete_book() -> None:
    """
    Удаление книги из библиотеки по ID.
    """

    book_id = input("Введите id книги:\n> ")

    is_delete = lib_db.delete_book(connection=Library, book_id=book_id)

    if is_delete:
        print("Книга успешно удалена!")

    else:
        print("Не удалось удалить книгу.")

    return None


def app_get_book() -> None:
    """
    Получение информации о книге по её ID.
    """

    book_id = input("Введите id книги:\n> ")

    book = lib_db.get_book(connection=Library, book_id=book_id)

    if book:
        print(f"Информация о книге:")
        print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Статус: {book[4]}")

    else:
        print("Ну удалось получить информацию о книге.")

    return None


def app_get_books() -> None:
    """
    Получение списка всех книг в библиотеке.
    """

    books = lib_db.get_books(connection=Library)

    if books:
        print("Список книг в библиотеке:")
        for book in books:
            print(f"ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год: {book[3]}, Статус: {book[4]}")
    else:
        print("Библиотека пуста.")

    return None


def app_update_status() -> None:
    """
    Обновление статуса книги.
    """

    book_id = input("Введите id книги:\n> ")
    status = input("Введите статус книги:\n> ")

    is_update_status = lib_db.update_status(connection=Library, book_id=book_id, status=status)
    if is_update_status:
        print("Статус успешно обновлен!")

    else:
        print("Не удалось обновить статус книги.")


def app_exit() -> None:
    """
    Завершение работы приложения.
    """

    print("Программа завершена.\nДо скорых встреч!")

    return None


def app_close_database() -> None:
    lib_db.close_connection(lib_db.Library)

    return None
