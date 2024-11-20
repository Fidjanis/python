from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  # HTML-страница с формами


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    publication_year = request.form['publication_year']

    conn = sqlite3.connect('literature.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Books (title, author_id, publication_year) VALUES (?, ?, ?)',
                   (title, author_id, publication_year))

    conn.commit()
    conn.close()

    return 'Book added!'


@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect('literature.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()

    conn.close()

    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)
