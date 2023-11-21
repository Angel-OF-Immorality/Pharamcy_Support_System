from flask import Flask,Request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config["SECRET_KEY"] = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123@localhost/pharmacy_records'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db =SQLAlchemy(app)

import routes,forms,models

with app.app_context():
    db.create_all()
    
  