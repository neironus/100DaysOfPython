from flask import Flask, render_template, request, url_for
from collections import namedtuple

app = Flask(__name__)

articleTupple = namedtuple('Article', 'title text')
articles = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/articles', methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        articles.append(
            articleTupple(request.form['title'], request.form['text'])
        )

    return render_template('articles.html', articles=articles)


@app.route('/articles/create', methods=['GET'])
def create_article():
    return render_template('create_article.html')


if __name__ == '__main__':
    app.run()
