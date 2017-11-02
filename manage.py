from app import app,db
from app.models import Todo,User,Tag
from flask_script import Manager,Shell
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def save():
    todo = Todo(content="study flask")
    todo.save()

def make_shell_context():
    return dict(app=app, db=db, User=User, Todo=Todo,Tag=Tag)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()