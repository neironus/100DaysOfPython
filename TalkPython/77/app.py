import string
from random import SystemRandom

from flask import Flask, render_template, request, abort, redirect, url_for
from collections import namedtuple

app = Flask(__name__)

articleTupple = namedtuple('Article', 'idx title text')
articles = {}


def random_string(n=20):
    return ''.join(
        SystemRandom().choice(string.ascii_uppercase + string.digits) for
        _ in range(n))


def get_unused_idx(n):
    idx = random_string(n)
    if articles.get(idx):
        return get_unused_idx(n)
    else:
        return idx


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/articles', methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        idx = request.form['id'] if 'id' in request.form else get_unused_idx(20)
        title = request.form['title']
        text = request.form['text']

        articles[idx] = articleTupple(idx, title, text)

    return render_template('articles.html', articles=articles)


@app.route('/articles/create', methods=['GET'])
def create_article():
    return render_template('create_article.html')


@app.route('/articles/edit/<string:article_id>', methods=['GET'])
def edit_article(article_id):
    if articles.get(article_id):
        return render_template(
            'create_article.html', article=articles.get(article_id)
        )
    else:
        abort(404)


@app.route('/articles/remove/<string:article_id>', methods=['GET'])
def remove_article(article_id):

    if articles.get(article_id):
        articles.pop(article_id)
        return redirect(url_for('article'))
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
