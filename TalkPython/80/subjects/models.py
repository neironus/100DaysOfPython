from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr

db = SQLAlchemy()


class DaySubject(db.Model):
    __abstract__ = True

    @declared_attr
    def subjects(self):
        return db.relationship('Subject', backref='day', lazy=True)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

    # day = db.relationship('Day')

    # day = db.relationship('Day', backref='object')
