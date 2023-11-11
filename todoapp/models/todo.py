from todoapp import db
from enum import Enum

class TodoStatus(Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'inprogress'
    DONE = 'done'
    DELAYED = 'delayed'

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=500), nullable=False)
    status = db.Column(db.Enum(TodoStatus), nullable=False)

    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.set_status(status)

    def set_status(self, status):
        self.status = status

