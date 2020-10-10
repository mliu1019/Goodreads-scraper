import unittest

# class Testing(unittest.TestCase):
#     def test_databaseconnection(self):
#         import pymongo as pm
#         from database import mongoclient

#         raised = False
#         try:
#             cli = mongoclient()
#             cli.list_collection_names()
#         except Exception as e:
#             print(e)
#             raised = True

#         self.assertFalse(raised, "Shoud not raise.")

#     def test_scrape_book(self):
#         from book import create_book
#         book = create_book("https://www.goodreads.com/book/show/3735293-clean-code")
#         self.assertEqual(book.book_url, "https://www.goodreads.com/book/show/3735293-clean-code")
#         self.assertEqual(book.title, "Clean Code: A Handbook of Agile Software Craftsmanship")
#         self.assertEqual(book.isbn, 9780132350884)
        

#     def test_scrape_author(self):
#         from author import create_author
#         author = create_author("https://www.goodreads.com/author/show/45372.Robert_C_Martin")
#         self.assertEqual(author.name, "Robert C. Martin")
#         self.assertEqual(author.author_url, "https://www.goodreads.com/author/show/45372.Robert_C_Martin")
#         self.assertEqual(author.author_id, "45372")


#     def test_scrape_book_related(self):
#         from book import create_book
#         book = create_book("https://www.goodreads.com/book/show/3735293-clean-code")
#         self.assertEqual(book.author_url, "https://www.goodreads.com/author/show/45372.Robert_C_Martin")
#         self.assertEqual(book.author, "Robert C. Martin")
#         self.assertEqual(book.image_url, "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436202607l/3735293._SX318_.jpg")


#     def test_scrape_author_related(self):
#         from author import create_author
#         author = create_author("https://www.goodreads.com/author/show/45372.Robert_C_Martin")
#         self.assertEqual(author.image_url, "https://images.gr-assets.com/authors/1490470967p5/45372.jpg")


#     def test_scrape_book_hard(self):
#         from book import create_book
#         book = create_book("https://www.goodreads.com/book/show/3735293-clean-code")
#         self.assertTrue("4099.The_Pragmatic_Programmer" in book.similar_books)
#         self.assertTrue("85009.Design_Patterns" in book.similar_books)
#         self.assertTrue("44936.Refactoring" in book.similar_books)

    
#     def test_scrape_author_hard(self):
#         from author import create_author
#         author = create_author("https://www.goodreads.com/author/show/45372.Robert_C_Martin")
#         self.assertTrue("2815.Andy_Hunt" in author.related_authors)
#         self.assertTrue("3307.Steve_McConnell" in author.related_authors)
#         self.assertTrue("The Clean Coder: A Code of Conduct for Professional Programmers" in author.author_books)
#         self.assertTrue("Clean Architecture" in author.author_books)


class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from app import app
        self._app = app


    def test_serverup(self):
        api = self._app.test_client(self)
        resp = api.get('/', content_type='html/text')
        self.assertEqual(resp.status_code, 200)
        
    def test_bookapi_response(self):
        api = self._app.test_client(self)
        body = {
            'isbn': 12314124
        }
        resp = api.put('/books?book_id=4099&rating=4.32', json=body)
        self.assertEqual(resp.status_code, 200)

        resp = api.get('/books?isbn=214214214')
        self.assertEqual(resp.status_code, 200)

        # self.assertEqual(resp.status_code, 200)

    def test_bookapi_correctness(self):
        api = self._app.test_client(self)
        body = [{
            "author": "Erich Gamma1",
            "author_url": "https://www.goodreads.com/author/show/48622.Erich_Gamma",
            "book_id": "85009",
            "book_url": "https://www.goodreads.com/book/show/85009.Design_Patterns",
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348027904l/85009.jpg",
            "isbn": "123456789",
            "rating": 4.18,
            "rating_count": 9855,
            "review_count": 351,
            "similar_books": [
                "3735293-clean-code",
                "44936.Refactoring",
            ],
            "title": "Design Patterns: Elements of Reusable Object-Oriented Software"
        }, 
        {
            "author": "Erich Gamma2",
            "author_url": "https://www.goodreads.com/author/show/48622.Erich_Gamma",
            "book_id": "85009",
            "book_url": "https://www.goodreads.com/book/show/85009.Design_Patterns",
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348027904l/85009.jpg",
            "isbn": "1234567892",
            "rating": 4.18,
            "rating_count": 9855,
            "review_count": 351,
            "similar_books": [
                "3735293-clean-code",
                "44936.Refactoring",
            ],
            "title": "Design Patterns: Elements of Reusable Object-Oriented Software"
        }, 
        {
            "author": "Erich Gamma3",
            "author_url": "https://www.goodreads.com/author/show/48622.Erich_Gamma",
            "book_id": "85009",
            "book_url": "https://www.goodreads.com/book/show/85009.Design_Patterns",
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348027904l/85009.jpg",
            "isbn": "1234567892",
            "rating": 4.18,
            "rating_count": 9855,
            "review_count": 351,
            "similar_books": [
                "3735293-clean-code",
                "44936.Refactoring",
            ],
            "title": "Design Patterns: Elements of Reusable Object-Oriented Software"
        }]
        resp = api.post('/book', json=body[0])
        self.assertEqual(resp.status_code, 200)
        resp = api.post('/books', json=body[1:])
        self.assertEqual(resp.status_code, 200)
        resp = api.delete('/book?isbn=9780201633610')
        self.assertEqual(resp.status_code, 200)
        # self.assertEqual(resp.status_code, 200)
        pass

if __name__ == '__main__':
    unittest.main()