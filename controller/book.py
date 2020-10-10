from flask import request, jsonify, abort
from flask.views import MethodView

import controller.utils as util

class APIWrapper(MethodView):
    def setup(self):
        if request.method == 'PUT' or request.method == 'POST':
            if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
                abort(415)
        self.params = util.check_book_attribute(request.args.to_dict())
        self.data = request.get_json()

    def teardown(self):
        pass

    def dispatch_request(self, *args, **kwargs):
        self.setup()
        response = super(APIWrapper, self).dispatch_request(*args, **kwargs)
        self.teardown()
        return util.JSONEncoder().encode(response)

class BooksAPI(APIWrapper):
    methods = ['GET', 'PUT', 'POST']

    def get(self):
        return util.get_books(self.params)

    def put(self):
        util.update_book(self.params, self.data)
    
    def post(self):
        util.create_books(self.data)


class BookAPI(APIWrapper):
    methods = ['POST', 'DELETE']

    def post(self):
        util.create_book(self.data)

    def delete(self):
        util.delete_book(self.params)