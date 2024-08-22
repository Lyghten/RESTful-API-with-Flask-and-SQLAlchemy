from flask_restful import Resource, Api, reqparse

api = Api(app)

class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        return BookSchema().dump(book), 200

    def post(self):
        data = request.get_json()
        new_book = Book(title=data['title'], author_id=data['author_id'])
        db.session.add(new_book)
        db.session.commit()
        return BookSchema().dump(new_book), 201

    def delete(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Book deleted'}, 200

api.add_resource(BookResource, '/books/<int:book_id>')

class AuthorResource(Resource):
    def get(self, author_id):
        author = Author.query.get(author_id)
        if not author:
            return {'message': 'Author not found'}, 404
        return AuthorSchema().dump(author), 200
