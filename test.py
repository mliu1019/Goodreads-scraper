import unittest

class Testing(unittest.TestCase):
    def test_databaseconnection(self):
        import pymongo as pm
        from database import mongoclient

        raised = False
        try:
            cli = mongoclient()
            cli.list_collection_names()
        except Exception as e:
            print(e)
            raised = True

        self.assertFalse(raised, "Shoud not raise.")

    def test_scrapebook(self):
        from book import create_book
        book = create_book("https://www.goodreads.com/book/show/3735293-clean-code")
        self.assertEqual(book.book_url, "https://www.goodreads.com/book/show/3735293-clean-code")
        self.assertEqual(book.author, "Robert C. Martin")
        self.assertEqual(book.title, "Clean Code: A Handbook of Agile Software Craftsmanship")


if __name__ == '__main__':
    unittest.main()