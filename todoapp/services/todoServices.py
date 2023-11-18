from todoapp.repository.data import getAllTodo,save,get_by_id,delete
from todoapp.models.todo import Todo,TodoStatus
from todoapp.models.user import Users


def getAll():
    return getAllTodo()

def save_todo(title,descrition,target_date,owner):
    save(Todo(title=title,description=descrition,status=TodoStatus.PENDING,owner=owner,target_date=target_date))

def updater_status(id,status):
    todo1=get_by_id(id)
    if(todo1 is None):
        return None
    new_status = TodoStatus(status)
    todo1.set_status(new_status)
    save(todo1)

def update_todo(todo_id,title,description,target_date):
    todo=get_by_id(todo_id)
    if(todo is None):
        return None
    todo.title=title
    todo.descrition=description
    todo.target_date=target_date
    print(todo)
    save(todo)


def delete_todo(id):
    todo=get_by_id(id)
    if(todo is None):
        return None
    delete(todo)

def register_user_service(name,email,password):
    user=Users()
    user.name=name
    user.email=email
    user.set_password(password)
    save(user)

def get_verified_user(email,password):
    user=Users.query.filter_by(email=email).first()
    if(user and user.check_password(password)):
        return user
    return None


