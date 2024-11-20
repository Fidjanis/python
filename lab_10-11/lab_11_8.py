import json
import sqlite3

def export_books_to_json():
    conn = sqlite3.connect('literature.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()

    books_list = [{'id': book[0], 'title': book[1], 'author_id': book[2], 'publication_year': book[3]} for book in
                  books]

    with open('books.json', 'w') as json_file:
        json.dump(books_list, json_file)

    conn.close()


export_books_to_json()
