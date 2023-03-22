from flask import Flask, redirect
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


# I used redirect to avoid typing /hello every time
@app.route('/')
def index():
    return redirect("/hello", code=302)


if __name__ == '__main__':
    app.run()
