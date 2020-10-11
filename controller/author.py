from flask import request, jsonify, abort
from flask.views import MethodView

import controller.utils as util


class APIWrapper(MethodView):
    def setup(self):
        if request.method == 'PUT' or request.method == 'POST':
            if 'Content-Type' not in request.headers or request.headers['Content-Type'] != 'application/json':
                abort(415)
        self.params = util.check_attribute(request.args.to_dict())
        self.data = request.get_json()

    def teardown(self):
        pass

    def dispatch_request(self, *args, **kwargs):
        self.setup()
        response = super(APIWrapper, self).dispatch_request(*args, **kwargs)
        self.teardown()
        return util.JSONEncoder().encode(response)


class AuthorsAPI(APIWrapper):
    methods = ['GET', 'PUT', 'POST']

    def get(self):
        return util.get_authors(self.params)

    def put(self):
        util.update_author(self.params, self.data)
    
    def post(self):
        util.create_authors(self.data)


class AuthorAPI(APIWrapper):
    methods = ['POST', 'DELETE']

    def post(self):
        util.create_author(self.data)

    def delete(self):
        util.delete_author(self.params)