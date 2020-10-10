from flask import Flask, Blueprint
# from controller.book import book, books
from controller.book import BooksAPI, BookAPI

app = Flask(__name__, static_url_path='/', static_folder="static")

@app.route('/')
def index():
    return "CS242 Assignment2."

apis = Blueprint('api', __name__)

apis.add_url_rule('/books', view_func=BooksAPI.as_view('books'))
apis.add_url_rule('/book', view_func=BookAPI.as_view('book'))

app.register_blueprint(apis, url_prefix='/api')

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv('config.env')

    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)