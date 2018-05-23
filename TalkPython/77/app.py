from flask import Flask, render_template, request, abort, redirect, url_for
from collections import namedtuple

app = Flask(__name__)

articleTupple = namedtuple('Article', 'id title text')
articles = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/articles', methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        if request.form['id']:
            idx = int(request.form['id'])-1
            print(idx)
            articles[idx] = articles[idx]._replace(title=title)
            articles[idx] = articles[idx]._replace(text=text)
        else:
            articles.append(
                articleTupple(
                    len(articles)+1, title, text
                )
            )

    return render_template('articles.html', articles=articles)


@app.route('/articles/create', methods=['GET'])
def create_article():
    return render_template('create_article.html')


@app.route('/articles/edit/<int:article_id>', methods=['GET'])
def edit_article(article_id):
    try:
        article = articles[article_id-1]
        return render_template('create_article.html', article=article)
    except Exception:
        abort(404)


@app.route('/articles/remove/<int:article_id>', methods=['GET'])
def remove_article(article_id):
    try:
        article = articles[article_id-1]
        articles.remove(article)

        return redirect(url_for('article'))
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run()
