from todoapp import app1 as app
from todoapp.services.todoServices import getAll ,save_todo, updater_status,update_todo,delete_todo,register_user_service,get_verified_user
from flask import request,render_template,url_for,redirect,flash
from flask_login import login_user, logout_user, login_required,current_user


@app.route('/')
@login_required
def renderindex():
    todos=getAll()
    return render_template('index.html',todos=current_user.all_todos())

@app.route('/hello')
def hello():
    return "hello world"

@app.route('/todos')
@login_required
def get_all():
    return getAll()

@app.route('/todo',methods=['GET','POST'])
def post_todo():
    save_todo(request.form.get('title'),request.form.get('description'),request.form.get('target_date'),current_user.id)
    return redirect(url_for('renderindex'))

@app.route('/todo/status/<int:id>',methods=['PUT','POST'])
@login_required
def update_status(id):
    new_status_str =  request.form['status']
    updater_status(id,new_status_str)
    return redirect(url_for('renderindex'))

@app.route('/todo/update',methods=['POST','PUT'])
@login_required
def update_todo_api():
    todo_id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    target_date=request.form.get('target_date')
    update_todo(todo_id,title,description,target_date)
    return redirect(url_for('renderindex'))

@app.route('/todo/<int:id>', methods=['POST', 'DELETE'])
@login_required
def delete_todo_api(id):
    delete_todo(id)
    return redirect(url_for('renderindex'))

@app.route('/register',methods=['POST'])
def register_user():
    
    name = request.form.get('name')
    email = request.form['email']
    password = request.form['password']
    c_password = request.form['C_password']
    
    if(password!=c_password):
        flash("password mismached",'success')
        return {"message":"please ensure password","status":False}
    register_user_service(name,email,password)
    flash("User registered successfully. Please log in.", 'success')
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


@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login_page"))

    


   