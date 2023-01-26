from typing import Callable

from flask import redirect, render_template, request

def init_views(app, db_access: dict[str, Callable]): 
    # definición de las acciones a realizar para lanzar cada vista
    # nótese que el código de "/" no pregunta si se ha hecho una petición, así que deberá ejecutarse al inicializar
    # en el caso de los demás tienen sentencias IF para que el código se ejecute solo si haya una petición
    @app.route("/", methods=["GET", "POST"])
    def index():
    	# invoca a la clase contact que está implementada en models.py con el método "list"
    	# y luego lanza la vista "index.html"
        list_gundams = db_access["list"] 
        gundams = list_gundams() # para mostrar al inicio los contactos que ya están en la BD
        return render_template("index.html", gundams=gundams)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        if request.method == "GET":
            return render_template("create.html")

        if request.method == "POST":
            create_gundam = db_access["create"]
            create_gundam(
                name=request.form["name"],
                series=request.form["series"],
                height=int(request.form["height"]),
                manufacturer=request.form["manufacturer"],
                imageUrl=request.form["imageUrl"],
                price=request.form["price"],
                release=request.form["release"],
            )
            return redirect("/")

    @app.route("/update/<int:uid>", methods=["GET", "POST"])
    def update(uid: int):
        if request.method == "GET":
            read_gundam = db_access["read"]
            gundam = read_gundam(uid)
            return render_template("update.html", gundam=gundam)

        if request.method == "POST":
            update_gundam = db_access["update"]
            update_gundam(
                uid=uid,
                name=request.form["name"],
                series=request.form["series"],
                height=int(request.form["height"]),
                manufacturer=request.form["manufacturer"],
                imageUrl=request.form["imageUrl"],
                price=request.form["price"],
                release=request.form["release"],
            )
            return redirect("/")

    @app.route("/delete/<int:uid>", methods=["GET", "POST"])
    def delete(uid: int):
        if request.method == "GET":
            read_gundam = db_access["read"]
            gundam = read_gundam(uid)
            return render_template("delete.html", gundam=gundam)

        if request.method == "POST":
            delete_gundam = db_access["delete"]
            delete_gundam(
                uid=uid,
            )
            return redirect("/")
