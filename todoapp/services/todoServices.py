from todoapp.repository.data import getAllTodo,save_todo,get_by_id,delete
from todoapp.models.todo import Todo,TodoStatus



def getAll():
    return getAllTodo()

def save(title,descrition):
    save_todo(Todo(title=title,description=descrition,status=TodoStatus.PENDING))

def updater_status(id,status):
    todo1=get_by_id(id)
    if(todo1 is None):
        return None
    todo1.set_status(status)
    save_todo(todo=todo1)

def update_todo(todo_id,title,description):
    todo=get_by_id(todo_id)
    if(todo is None):
        return None
    todo.title=title
    todo.descrition=description
    print(todo)
    save_todo(todo=todo)


def delete_todo(id):
    todo=get_by_id(id)
    if(todo is None):
        return None
    delete(todo)

