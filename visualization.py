"""This creates visualizations based on ranking of books and authors."""
import json
import matplotlib.pyplot as plt

book_arr = json.load(open('book.json'))
author_arr = json.load(open('author.json'))


def visualize_authors(author_arr):
    """Visualizes the top 15 authors with the highest ratings."""
    author_arr = sorted(author_arr, key = lambda i: i['rating'], reverse=True)[:15]

    authors = []
    ratings = []

    for author in author_arr:
        name = author['name'].split()[0] + '\n' + author['name'].split()[1]
        authors.append(name)
        ratings.append(author['rating'])

    plt.figure(figsize=(15, 10))
    for i, v in enumerate(ratings):
        plt.text(i-0.25, v+0.02, v)
    plt.bar(authors, ratings)
    plt.xlabel('Author')
    plt.ylabel('Rating')
    plt.title('Top 15 Authors with Highest Ratings')
    plt.tight_layout()
    plt.savefig('static/vis1.png')


def visualize_books(book_arr):
    """Visualizes the top 15 books with the most number of similar books."""
    book_arr = sorted(book_arr, key = lambda i: i['review_count'], reverse=True)[:15]

    books = []
    review_counts = []

    for book in book_arr:
        title = ''
        for word in book['title'].split():
            title += word
            title += '\n'
        books.append(title)
        review_counts.append(book['review_count'])

    plt.figure(figsize=(15, 10))
    for i, v in enumerate(review_counts):
        plt.text(i-0.25, v+0.02, v)
    plt.bar(books, review_counts)
    plt.xlabel('Title')
    plt.ylabel('Review Count')
    plt.title('Top 15 Books with Most Reviews')
    plt.tight_layout()
    plt.savefig('static/vis2.png')


visualize_authors(author_arr)
visualize_books(book_arr)