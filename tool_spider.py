from flask import Flask
from flask_mail import Mail

from dysfz.spider import get_movie_list
from plugins import mail

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dysfz/')
def dysfz():
    try:
        get_movie_list()
        return "成功"
    except:
        return "出现异常"


def create_app():
    app.config.from_pyfile('config.py')
    mail.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()

