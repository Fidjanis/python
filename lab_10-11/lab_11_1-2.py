import sqlite3

# Подключение к базе данных (если не существует, она будет создана)
conn = sqlite3.connect('literature.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
CREATE TABLE Authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_year INTEGER
)
''')

cursor.execute('''
CREATE TABLE Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    publication_year INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
)
''')

cursor.execute('''
CREATE TABLE Genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE BookGenres (
    book_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES Books(id),
    FOREIGN KEY (genre_id) REFERENCES Genres(id),
    PRIMARY KEY (book_id, genre_id)
)
''')

conn.commit()
conn.close()
