# -*- coding: utf-8 -*-
from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin,AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_content = db.Column(db.String(64))
    time = db.Column(db.DateTime(), default=datetime.now)
    status =  db.Column(db.Boolean, default=False)
    tag_id=db.Column(db.Integer,db.ForeignKey('tag.id'),default=1)


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_content = db.Column(db.String(64), unique=True, index=True)
    todos=db.relationship('Todo',backref='tag',lazy='dynamic')

