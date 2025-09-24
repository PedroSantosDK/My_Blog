from __init__ import app, db, lm
from flask_login import login_user, login_required, logout_user
from flask import render_template, request, redirect, url_for
from models import User, Post
from datetime import datetime

@lm.user_loader
def user_loader(id):
    global actual_user_id
    actual_user_id = id
    usuario_id = db.session.query(User).filter_by(id=actual_user_id).first()
    return usuario_id

@app.route("/")
def homepage():
    postagens = []
    times = []
    result = db.session.query(Post.post_content).all()
    time = db.session.query(Post.time).all()
    for i in result:
        postagens.append(i[0])

    for t in time:
        times.append(t[0])

    post_time = list(zip(postagens, times))

    return render_template("index.html", post_time=post_time)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form.get("username")
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("senha")
        if name == "":
            name = None
        
        new_user = User(username=username, real_name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
            
        return redirect(url_for("homepage"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("senha")

        user = db.session.query(User).filter_by(email=email, password=password).first()
        print(user)
        if not user:
            return "nome ou senha incorretos"
        else:
            login_user(user)
            return redirect(url_for("homepage"))

@app.route("/rec_password")
def rec_password():
    return render_template("rec_password.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/send-post", methods=["GET", "POST"])
@login_required
def post():
    if request.method == "POST":
        msg = request.form.get("postagem")

        now_hour = str(datetime.now())
        now_hour = now_hour[:-10:]
        new_post = Post(post_id=actual_user_id, post_content=msg, time=now_hour)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    
    if request.method == "GET":
        return render_template("post_page.html")