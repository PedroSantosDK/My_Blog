from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r"blog/My_Secrets/secrets.env")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
lm = LoginManager(app)
lm.login_view = "login"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Atlas_Database/atlas_website.db"
db = SQLAlchemy()
db.init_app(app)

from routes import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()