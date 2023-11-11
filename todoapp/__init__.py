from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app1=Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI']='mysql://arjunagi123:abdul1234@localhost:3306/todo'
db = SQLAlchemy(app1)
from todoapp.controller import todoController