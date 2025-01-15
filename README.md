Библиотечное приложение для учета книг.

Это консольное приложение предназначено для учета, анализа и изменения данных о книжной библиотеке. 
Оно предоставляет набор команд для управления базой данных книг.
Приложение написано в процедурном стиле, также, программа не использует сторонних библиотек, кроме стандартных, для работы с базой данных и логированием.

*Доступные команды:
    1. /add_book         - Добавить книгу (параметры: title, author, year).
    2. /delete_book      - Удалить книгу по ID.
    3. /get_book         - Найти книгу по title, author или year.
    4. /get_books        - Показать все книги в библиотеке.
    5. /update_status    - Обновить статус книги ('в наличии' или 'выдана').
    6. /end              - Завершить работу приложения.


*Пример работы программы:

> /start
Приложение запущено. Добро пожаловать!
> /help
Для того, чтобы узнать список команд - введите /help
> /add_book
Введите название книги: Война и мир
Введите автора книги: Лев Толстой
Введите год выпуска книги: 1869
Книга добавлена: Война и мир - Лев Толстой (1869), ID: 1
> /get_books
ID: 1, Название: Война и мир, Автор: Лев Толстой, Год: 1869, Статус: в наличии


*Требования:
Для работы приложения необходим Python версии 3.x и библиотека sqlite3, которая встроена в стандартную библиотеку Python.
