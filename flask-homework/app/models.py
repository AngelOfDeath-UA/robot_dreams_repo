from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80))
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String)

    # Определение отношения один-ко-многим с моделью Purchase
    purchases = db.relationship('Purchase', backref='user', lazy=True)
    def __repr__(self):
        return f'User {self.first_name}'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable=False)

    # Определение отношения один-ко-многим с моделью Purchase
    purchases = db.relationship('Purchase', backref='book', lazy=True)
    def __repr__(self):
        return f'Book {self.author} - {self.title}'


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)  # Использование функции datetime.utcnow() в качестве значения по умолчанию

    def __repr__(self):
        return f'Purchase {self.id}'
