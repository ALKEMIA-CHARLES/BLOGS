from flask import (render_template, request, redirect, url_for, abort)
from . import main
from .forms import AddBlog, DelBlog, CommentsForm
from ..models import User, Blogpost, Comments
from flask_login import login_required, current_user
from .. import db, photos


@main.route("/")
def index():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/add", methods=["GET", "POST"])
@login_required
def add_blog():
    form = AddBlog()
    if form.validate_on_submit():

        blogpost = form.blogpost.data

        new_blogpost = Blogpost(post_blog_section=blogpost)
        db.session.add(new_blogpost)
        db.session.commit()

        return redirect(url_for('main.blogs'))

    return render_template('add.html', form=form)


@main.route("/delete", methods=["GET", "POST"])
@login_required
def del_blog():
    form = DelBlog()

    if form.validate_on_submit():

        id = form.id.data
        blog = Blogpost.query.get(id)
        db.session.delete(blog)
        db.session.commit()

        return redirect(url_for('main.blogs'))

    return render_template('delete.html', form=form)
