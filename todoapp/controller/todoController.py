from todoapp import app1 as app
from todoapp.services.todoServices import getAll ,save, updater_status,update_todo,delete_todo
from flask import request,render_template,url_for,redirect
from todoapp.models.todo import TodoStatus


@app.route('/')
def renderindex():
    todos=getAll()
    print(todos)
    return render_template('index.html',todos=todos)

@app.route('/hello')
def hello():
    return "hello world"

@app.route('/todos')
def get_all():
    return getAll()

@app.route('/todo',methods=['GET','POST'])
def post_todo():
    save(request.form.get('title'),request.form.get('description'))
    return redirect(url_for('renderindex'))

@app.route('/todo/status/<int:id>',methods=['PUT','POST'])
def update_status(id):
    new_status_str =  request.form['status']
    
    try:
        new_status = TodoStatus(new_status_str)
    except ValueError:
        return "Invalid status value"
    updater_status(id,new_status)
    return redirect(url_for('renderindex'))

@app.route('/todo',methods=['PUT'])
def update_todo_api():
    update_todo(request.get_json())
    return "added sucessfully"

@app.route('/todo/<int:id>', methods=['POST', 'DELETE'])
def delete_todo_api(id):
    delete_todo(id)
    return redirect(url_for('renderindex'))
   