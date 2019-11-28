from . import db
from werkzeug.security import (generate_password_hash, check_password_hash)
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class Blogpost(db.Model):

    __tablename__ = 'blogpost'
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String)
    post_blog_section = db.Column(db.Text)
    username = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship(
        "Comments", backref="post_comments", lazy="dynamic")

    def __init__(self, post_blog_section, blog_title):
        self.post_blog_section = post_blog_section
        self.blog_title = blog_title

    def __repr__(self):
        return f"There is a pretty cool blog here !:{self.post_blog_section}"


class Comments(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comments_section = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blogpost_id = db.Column(db.Integer, db.ForeignKey('blogpost.id'))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    blog_post = db.relationship(
        "Blogpost", backref="user_blogs", lazy="dynamic")
    comments = db.relationship(
        "Comments", backref="user_comments", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'
