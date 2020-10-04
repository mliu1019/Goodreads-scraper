"""This creates a graph based on book and author relations."""
import json
import networkx as nx
import matplotlib.pyplot as plt

book_arr = json.load(open('book.json'))
author_arr = json.load(open('author.json'))

G = nx.Graph()

books = set()
authors = set()

for book in book_arr:
    book_id = book['book_url'].replace('https://www.goodreads.com/book/show/', '')
    G.add_node(book_id)
    books.add(book_id)
    G.add_node(book['author'])
    authors.add(book['author'])
    G.add_edge(book_id, book['author'])

    for related in book['similar_books']:
        if related not in books:
            G.add_node(related)
            books.add(related)
        G.add_edge(book_id, related)

for author in author_arr:
    author_id = author['author_url'].replace('https://www.goodreads.com/author/show/', '')
    G.add_node(author_id)
    authors.add(author_id)

    for related in author['related_authors']:
        if related not in authors:
            G.add_node(related)
            authors.add(related)
        G.add_edge(author_id, related)

    for related in author['author_books']:
        if related not in books:
            G.add_node(related)
            books.add(related)
        G.add_edge(author_id, related)

color_map = []

for node in G:
    if node in books:
        color_map.append('blue')
    elif node in authors:
        color_map.append('red')

nx.draw(G, node_color=color_map, node_size=5, edge_color='grey')
plt.show()
