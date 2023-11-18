from todoapp import db
from enum import Enum
from datetime import datetime
from .user import Users


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
    target_date = db.Column(db.Date, default=None, nullable=True)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __init__(self, title, description, status, owner,target_date=None):
        self.title = title
        self.description = description
        self.set_status(status)
        self.target_date = target_date
        self.owner=owner

    def set_status(self, status):
        self.status = status

    def serialize(self):
        return {
            'id': self.id,
            'name': self.title,
            'description': self.description,
            'target_date':self.target_date,
            'status': self.status
        }
