from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    subjects = db.relationship('Subject', backref='day')


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

