from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author

