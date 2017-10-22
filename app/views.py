from app import app
from flask import render_template,request,redirect,url_for
from models import Todo
from forms import TodoForm
from datetime import datetime
from . import db


@app.route('/',methods=['GET','POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
        content = form.content.data
        todo = Todo(content=content,time=datetime.now())
        db.session.add(todo)
        return redirect(url_for('index'))
    todos = Todo.query.order_by(Todo.time.desc()).all()
    return render_template("index.html",todos=todos,form=form)


# @app.route('/add', methods=['POST',])
# def add():
#     form = TodoForm()
#     if form.validate_on_submit():
#         content = form.content.data
#         todo = Todo(content=content,time=datetime.now())
#         db.session.add(todo)
#     todos = Todo.query.order_by(Todo.time.desc()).all()
#     return render_template("index.html",todos=todos,form=form)

@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = TodoForm()
    todo = Todo.query.get_or_404(todo_id)
    todo.status = 1
    db.session.add(todo)
    todos = Todo.query.order_by(Todo.time.desc()).all()
    return render_template("index.html",todos=todos,form=form)


@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = TodoForm()
    todo = Todo.query.get_or_404(todo_id)
    todo.status = 0
    db.session.add(todo)
    todos = Todo.query.order_by(Todo.time.desc()).all()
    return render_template("index.html",todos=todos,form=form)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    todos = Todo.query.order_by(Todo.time.desc()).all()
    return render_template("index.html",todos=todos,form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')