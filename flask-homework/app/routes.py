from random import randint, choice
import re
from flask import Flask, abort, render_template, request,redirect
from logging.config import dictConfig
from datetime import datetime


app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


@app.route('/hello')
def hello_world():
    app.logger.info(f'Successful Request on /hello on: {datetime.now()}')
    return '<h1 style="color: blue">Hello, world!</h1>'

@app.route('/users')
def get_users():
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isabella", "Jack",
                   "Katherine", "Liam", "Mia", "Nathan", "Olivia", "Parker", "Quinn", "Ryan", "Samantha", "Thomas",
                   "Uma", "Victoria", "William", "Xander", "Yvonne", "Zachary"]
    context = []
    for i in range(randint(1, 30)):
        chosen_name = choice(names)
        context.append(chosen_name)
    return render_template('users.html', items=context)

@app.route('/books')
def get_books():
    book_titles = ["To Kill a Mockingbird", "1984", "Brave New World", "The Great Gatsby", "The Catcher in the Rye",
                   "One Hundred Years of Solitude", "Pride and Prejudice", "The Lord of the Rings", "Animal Farm",
                   "The Da Vinci Code", "The Hitchhiker's Guide to the Galaxy", "The Hunger Games", "The Giver",
                   "The Picture of Dorian Gray", "The Alchemist", "The Girl with the Dragon Tattoo",
                   "The Adventures of Huckleberry Finn", "The Adventures of Tom Sawyer", "The Bell Jar",
                   "Wuthering Heights", "The Hobbit", "The Little Prince", "The Lovely Bones", "The Outsiders",
                   "The Perks of Being a Wallflower", "The Road", "The Stand", "The Sun Also Rises",
                   "The Time Traveler's Wife", "The War of the Worlds"]

    context = []
    for i in range(randint(1, 30)):
        chosen_name = choice(book_titles)
        context.append(chosen_name)
    return render_template('books.html', items=context)

@app.route('/users/<int:user_id>')
def get_users_id(user_id):
    if user_id % 2 == 0:
        return f'<h1 style="color: black">{user_id}</h1>'
    else:
        return abort(404)

@app.route('/books/<string:title>')
def get_books_title(title):
    title = title.capitalize()
    return f'<h1 style="color: black">{title}</h1>'

@app.route('/params')
def get_params():
    context = request.args.to_dict().items()
    return render_template('params.html', items=context)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) < 5:
            return abort(400, 'Логін менше 5 символів')
        elif not re.search(r"^(?=.*\d)(?=.*[A-Z]).{8,}$", password):
            return abort(400, 'Незадовільний пароль.')
        else:
            return redirect("/users", code=302)
    else:
        return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500





















if __name__ == '__main__':
    app.run()
