from book import *
from author import *
import json

url = 'https://www.goodreads.com/book/show/3735293-clean-code'
book = create_book(url)

books = []
store_book(books, book)
visited = set()
visited.add(book.book_id)

i = 0
while len(books) < 20:
    curr = books[i]
    for book_id in curr['similar_books']:
        if book_id not in visited:
            book = create_book('https://www.goodreads.com/book/show/'+book_id)
            store_book(books, book)
    i += 1

with open('book.txt', 'w') as outfile:
    json.dump(books, outfile)




url = books[0]['author_url']
author = create_author(url)

authors = []
store_author(authors, author)
visited = set()
visited.add(author.author_id)

i = 0
while len(authors) < 10:
    curr = authors[i]
    for author_id in curr['related_authors']:
        if author_id not in visited:
            author = create_author('https://www.goodreads.com/author/show/'+author_id)
            store_author(authors, author)
    i += 1

with open('author.txt', 'w') as outfile:
    json.dump(authors, outfile)
