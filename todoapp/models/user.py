# user.py
from todoapp import login_manager,db,bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=100), nullable=False)
    email = db.Column(db.String(length=30), nullable=False,unique=True)
    password=db.Column(db.String(length=60), nullable=False)
    todos = db.relationship('Todo', backref='users', lazy=True)

    def set_password(self,password):
        self.password=bcrypt.generate_password_hash(password).decode("utf-8")
    def get_password(self):
        return self.password
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email
        }
    def all_todos(self):
        return [ todo.serialize() for todo in self.todos]