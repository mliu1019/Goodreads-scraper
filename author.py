import requests
from bs4 import BeautifulSoup

class Author:
    def __init__(self, name='', author_url='', author_id='', rating=0.0, rating_count=0, review_count=0, image_url='', related_authors=[], author_books=[]):
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
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    name = soup.find('h1', class_='authorName').get_text().strip()
    author_url = soup.find('link', href=True)['href']
    author_id = author_url.replace('https://www.goodreads.com/author/show/', '').split('.')[0]
    rating = float(soup.find('span', itemprop='ratingValue').get_text().strip())
    rating_count = int(soup.find('span', itemprop='ratingCount')['content'])
    review_count = int(soup.find('span', itemprop='reviewCount')['content'])
    image_url = soup.find('meta', itemprop='image')['content']

    sim_url = 'https://www.goodreads.com/' + soup.find('div', class_='hreview-aggregate').find_all('a')[1]['href']
    sim_req = requests.get(sim_url)
    sim_soup = BeautifulSoup(sim_req.content, 'html.parser')
    related_authors = [author['href'].replace('https://www.goodreads.com/author/show/', '') for author in sim_soup.find_all('a', class_='gr-h3')[1:]]

    author_books = [book.get_text() for book in soup.find_all('span', {'itemprop':'name', 'role':'heading'})]

    author = Author(name, author_url, author_id, rating, rating_count, review_count, image_url, related_authors, author_books)

    return author


def store_author(authors, author):
    authors.append({
        'name': author.name,
        'author_url': author.author_url,
        'author_id': author.author_id,
        'rating': author.rating,
        'rating_count': author.rating_count,
        'review_count': author.review_count,
        'image_url': author.image_url,
        'related_authors': author.related_authors,
        'author_books': author.author_books
    })