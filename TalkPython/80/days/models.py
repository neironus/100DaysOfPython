from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Day(db.Model):
    __tablename__ = 'days'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
