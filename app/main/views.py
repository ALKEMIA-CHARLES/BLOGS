from flask import (render_template, request, redirect, url_for, abort)
from . import main
from .forms import AddBlog, DelBlog, CommentsForm, UpdateBlog, HomeCommentsForm
from ..models import User, Blogpost, Comments, HomeComments
from flask_login import login_required, current_user
from .. import db


@main.route("/")
def index():

    blogposts = Blogpost.query.filter_by().all()

    return render_template('home.html', blogposts=blogposts)


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
            blog_title=title, post_blog_section=blogpost, user_id=current_user.id)
        db.session.add(new_blogpost)
        db.session.commit()

        return redirect(url_for('main.blogs_list'))

    return render_template('add.html', form=form)


@main.route("/delete/<blog_id>", methods=["GET", "POST"])
@login_required
def del_blog(blog_id):

    blog = Blogpost.query.filter_by(id=blog_id).first()
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.blogs_list'))


@main.route("/deletecomment/<int:blog_id>/<int:comments_id>", methods=["GET", "POST"])
@login_required
def del_comment(blog_id, comments_id):

    comments = Comments.query.filter_by(id=comments_id).first()
    db.session.delete(comments)
    db.session.commit()

    return redirect(url_for('main.comments', blogpost_id=blog_id))


@main.route('/blogs')
@login_required
def blogs_list():

    blogposts = Blogpost.query.filter_by(user_id=current_user.id)[::-1]
    return render_template('blogs.html', blogposts=blogposts)


@main.route("/comments/<int:blogpost_id>", methods=['GET', 'POST'])
def comments(blogpost_id):

    form = CommentsForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comments_section=comment,
                               user_id=current_user.id, blogpost_id=blogpost_id)
        db.session.add(new_comment)
        db.session.commit()

    all_comments = Comments.query.filter_by(blogpost_id=blogpost_id).all()
    title = 'blogpost'
    return render_template("comments.html", all_comments=all_comments, title=title, form=form, blogpost_id=blogpost_id)


@main.route("/viewblogs/<int:blogpost_id>")
def viewblogs(blogpost_id):
    blog = Blogpost.query.filter_by(id=blogpost_id).first()
    return render_template("singlepost.html", blog=blog)


@main.route("/editblogs/<int:blogpost_id>", methods=['GET', 'POST'])
def editblogs(blogpost_id):
    blog = Blogpost.query.filter_by(id=blogpost_id).first()
    form = UpdateBlog()

    if form.validate_on_submit():
        blog.blog_title = form.title.data
        blog.post_blog_section = form.editblog.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.viewblogs', blogpost_id=blog.id))

    all_edits = Blogpost.query.filter_by(id=blogpost_id).first()
    return render_template("editblogs.html", blog=blog, form=form)


# @main.route("/homecomments/<int:homecomments_id>", methods=['GET', 'POST'])
# def homecomments(homecomments_id):
#     comment = HomeComments.query.filter_by(id=homecomments_id).all()
#     form = HomeCommentsForm()

#     if form.validate_on_submit():
#         comment.home_comments_title = form.title.data
#         comment.home_comments_section = form.homecomment.data
#         db.session.add(comment)
#         db.session.commit()

#         return redirect(url_for('main.index', homecomments_id=comment.id))
#         all_home_comments = HomeComments.query.filter_by(
#             id=homecomments_id).all()

#         return render_template("home.html", comment=comment, form=form)
