"""
The Author class and scraper functions.
Initializes an Author object for database and visualization purposes.
"""
import requests
from bs4 import BeautifulSoup


class Author:
    """The Author class."""
    def __init__(self, name='', author_url='', author_id='', rating=0.0, rating_count=0,
                review_count=0, image_url='', related_authors=None, author_books=None):
        self.name = name # name of the author
        self.author_url = author_url # the page URL
        self.author_id = author_id # a unique identifier of the author
        self.rating = rating # the rating of the author
        self.rating_count = rating_count # the number of rating the author received
        self.review_count = review_count # the number of the comments the author received
        self.image_url = image_url # a URL of the author's image
        self.related_authors = related_authors # a list of authors related to the author
        self.author_books = author_books # a list of books by the author


def create_author(url):
    """Creates a Author instance."""
    try:
        req = requests.get(url)
    except:
        return None

    soup = BeautifulSoup(req.content, 'html.parser')

    try:
        name = soup.find('h1', class_='authorName').get_text().strip()
    except TypeError:
        name = ''

    try:
        author_url = soup.find('link', href=True)['href']
    except TypeError:
        author_url = ''

    try:
        author_id = author_url.replace('https://www.goodreads.com/author/show/', '').split('.')[0]
    except TypeError:
        author_id = ''

    try:
        rating = float(soup.find('span', itemprop='ratingValue').get_text().strip())
    except TypeError:
        rating = 0.0

    try:
        rating_count = int(soup.find('span', itemprop='ratingCount')['content'])
    except TypeError:
        rating_count = 0

    try:
        review_count = int(soup.find('span', itemprop='reviewCount')['content'])
    except TypeError:
        review_count = 0

    try:
        image_url = soup.find('meta', itemprop='image')['content']
    except TypeError:
        image_url = ''

    try:
        sim_url = 'https://www.goodreads.com/' + soup.find('div',
                class_='hreview-aggregate').find_all('a')[1]['href']
    except TypeError:
        sim_url = ''

    try:
        sim_soup = BeautifulSoup(requests.get(sim_url).content, 'html.parser')
        related_authors = [author['href'].replace('https://www.goodreads.com/author/show/', '')
                        for author in sim_soup.find_all('a', class_='gr-h3')[1:]]
    except TypeError:
        related_authors = None

    try:
        author_books = [book.get_text() for book in
                    soup.find_all('span', {'itemprop':'name', 'role':'heading'})]
    except TypeError:
        author_books = None

    author = Author(name, author_url, author_id, rating, rating_count,
                    review_count, image_url, related_authors, author_books)

    return author


def store_author(author):
    """Stores a Author into the dictionary form."""
    author_dict = {
        'name': author.name,
        'author_url': author.author_url,
        'author_id': author.author_id,
        'rating': author.rating,
        'rating_count': author.rating_count,
        'review_count': author.review_count,
        'image_url': author.image_url,
        'related_authors': author.related_authors,
        'author_books': author.author_books
    }

    return author_dict
