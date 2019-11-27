from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                     SubmitField, SelectField, IntegerField)
from wtforms.validators import Required


class AddBlog(FlaskForm):
    blogpost = StringField(
        "You seem like the type that can express themselves")
    submit = SubmitField('Add Blog')


class DelBlog(FlaskForm):
    id = IntegerField(
        "please enter the ID number of Blog you would like to delete ")
    submit = SubmitField("Remove Pitch")


class CommentsForm(FlaskForm):
    comment = TextAreaField("Don't be shy ! This is a free space...")
    submit = SubmitField("Submit Comment")


class DelComments(FlaskForm):
    id = IntegerField(
        "Please enter the ID number of the comment you would like to delete")
