from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    subjects = db.relationship('Subject', backref='day')


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

    # day = db.relationship('Day')

    # day = db.relationship('Day', backref='object')
