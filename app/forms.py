# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired, Length
from .models import Tag

# result=Tag.query.all()
# choices=[]
# for i in result:
#     name=i.tag_content
#     choices.append((name,name))

class TodoForm(Form):


    todo_content = StringField('Todo',validators=[DataRequired(),Length(0,64)])
    select_tag=SelectField('select_tag', choices=[('default','')])
    submit = SubmitField('add_todo')
class TagForm(Form):
    tag_content = StringField('Tag',validators=[DataRequired(),Length(0,64)])
    submit = SubmitField('add_tag')

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('password', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('submit')

