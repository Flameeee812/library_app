import sqlite3 as sql
from ..library_funcs import library_funcs_utils as utils
import logger as log


def get_connection(path):
    """
    Функция для подключения к базе данных библиотеки.

    Параметры:
        1. path - путь к базе данных.
    """
    try:
        connection = sql.connect(path, check_same_thread=False)
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Library (
                book_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year TEXT NOT NULL,
                status TEXT DEFAULT "в наличии"
                )
            ''')
        connection.commit()
        log.db_logger.info("Подключение к базе данных прошло успешно.")

        return connection

    except sql.Error as e:
        print("Ошибка при подключении к базе данных.")
        log.db_logger.exception(f"Ошибка при подключении к БД: {e}")

        return None


def close_connection(connection):
    """
    Функция для закрытия соединения с базой данных.
    """
    try:
        connection.close()
        log.db_logger.info("База данных закрыта.")

    except sql.Error as e:
        print("Ошибка при закрытии соединения с базой данных.")
        log.db_logger.exception(f"Ошибка при закрытии базы данных: {e}")

    return None


def add_book(connection, title: str, author: str, year: str) -> str | None:
    """
    Функция для добавления книги в библиотеку.

    Параметры:
        1. connection - подключение к базе данных библиотеки.
        2. title - Название книги.
        3. author - Автор книги.
        4. year - Год выпуска книги.
    """
    try:
        cursor = connection.cursor()

        if utils.is_correct_data(title, author, year):
            cursor.execute("INSERT INTO Library (title, author, year) VALUES (?, ?, ?)", (title, author, year))
            connection.commit()
            log.db_logger.info(f"Книга добавлена: {title}, автор: {author}, id: {cursor.lastrowid}")

            book_id = cursor.lastrowid
            return book_id

    except sql.Error as e:
        print("Ошибка при добавлении книги.")
        log.db_logger.exception(f"Ошибка при добавлении книги: {e}")

    return None


def delete_book(connection, book_id: str) -> bool:
    """
    Функция для удаления книги из библиотеки

    Параметры:
        1. connection - подключение к базе данных библиотеки.
        2. book_id - id книги.
    """
    try:
        if utils.is_book_id_digit(book_id):
            cursor = connection.cursor()

            cursor.execute("SELECT 1 FROM Library WHERE book_id == ?", (book_id,))
            if cursor.fetchone() is None:
                print(f"Книги с ID {book_id} нет в библиотеке.")
                log.db_logger.exception(f"Ошибка при удалении книги: Книги с ID {book_id} нет в библиотеке.")
                return False

            cursor.execute("DELETE FROM Library WHERE book_id = ?", (book_id,))
            connection.commit()
            log.db_logger.info(f"Данные книги с ID {book_id} удалены.")

            return True

        return False

    except sql.Error as e:
        print("Ошибка при удалении книги.")
        log.db_logger.exception(f"Ошибка при удалении книги: {e}")

        return False


def get_book(connection, book_id: str) -> tuple | None:
    """
    Функция для отображения книгу по id

    Параметры:
        1. connection - подключение к базе данных библиотеки.
        2. title - Название книги.
        3. author - Автор книги.
        4. year - Год выпуска книги.
    """
    try:
        if utils.is_book_id_digit(book_id):
            cursor = connection.cursor()

            cursor.execute("SELECT book_id, title, author, year, status FROM Library WHERE book_id == ?", (book_id,))
            book = cursor.fetchone()
            connection.commit()

            return book

    except sql.Error as e:
        print("Ошибка при закрытии соединения с базой данных.")
        log.db_logger.exception(f"Ошибка при получении данных о книге: {e}")

    return None


def get_books(connection) -> list:
    """
    Функция для отображения всех книг библиотеки.

    Параметры:
        1. connection - подключение к базе данных библиотеки.
    """
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Library")
        library = cursor.fetchall()

        return library

    except sql.Error as e:
        print(f"Ошибка при получении списка книг.")
        log.db_logger.exception(f"Ошибка при получении списка книг: {e}")

        return []


def update_status(connection, book_id: str, status: str) -> bool:
    """
    Функция для изменения статуса книги по id.

    Параметры:
        1. connection - подключение к базе данных библиотеки.
        2. book_id - id книги.
    """
    try:
        if utils.is_book_id_digit(book_id):
            cursor = connection.cursor()
            if utils.is_status_correct(status):
                cursor.execute("SELECT status FROM Library WHERE book_id = ?", (book_id,))
                old_status = cursor.fetchone()[0]

                cursor.execute("UPDATE Library SET status = ? WHERE book_id = ?", (status, book_id))
                connection.commit()
                log.db_logger.info(f"Статус книги с ID {book_id} изменен с {old_status} на {status}.")

                return True

            log.db_logger.exception("Ошибка попытке обновить статус книги.")

        return False

    except sql.Error as e:
        print("Ошибка при обновлении статуса книги.")
        log.db_logger.exception(f"Ошибка попытке обновить статус книги: {e}")

        return False
