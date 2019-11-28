from flask import (render_template, request, redirect, url_for, abort)
from . import main
from .forms import AddBlog, DelBlog, CommentsForm
from ..models import User, Blogpost, Comments
from flask_login import login_required, current_user
from .. import db


@main.route("/")
def index():
    # return redirect(url_for('main.add_blog'))

    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/add", methods=["GET", "POST"])
@login_required
def add_blog():
    form = AddBlog()
    if form.validate_on_submit():
        title = form.title.data
        blogpost = form.blogpost.data

        new_blogpost = Blogpost(
            blog_title=title, post_blog_section=blogpost,)
        db.session.add(new_blogpost)
        db.session.commit()

        return redirect(url_for('main.blogs_list'))

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

        return redirect(url_for('main.blogs_list'))

    return render_template('delete.html', form=form)


@main.route('/blogs')
@login_required
def blogs_list():

    blogposts = Blogpost.query.all()[::-1]
    return render_template('blogs.html', blogposts=blogposts)


@main.route("/comments/<int:blogpost_id>", methods=['GET', 'POST'])
def comments(blogpost_id):

    form = CommentsForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment_section=comment,
                               user_id=current_user.id, blogpost_id=blogpost_id)
        db.session.add(new_comment)
        db.session.commit()

    all_comments = Comments.query.filter_by(blogpost_id=blogpost_id).all()
    title = 'blogpost'
    return render_template("comments.html", all_comments=all_comments, title=title, form=form)
