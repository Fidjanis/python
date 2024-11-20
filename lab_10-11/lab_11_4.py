import sqlite3
conn = sqlite3.connect('literature.db')
cursor = conn.cursor()

# Запрос 1: Все книги и их авторы
cursor.execute('''
SELECT Books.title, Authors.name 
FROM Books 
JOIN Authors ON Books.author_id = Authors.id
''')
books_with_authors = cursor.fetchall()

# Запрос 2: Количество книг по каждому автору
cursor.execute('''
SELECT Authors.name, COUNT(Books.id) 
FROM Authors 
LEFT JOIN Books ON Authors.id = Books.author_id 
GROUP BY Authors.name
''')
books_count_by_author = cursor.fetchall()

# Запрос 3: Все жанры и количество книг в каждом жанре
cursor.execute('''
SELECT Genres.name, COUNT(BookGenres.book_id) 
FROM Genres 
LEFT JOIN BookGenres ON Genres.id = BookGenres.genre_id 
GROUP BY Genres.name
''')
genres_count = cursor.fetchall()

print(books_with_authors)
print(books_count_by_author)
print(genres_count)

conn.close()
