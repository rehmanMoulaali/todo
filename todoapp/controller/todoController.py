from todoapp import app1 as app
from todoapp.services.todoServices import getAll ,save_todo, updater_status,update_todo,delete_todo,register_user_service,get_verified_user
from flask import request,render_template,url_for,redirect,flash
from flask_login import login_user, logout_user, login_required,current_user
from todoapp.services.table_services import *


@app.route('/')
@app.route('/tables')
@login_required
def render_tables():
    return render_template('todo_tables.html',tables=current_user.all_todo_tables())
@app.route('/table',methods=['GET','POST'])
def post_table():
    save_table(request.form.get('title'),request.form.get('description'),current_user)
    return redirect(url_for('render_tables'))

@app.route('/table/delete/<int:id>',methods=['POST'])
def delete_table_api(id):
    delete_table(id)
    return redirect(url_for('render_tables'))

@app.route('/table/update',methods=['POST'])
def update_table_api():
    table_id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    update_table(table_id,title,description)
    return redirect(url_for('render_tables'))

@app.route('/table/share',methods=['POST'])
def add_user_to_table():
    table_id = request.form.get('id')
    email = request.form.get('email')
    add_user(table_id,email)
    return redirect(url_for('render_tables'))

@app.route('/todos/<int:id>')
@login_required
def renderindex(id):
    todos=getAll()
    return render_template('index.html',todos=get_by_id(id).get_todos())


# @app.route('/todos')
# @login_required
# def get_all():
#     return current_user.all_todos()

@app.route('/todo',methods=['GET','POST'])
def post_todo():
    save_todo(request.form.get('title'),request.form.get('description'),request.form.get('target_date'),request.form.get('table_id'))
    return redirect(url_for('renderindex',id=request.form.get('table_id')))

@app.route('/todo/status/<int:id>',methods=['PUT','POST'])
@login_required
def update_status(id):
    new_status_str =  request.form['status']
    table_id=updater_status(id,new_status_str)
    return redirect(url_for('renderindex',id=table_id))

@app.route('/todo/update',methods=['POST','PUT'])
@login_required
def update_todo_api():
    todo_id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    target_date=request.form.get('target_date')
    table_id=update_todo(todo_id,title,description,target_date)
    return redirect(url_for('renderindex',id=table_id))

@app.route('/todo/<int:id>', methods=['POST', 'DELETE'])
@login_required
def delete_todo_api(id):
    table_id=delete_todo(id)
    return redirect(url_for('renderindex',id=table_id))

@app.route('/register',methods=['POST'])
def register_user():
    
    name = request.form.get('name')
    email = request.form['email']
    password = request.form['password']
    c_password = request.form['C_password']
    if(password!=c_password):
        return {"message":"please ensure password","status":False}
    register_user_service(name,email,password)
    return {"message":"register sucessfull please login","status":True}

@app.route('/register')
def register_page():
    return render_template('login-signup.html')

@app.route('/login',methods=['GET'])
def login_page():
    return render_template('login-signup.html')

@app.route('/login',methods=['POST'])
def user_login():
    email = request.form['email']
    password = request.form['password']
    user = get_verified_user(email,password)
    if(not user):
        return {"status":False}
    login_user(user)
    return {"status":True}

# need to make page
@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for("login_page"))

    


   