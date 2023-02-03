from typing import Callable

from flask import redirect, render_template, request

def init_views(app, db_access: dict[str, Callable]): 
    # definición de las acciones a realizar para lanzar cada vista
    # nótese que el código de "/" no pregunta si se ha hecho una petición, así que deberá ejecutarse al inicializar
    # en el caso de los demás tienen sentencias IF para que el código se ejecute solo si haya una petición
    @app.route("/", methods=["GET", "POST"])
    @app.route("/index.html", methods=["GET", "POST"])
    def index():
        return render_template("index.html")
    @app.route("/gundams.html", methods=["GET", "POST"])
    def gundams():
    	# invoca a la clase contact que está implementada en models.py con el método "list"
    	# y luego lanza la vista "index.html"
        list_gundams = db_access["list_gundams"] 
        gundams = list_gundams() # para mostrar al inicio los contactos que ya están en la BD
        return render_template("gundams.html", gundams=gundams)
    

   
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


        
    @app.route("/usuarios.html", methods=["GET", "POST"])
    def Usuarios():
    	# invoca a la clase contact que está implementada en models.py con el método "list"
    	# y luego lanza la vista "index.html"
        list_usuarios = db_access["list_usuarios"] 
        usuarios = list_usuarios() # para mostrar al inicio los contactos que ya están en la BD
        return render_template("usuarios.html", usuarios=usuarios)


    @app.route("/create", methods=["GET", "POST"])
    def create_usuario():
        if request.method == "GET":
            return render_template("create_usuario.html")

        if request.method == "POST":
            create_usuario = db_access["create_usuario"]
            create_usuario(
                nick=request.form["nick"],
                nombre=request.form["nombre"],
                apellidos=request.form["apellidos"],
            )
            return redirect("/usuarios.html")

    @app.route("/delete/<int:uid>", methods=["GET", "POST"])
    def delete_usuario(uid: int):
        if request.method == "GET":
            read_usuario = db_access["read_usuario"]
            usuario = read_usuario(uid)
            return render_template("delete_usuario.html", usuario=usuario)

        if request.method == "POST":
            delete_usuario = db_access["delete_usuario"]
            delete_usuario(
                uid=uid,
            )
            return redirect("/usuarios.html")
