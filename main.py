"""Main entry point for the scraper."""
import json
import argparse
from book import create_book, store_book
from author import create_author, store_author
from database import mongoclient
from dotenv import load_dotenv

def scrape(initial_url="", book_count=200, author_count=50):
    db = mongoclient()

    db.books.remove({})
    db.authors.remove({})

    # https://www.goodreads.com/book/show/3735293-clean-code
    book = create_book(initial_url)

    book_arr = [store_book(book)]
    visited = set()
    visited.add(initial_url.replace('https://www.goodreads.com/book/show/', ''))

    i = 0
    while len(book_arr) < book_count:
        curr = book_arr[i]
        for book_id in curr['similar_books']:
            if book_id not in visited:
                book = create_book('https://www.goodreads.com/book/show/'+book_id)
                book_arr.append(store_book(book))
                db.books.insert_one(store_book(book))
                visited.add(book_id)

        i += 1

    with open('book.txt', 'w') as outfile:
        json.dump(book_arr, outfile)


    url = book_arr[0]['author_url']
    author = create_author(url)

    author_arr = [store_author(author)]
    visited = set()
    visited.add(url.replace('https://www.goodreads.com/author/show/', ''))

    i = 0
    while len(author_arr) < author_count:
        curr = author_arr[i]
        for author_id in curr['related_authors']:
            if author_id not in visited:
                author = create_author('https://www.goodreads.com/author/show/'+author_id)
                author_arr.append(store_author(author))
                db.authors.insert_one(store_author(author))
                visited.add(author_id)
        i += 1

    with open('author.txt', 'w') as outfile:
        json.dump(author_arr, outfile)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='CS242 Assignment 2 User Inputs.')

    parser._action_groups.pop()

    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument('--url', help='URL to begin.', required=True, metavar="")
    optional.add_argument('--nbook', help='Number of books to scrape.', default=200, metavar="")
    optional.add_argument('--nauthor', help='Number of authors to scrape.', default=50, metavar="")
    args = parser.parse_args()
    
    load_dotenv("config.env")

    scrape(initial_url=args.url, book_count=args.nbook, author_count=args.nauthor)