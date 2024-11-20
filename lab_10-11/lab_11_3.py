import sqlite3
# Заполнение таблиц данными
conn = sqlite3.connect('literature.db')
cursor = conn.cursor()

# Добавление авторов
authors = [
    ('Lev Tolstoy', 1828),
    ('Fyodor Dostoevsky', 1821),
    ('Jane Austen', 1775)
]
cursor.executemany('INSERT INTO Authors (name, birth_year) VALUES (?, ?)', authors)

# Добавление книг
books = [
    ('War and Peace', 1, 1869),
    ('Crime and Punishment', 2, 1866),
    ('Pride and Prejudice', 3, 1813)
]
cursor.executemany('INSERT INTO Books (title, author_id, publication_year) VALUES (?, ?, ?)', books)

# Добавление жанров
genres = [
    ('Fiction',),
    ('Classic',),
    ('Drama',)
]
cursor.executemany('INSERT INTO Genres (name) VALUES (?)', genres)

# Связывание книг и жанров
book_genres = [
    (1, 1),  # War and Peace - Fiction
    (1, 2),  # War and Peace - Classic
    (2, 1),  # Crime and Punishment - Fiction
    (2, 2),  # Crime and Punishment - Classic
    (3, 1),  # Pride and Prejudice - Fiction
    (3, 2)   # Pride and Prejudice - Classic
]
cursor.executemany('INSERT INTO BookGenres (book_id, genre_id) VALUES (?, ?)', book_genres)

conn.commit()
conn.close()