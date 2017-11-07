# -*- coding: utf-8 -*-
from . import app,login_manager
from flask import render_template,request,redirect,url_for,flash
from models import Todo,User,Tag
from forms import TodoForm,LoginForm,TagForm
from datetime import datetime
from . import db
from flask_login import login_user, logout_user, login_required,\
    current_user

@app.route('/',methods=['GET','POST'])
def index():
    form = TodoForm()

    if form.validate_on_submit():
        todo_content = form.todo_content.data
        thistag=Tag.query.filter_by(tag_content=form.select_tag.data).first()
        # if thistag=='':
        #     flash("you should add a tag first")
        #     return redirect('index')
        todo = Todo(todo_content=todo_content,tag=thistag)
        db.session.add(todo)
        return redirect(url_for('index'))

    alltodos = Todo.query.order_by(Todo.time.desc()).all()
    return render_template("index.html",alltodos=alltodos,form=form)

@app.route('/addtag',methods=['GET','POST'])
def addtag():
    form = TagForm()
    if form.validate_on_submit():
        tag_content = form.tag_content.data
        tag = Tag(tag_content=tag_content)
        form_todo=TodoForm()
        form_todo.select_tag.choices+=[(tag.tag_content,tag.tag_content)]
        db.session.add(tag)
        return redirect(url_for('addtag'))
    alltags = Tag.query.all()
    return render_template("addtag.html", alltags=alltags,form=form)

@app.route('/delete_tag/<string:tag_id>')
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    form_todo=TodoForm()
    form_todo.select_tag.choices.remove((tag.tag_content,tag.tag_content))
    for todo_todelete in tag.todos.all():
        db.session.delete(todo_todelete)
    db.session.delete(tag)

    return redirect(url_for('addtag'))


@app.route('/done/<string:todo_id>')
def done(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.status = 1
    db.session.add(todo)
    return redirect(url_for('index'))

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.status = 0
    db.session.add(todo)
    return redirect(url_for('index'))

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_a=User.query.filter_by(username=form.username.data).first()
        if user_a is not None and user_a.verify_password(form.password.data):
            flash('success')
            login_user(user_a)
            return redirect(url_for('index'))
        flash('Invalid username or password.')
    return render_template("login.html",form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out')
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    return render_template('profile.html')



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#
