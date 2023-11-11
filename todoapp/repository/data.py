from todoapp.models.todo import Todo
from todoapp import db
from todoapp import app1 as app

def getAllTodo():
    todo_list = Todo.query.all()
    return [ {
        'id': todo.id,
        'name': todo.title,
        'description': todo.description,
        'status': todo.status
    } for todo in todo_list]

def save_todo(todo):
    db.session.add(todo)
    db.session.commit()

def get_by_id(id):
    return Todo.query.get(id)

def delete(todo):
    db.session.delete(todo)
    db.session.commit()
