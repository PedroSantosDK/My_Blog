from __init__ import db
from sqlalchemy import *
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(45), nullable=False, unique=True)
    real_name = Column(String(50), nullable=True, unique=False)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(16), nullable=False, unique=True)

class Post(UserMixin, db.Model):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, unique=True)
    post_id = Column(Integer, unique=False, nullable=False)
    post_content = Column(Text(200), nullable=False, unique=False)
    time = Column(Text, nullable=False, unique=False)