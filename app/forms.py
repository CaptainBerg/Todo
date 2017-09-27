# -*- coding: utf-8 -*-
import datetime
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,SubmitField,DateTimeField,IntegerField
from wtforms.validators import Required, Length, Email, Regexp


class TodoForm(Form):
    content = StringField('content',validators=[Required(),Length(0,64)])
    # wtf-field has default()?
    time = DateTimeField('time',default=datetime.datetime.now())
    status = IntegerField('status',default=0)

