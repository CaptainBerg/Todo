# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,SubmitField,DateTimeField,IntegerField
from wtforms.validators import Required, Length, Email, Regexp


class TodoForm(Form):
    content = StringField('Todo',validators=[Required(),Length(0,64)])
    submit = SubmitField('add')

