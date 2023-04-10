from app import app, db
from werkzeug.security import generate_password_hash
import re
from flask import abort, render_template, request, redirect, session, url_for
from app.models import User, Book, Purchase


def save_last_endpoint():
    """Save last endpoint for redirect after login."""

    endpoint = request.path
    session['last_endpoint'] = endpoint


@app.route('/users')
def get_users():
    save_last_endpoint()

    if session.get('username') is None:
        return redirect(url_for('login'))

    query = db.select(User)
    users = db.session.scalars(query)

    context = []

    for user in users:
        context.append(user)

    return render_template('users.html', users=context)


@app.route('/books')
def get_books():
    save_last_endpoint()

    if session.get('username') is None:
        return redirect(url_for('login'))

    query = db.select(Book)
    books = db.session.scalars(query)

    context = []

    for book in books:
        context.append(book)

    return render_template('books.html', books=context)


@app.route('/purchases')
def purchases():
    save_last_endpoint()

    if session.get('username') is None:
        return redirect(url_for('login'))

    query = db.select(Purchase, User, Book).join(User).join(Book)
    db_purchases = db.session.scalars(query).all()

    context = []

    for purchase in db_purchases:
        context.append(purchase)

    return render_template('purchases.html', purchases=context)


@app.route('/users/<int:user_id>')
def get_users_id(user_id):
    save_last_endpoint()

    if session.get('username') is None:
        return redirect(url_for('login'))

    query = db.select(User).where(User.id == int(user_id))
    user = db.session.scalars(query).first()

    if user:
        return render_template('users_id.html', user=user)
    else:
        return abort(404)


@app.route('/books/<int:title_id>')
def get_books_title(title_id):
    save_last_endpoint()

    if session.get('username') is None:
        return redirect(url_for('login'))

    query = db.select(Book).where(Book.id == int(title_id))
    book = db.session.scalars(query).first()
    if book:
        return render_template('books_id.html', book=book)
    else:
        return abort(404)


@app.route('/purchases/<int:purchase_id>')
def purchase_id(purchase_id):
    save_last_endpoint()

    if session.get('username') is None:
        return redirect(url_for('login'))

    query = db.select(Purchase, User, Book).join(User).join(Book).where(Book.id == int(purchase_id))
    purchase = db.session.scalars(query).first()
    if purchase:
        return render_template('purchase_id.html', purchase=purchase)
    else:
        return abort(404)


@app.route('/users', methods=['POST'])
def post_users():
    """
    Example JSON Request:
    {
        "first_name": "Test",
        "age": 26,
        "password": "test123"
    }
    """

    save_last_endpoint()
    data = request.get_json()

    user = User(
        first_name=data['first_name'],
        age=data['age'],
        password=generate_password_hash(data['first_name']),
    )
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('get_users'))


@app.route('/books', methods=['POST'])
def post_books():
    """
    Example JSON Request:
    {
        "title": "Test",
        "author": "Test",
        "year": 2019,
        "price": 520
    }
    """

    save_last_endpoint()

    data = request.get_json()

    user = Book(
        title=data['title'],
        author=data['author'],
        year=data['year'],
        price=data['price'],
    )
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('get_users'))


@app.route('/purchases', methods=['POST'])
def post_purchases():
    """
    Example JSON Request:
    {
        "user_id": 1,
        "book_id": 2,

    }
    """

    save_last_endpoint()

    data = request.get_json()

    # check user_id and book_id

    query_user = db.select(User).where(User.id == int(data['user_id']))
    user = db.session.scalars(query_user).first()

    query_book = db.select(Book).where(Book.id == int(data['book_id']))
    book = db.session.scalars(query_book).first()

    if book and user:
        user = Purchase(
            user_id=int(data['user_id']),
            book_id=int(data['book_id'])
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('get_users'))
    else:
        return abort(404)


@app.route('/params')
def get_params():
    save_last_endpoint()

    if session.get('username') is None:
        return redirect(url_for('login'))

    context = request.args.to_dict().items()
    return render_template('params.html', items=context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) < 5:
            return abort(400, 'Логін менше 5 символів')
        elif not re.search(r"^(?=.*\d)(?=.*[A-Z]).{8,}$", password):
            return abort(400, 'Незадовільний пароль.')
        else:
            session['username'] = username
            last_endpoint = session.get('last_endpoint')
            if last_endpoint:
                return redirect(last_endpoint)
            else:
                return redirect('/users')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
