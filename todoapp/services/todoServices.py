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

def update_todo(json_todo):
    todo=get_by_id(json_todo.get('id'))
    if(todo is None):
        return None
    todo.title=json_todo.get('title')
    todo.descrition=json_todo.get('descrition')
    todo.status=json_todo.get('status')
    save_todo(todo=todo)


def delete_todo(id):
    todo=get_by_id(id)
    if(todo is None):
        return None
    delete(todo)

