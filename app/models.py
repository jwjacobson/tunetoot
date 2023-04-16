from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
from hashlib import md5

"""
join table syntax taken from https://hackmd.io/@jpshafto/H1VbmP3yO
"""

repertoire = db.Table("repertoire",
db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
db.Column("tune_id", db.Integer, db.ForeignKey("tunes.id"), primary_key=True))


class Tune(db.Model):
    __tablename__ = "tunes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    composer = db.Column(db.String(64))
    key = db.Column(db.String(3))
    other_key = db.Column(db.String(12))
    song_form = db.Column(db.String(20))
    style = db.Column(db.String(20))
    meter = db.Column(db.SmallInteger)
    year = db.Column(db.SmallInteger)
    decade = db.Column(db.String(5))
    knowledge = db.Column(db.String(10))
    started_learning = db.Column(db.DateTime)
    last_played = db.Column(db.DateTime)
    users = db.relationship("User", secondary=repertoire, back_populates="tunes")

    def __repr__(self):
        return f'<Tune {self.id}|{self.title}>'

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tunes = db.relationship("Tune", secondary=repertoire, back_populates="users")

    def __repr__(self):
        return f'<User {self.id}|{self.username}>'
    