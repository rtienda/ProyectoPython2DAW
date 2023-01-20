from typing import Callable
from flask import render_template

def init_views(app, db_access:dict[str,Callable]):
    @app.route("/", methods=["GET","POST"])
    def index():
        return render_template("index.html")
    @app.route("/create",methods=["GET", "POST"])
    def create():
        return render_template("create.html")
    @app.route("/update/<int:uid>",methods=["GET","POST"])
    def update(uid: int):
        return render_template("update.html")
    @app.route("/delete/<int:uid>",methods=["GET","POST"])
    def delete(uid:int):
        return render_template("delete.html")