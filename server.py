import imp
from flask import Flask, request, json
from sqlite3 import Connection as sqlite3Connectl
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy




#app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlitedb.file"
app.config['SQL_TRACK_MODIFICATION'] = 0



#models
class User(db.model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address= db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship('BlogPost')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name
