from flask import Flask
# from controller.book import book, books
from controller.book import BooksAPI, BookAPI

app = Flask(__name__, static_url_path='/static', static_folder="static")


@app.route('/')
def hello_world():
    return 'Hello, World!'

app.add_url_rule('/books', view_func=BooksAPI.as_view('books'))
app.add_url_rule('/book', view_func=BookAPI.as_view('book'))

# app.register_blueprint(books, url_prefix='/books')
# app.register_blueprint(book, url_prefix='/book')

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv('config.env')

    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)