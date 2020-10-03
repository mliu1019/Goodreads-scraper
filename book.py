import requests
from bs4 import BeautifulSoup

class Book:
    def __init__(self, book_url='', title='', book_id='', ISBN='', author_url='', author='', rating=0.0, rating_count=0, review_count=0, image_url='', similar_books=[]):
        self.book_url = book_url # URL of the book
        self.title = title # name of the book
        self.book_id = book_id # a unique identifier of the book
        self.ISBN = ISBN # the ISBN of the book
        self.author_url = author_url # URL of the author of the book
        self.author = author # author of the book
        self.rating = rating # the rating of the book
        self.rating_count = rating_count # the number of rating the book received
        self.review_count = review_count # the number of the comments the book received
        self.image_url = image_url # a URL of the book's image
        self.similar_books = similar_books # a list of books similar or related to the book


def create_book(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    book_url = soup.find('link', href=True)['href']
    title = soup.find('h1', class_='gr-h1').get_text().strip()
    book_id = soup.find('input', {'name':'book_id'})['value']
    ISBN = soup.find('meta', property='books:isbn')['content']
    author_url = soup.find('a', class_='authorName')['href']
    author = soup.find('a', class_='authorName').get_text()
    rating = float(soup.find('span', itemprop='ratingValue').get_text().strip())
    rating_count = int(soup.find('meta', itemprop='ratingCount')['content'])
    review_count = int(soup.find('meta', itemprop='reviewCount')['content'])
    image_url = soup.find('img', id='coverImage')['src']
    similar_books = [book.find('a')['href'].replace('https://www.goodreads.com/book/show/', '') for book in soup.find_all('li', class_='cover')]

    book = Book(book_url, title, book_id, ISBN, author_url, author, rating, rating_count, review_count, image_url, similar_books)
    
    return book


def store_book(books, book):
    books.append({
        'book_url': book.book_url,
        'title': book.title,
        'book_id': book.book_id,
        'ISBN': book.ISBN,
        'author_url': book.author_url,
        'author': book.author,
        'rating': book.rating,
        'rating_count': book.rating_count,
        'review_count': book.review_count,
        'image_url': book.image_url,
        'similar_books': book.similar_books
    })