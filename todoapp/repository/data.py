from todoapp.models.todo import Todo
from todoapp.models.user import Users
from todoapp import db

def getAllTodo():
    obj_list = Todo.query.all()
    return [ obj.serialize() for obj in obj_list]

def save(data, description=None, target_date=None):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def get_by_id(id):
    return Todo.query.get(id)

def delete(todo):
    db.session.delete(todo)
    db.session.commit()
