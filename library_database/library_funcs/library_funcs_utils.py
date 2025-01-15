from string import punctuation, digits
import datetime as date


def is_correct_data(title: str, author: str, year: str) -> bool:
    """
    Утилита для проверки коррекстности введённых title/author/year.

    Параметры:
    1. title - Название книги
    2. author - Автор книги
    3. year - Год выпуска книги
    """

    incorrect_title_chars = "".join(punctuation.split("-"))
    incorrect_author_chars = "".join(punctuation.split("-.")) + digits
    current_year = date.datetime.now().year

    # ошибка, если в названии книги есть знак пунктуации помимо дефиса
    if any([char in incorrect_title_chars for char in title]) or not title:
        print("Ошибка: введено некорректоное название книги.")
        return False

    # ошибка, если в году издания книги хотя бы один знак - это цифра/знак пунктуации помимо тире
    if any([char in incorrect_author_chars for char in author]) or not author:
        print("Ошибка: введено некорректоное имя автора.")
        return False

    # ошибка, если в году издания книги хотя бы один знак не цифра
    try:
        year = int(year)
        if year > current_year or year < 0:
            print("Ошибка: введен год в будущем.")
            return False
    except ValueError:
        print("Ошибка: введено некорректное значение. Введите числовое значение для года.")
        return False

    return True


def is_book_id_digit(book_id: str) -> bool:
    """
    Утилита для проверки корректности введённого id книги.

    Параметры:
    1. book_id - id книги в базе данных.
    """
    if book_id.isdigit():
        return True

    print("Ошибка: введено некорректное id книги.")
    return False


def is_status_correct(status: str) -> bool:
    """
    Утилита для проверки корректности введённого статуса книги.

    Параметры:
     1. status - статус книги
    """
    if status == "выдана" or status == "в наличии":
        return True

    else:
        print("Ошибка: введён некорректный статус.")
        return False
