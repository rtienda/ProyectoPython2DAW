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
    @app.route("/gundams", methods=["GET", "POST"])
    def gundams():
    	# invoca a la clase contact que está implementada en models.py con el método "list"
    	# y luego lanza la vista "index.html"
        if  request.args.get("Serie") == None:
            print("antiguo")
            list_gundams = db_access["list_gundams"] 

            gundams = list_gundams() # para mostrar al inicio los contactos que ya están en la BD
            list_gundams_filtro = db_access["list_gundams_filtro"]
            series1= list_gundams_filtro()
            print(request.args.get("Serie"))

        else:
            print("entra")
            list_gundams_filtro1 = db_access["list_gundams_filtro1"] 

            # prueba=request.args.get("Serie")
            print(request.args)
            print(request.args.get("Serie"))
            serieActual=request.args.get("Serie")
            gundams = list_gundams_filtro1(serieActual)
            # print(gundams[1].name)
            # para mostrar al inicio los contactos que ya están en la BD
            list_gundams_filtro = db_access["list_gundams_filtro"]
            series1= list_gundams_filtro()            
        return render_template("gundams.html", gundams=gundams,series1=series1)
    
    @app.route("/gundams/<series2>", methods=["GET", "POST"])
    def gundamsBusqueda(series2: str):
    	# invoca a la clase contact que está implementada en models.py con el método "list"
    	# y luego lanza la vista "index.html"
        print("entra")
        list_gundams_filtro1 = db_access["list_gundams_filtro1"] 
        gundams = list_gundams_filtro1(series2)
        print(gundams[1].name)
        # para mostrar al inicio los contactos que ya están en la BD
        list_gundams_filtro = db_access["list_gundams_filtro"]
        series1= list_gundams_filtro()
        return render_template("gundams.html", gundams=gundams,series1=series1)
    # def filtro_series_gundams():
    #     list_gundams_filtro = db_access["list_gundams_filtro"]
    #     series1= list_gundams_filtro()
    #     return render_template("gundams.html",series1=series1)

   
    @app.route("/update_usuario/<int:uid>", methods=["GET", "POST"])
    def update_usuario(uid: int):
        if request.method == "GET":
            read_usuario = db_access["read_usuario"]
            usuario = read_usuario(uid)
            return render_template("update_usuario.html", usuario=usuario)

        if request.method == "POST":
            update_usuario = db_access["update_usuario"]
            update_usuario(
                uid=uid,
                nick=request.form["nick"],
                nombre=request.form["nombre"],
                apellidos=request.form["apellidos"],
            )
            return redirect("/usuarios")
        
    @app.route("/update_gundam/<int:uid>", methods=["GET", "POST"])
    def update_gundam(uid: int):
        if request.method == "GET":
            read_gundam = db_access["read_gundam"]
            gundam = read_gundam(uid)
            return render_template("update_gundam.html", gundam=gundam)

        if request.method == "POST":
            update_gundam = db_access["update_gundam"]
            update_gundam(
                uid=uid,
                name=request.form["name"],
                series=request.form["series"],
                # height=float(request.form["height"]),
                manufacturer=request.form["manufacturer"],
                imageUrl=request.form["imageUrl"],
                price=request.form["price"],
                release=request.form["release"],
            )
            return redirect("/gundams")


        
    @app.route("/usuarios", methods=["GET", "POST"])
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
            
            nick = request.form["nick"]
            nombre = request.form["nombre"]
            apellidos = request.form["apellidos"]

            # Procesamiento para convertir a minúscula excepto la primera letra
            nick = nick.lower().capitalize()
            nombre = nombre.lower().capitalize()
            apellidos = apellidos.lower().capitalize()

            create_usuario = db_access["create_usuario"]
            create_usuario(
                nick=nick,
                nombre=nombre,
                apellidos=apellidos,
            )
            return redirect("/usuarios")
    @app.route("/create_gundam", methods=["GET", "POST"])
    def create_gundam():
        if request.method == "GET":
            return render_template("create_gundam.html")

        if request.method == "POST":
            create_gundam = db_access["create_gundam"]
            create_gundam(
                name=request.form["name"],
                series=request.form["series"],
                # height=float(request.form["height"]),
                manufacturer=request.form["manufacturer"],
                imageUrl=request.form["imageUrl"],
                price=request.form["price"],
                release=request.form["release"],
            )
            return redirect("/gundams")


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
            return redirect("/usuarios")

    @app.route("/delete_gundam/<int:uid>", methods=["GET", "POST"])
    def delete_gundam(uid: int):
        if request.method == "GET":
            read_gundam = db_access["read_gundam"]
            gundam = read_gundam(uid)
            return render_template("delete_gundam.html", gundam=gundam)

        if request.method == "POST":
            delete_gundam = db_access["delete_gundam"]
            delete_gundam(
                uid=uid,
            )
            return redirect("/gundams")
        
    @app.route("/delete_usuario_gundam/<int:uid>", methods=["GET", "POST"])
    def delete_usuario_gundam(uid: int):
        if request.method == "GET":
            read_usuario_gundam = db_access["read_usuario_gundam"]
            usuario_gundam = read_usuario_gundam(uid)
            return render_template("delete_usuario_gundam.html", usuario_gundam=usuario_gundam)

        if request.method == "POST":
            delete_usuario_gundam = db_access["delete_usuario_gundam"]
            delete_usuario_gundam(
                uid=uid,
            )
            return redirect("/usuario_gundam")

    @app.route("/usuario_gundam", methods=["GET"])
    def usuario_gundam(): 
        # proys_trabjs_page = int(request.args.get("pagina", 1))  
        # -------------------------------------------------
        
        # -------------------------------------------------
        # leer los valores de la BD (la función está implementada en models.py)      
        usuario_gundam_list_all = db_access[
            "usuario_gundam_list_all"
        ]  
        usuario_gundam_list_all1=usuario_gundam_list_all()
        # proys_trabjs = usuario_gundam_list(page = proys_trabjs_page)
        # -------------------------------------------------
        
        # -------------------------------------------------
        # calcular el número total de páginas y crear listado
        # items_by_page = int(3)      
        # total_pages = ceil(proys_trabjs.total / items_by_page)
        # proys_trabjs_page_list = [i + 1 for i in range(total_pages)]          
        # -------------------------------------------------
        
           
        return render_template("usuario_gundam.html",
                               usuario_gundam_list_all1 = usuario_gundam_list_all1
                            #    proys_trabjs_page_list = proys_trabjs_page_list
                               )
    
    @app.route("/create_usuario_gundam", methods=["GET", "POST"])
    def create_usuario_gundam():   
        
        list_gundams = db_access["list_gundams"] 
        gundams = list_gundams()
        
        list_usuarios = db_access[ "list_usuarios"] 
        usuarios = list_usuarios()  
        
        usuario_gundam_list_all = db_access["usuario_gundam_list_all"]
        usuario_gundam = usuario_gundam_list_all()  
         
        return render_template("create_usuario_gundam.html",
                            usuarios = usuarios, 
                            gundams = gundams,  
                            usuario_gundam = usuario_gundam, 
                            )
        
    @app.route("/create_usuario_gundam_fecha", methods=["GET", "POST"])
    def create_usuario_gundam_fecha():
        if request.method == "POST":
            create_usuario_gundam = db_access["create_usuario_gundam"]
            create_usuario_gundam(
                fecha=request.form["usuario_gundam_fecha"],
                id_usuario=int(request.form["usuario_id"]),
                id_gundam=int(request.form["gundam_id"])               
            )
            return redirect("/create_usuario_gundam")
        
    @app.route("/update_usuario_gundam/<int:uid>", methods=["GET", "POST"])
    def update_usuario_gundam(uid: int):
        if request.method == "GET":
            read_usuario_gundam = db_access["read_usuario_gundam"]
            usuario_gundam = read_usuario_gundam(uid)
            return render_template("update_usuario_gundam.html", usuario_gundam=usuario_gundam)

        if request.method == "POST":
            update_usuario_gundam = db_access["update_usuario_gundam"]
            update_usuario_gundam(
                uid=uid,
                fecha=request.form["fecha"],
  
            )
            return redirect("/usuario_gundam")