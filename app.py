"""
Entry point for the API. Includes queries and visualizations.
"""

from flask import Flask, Blueprint, send_file
from controller.book import BooksAPI, BookAPI
from controller.author import AuthorsAPI, AuthorAPI
from controller.utils import find_author, find_book

app = Flask(__name__, static_url_path='/', static_folder="static")

@app.route('/')
def index():
    return "CS242 Assignment2."

@app.route('/query/most-book-authors')
def most_book_authors():
    ret = find_author()
    return ret[0]['_id']

@app.route('/query/most-similar-books')
def most_similar_books():
    ret = find_book()
    return ret[0]['_id']

@app.route('/vis/rank-authors')
def visualize_author_rank():
    return send_file('static/vis1.png')

@app.route('/vis/rank-books')
def visualize_book_rank():
    return send_file('static/vis2.png')
    

apis = Blueprint('api', __name__)

apis.add_url_rule('/books', view_func=BooksAPI.as_view('books'))
apis.add_url_rule('/book', view_func=BookAPI.as_view('book'))
apis.add_url_rule('/authors', view_func=AuthorsAPI.as_view('authors'))
apis.add_url_rule('/author', view_func=AuthorAPI.as_view('author'))

app.register_blueprint(apis, url_prefix='/api')

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv('config.env')

    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
