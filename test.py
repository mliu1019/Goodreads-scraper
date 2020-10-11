import unittest

class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        from dotenv import load_dotenv
        load_dotenv('config.env')
        from app import app
    
        self._app = app
        self._header = {
            'Content-Type': 'application/json'
        }


    def test_serverup(self):
        api = self._app.test_client(self)
        resp = api.get('/', content_type='html/text')
        self.assertEqual(resp.status_code, 200)
        

    def test_book_create(self):
        api = self._app.test_client(self)
        book = {
            'title': 'New Book',
            'author': 'Miranda Liu',
            'isbn': '123456'
        }
        resp = api.post('/api/book', json=book, headers=self._header)
        self.assertEqual(resp.status_code, 200)


    def test_book_get(self):
        api = self._app.test_client(self)
        resp = api.get('/api/book?isbn=654321')
        self.assertEqual(resp.status_code, 404)


    def test_book_delete(self):
        api = self._app.test_client(self)
        resp = api.delete('/api/book?isbn=123456')
        self.assertEqual(resp.status_code, 200)

    
    def test_author_create(self):
        api = self._app.test_client(self)
        author = {
            'name': 'Miranda Liu',
            'rating': '5.0'
        }
        resp = api.post('/api/author', json=author, headers=self._header)
        self.assertEqual(resp.status_code, 200)


    def test_author_get(self):
        api = self._app.test_client(self)
        resp = api.get('/api/author?name=John Doe')
        self.assertEqual(resp.status_code, 404)


    def test_author_delete(self):
        api = self._app.test_client(self)
        resp = api.delete('/api/author?rating=5.0')
        self.assertEqual(resp.status_code, 200)

    
    def test_put_post_200(self):
        api = self._app.test_client(self)
        resp = api.put('/api/books?book_id=4098', json={}, headers=self._header)
        self.assertEqual(resp.status_code, 200)
        resp = api.delete('/api/book?book_id=4098')
        self.assertEqual(resp.status_code, 200)


    def test_get_404(self):
        api = self._app.test_client(self)
        resp = api.get('/api/author?rating=5.1')
        self.assertEqual(resp.status_code, 404)


    def test_put_post_415(self):
        api = self._app.test_client(self)
        resp = api.put('/api/books?book_id=4099')
        self.assertEqual(resp.status_code, 415)



if __name__ == '__main__':
    unittest.main()