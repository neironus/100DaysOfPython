from flask_sqlalchemy import SQLAlchemy
from subjects.models import DaySubject

db = SQLAlchemy()


class Day(DaySubject):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
