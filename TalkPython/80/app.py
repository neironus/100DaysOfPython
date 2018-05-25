from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_PATH']
db.init_app(app)

# Blueprints
from days.views import days
app.register_blueprint(days)


@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run()


if __name__ == '__main__':
    main()
