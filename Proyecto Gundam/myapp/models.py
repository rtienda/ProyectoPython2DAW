from typing import Callable

from flask_sqlalchemy import SQLAlchemy

def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    class Gundams(db.Model):
        __tablename__ = "gunpla"

        uid = db.Column("id",db.Integer, primary_key=True)
        name = db.Column(db.String(255))
        series = db.Column(db.String(255))
        height = db.Column(db.Integer())
        manufacturer = db.Column(db.String(255))
        imageUrl = db.Column(db.String(255)) #pendiente o comprado
        price = db.Column(db.String(128))
        release = db.Column(db.String(128))

        def __str__(self): 
            return f"[{self.uid}] {self.names} {self.series}"

        # utilizar el decorador  property para crear una propiedad (atributo) de la clase
        # al que es posible referirse para directamente obtener los atributos nombre y apellido de una vez 
        @property
        def fullname(self) -> str:
            return f"{self.name} {self.series}"

    # ------------- métodos que operan sobre el contenido la tabla -----------
    def create_gundam(name: str, series: str, height: int, manufacturer: str,imageUrl: str, price: str,release: str):
        gundam = Gundams(
            name=name, series=series, height=height, manufacturer=manufacturer, imageUrl=imageUrl, price=price,release=release
        )
        db.session.add(gundam)
        db.session.commit()

    def read_gundam(uid: int) -> Gundams:
        return Gundams.query.get(uid)

    def update_gundam(
        uid: int, name: str, series: str, height: int, manufacturer: str,imageUrl: str, price: str,release: str
    ):
        gundam = Gundams.query.get(uid)
        gundam.name = name
        gundam.series = series
        gundam.height = height
        gundam.manufacturer = manufacturer
        gundam.imageUrl = imageUrl
        gundam.price = price
        gundam.release = release
        db.session.commit()

    def delete_gundam(uid: int):
        gundam = Gundams.query.get(uid)
        db.session.delete(gundam)
        db.session.commit()

    def list_gundams() -> list[Gundams]:
        gundams = Gundams.query.all()
        return [gundam for gundam in gundams]


    #Creacion de tablas usuarios y sus metodos
    class Usuarios(db.Model):
        __tablename__ = "Usuarios"

        uid = db.Column("id",db.Integer, primary_key=True)
        nick = db.Column(db.String(255))
        nombre = db.Column(db.String(255))
        apellidos = db.Column(db.String(255))

        def __str__(self): 
            return f"[{self.uid}] {self.nick} {self.nombre}"

        # utilizar el decorador  property para crear una propiedad (atributo) de la clase
        # al que es posible referirse para directamente obtener los atributos nombre y apellido de una vez 
        @property
        def fullname(self) -> str:
            return f"{self.nick} {self.nombre}"

    # ------------- métodos que operan sobre el contenido la tabla -----------
    def create_usuario(nick: str, nombre: str, apellidos: str):
        usuario = Usuarios(
            nick=nick, nombre=nombre, apellidos=apellidos,
        )
        db.session.add(usuario)
        db.session.commit()

    def read_usuario(uid: int) -> Usuarios:
        return Usuarios.query.get(uid)

    def update_usuario(
        uid: int, nick: str, nombre: str, apellidos: str
    ):
        usuario = Usuarios.query.get(uid)
        usuario.nick = nick
        usuario.nombre = nombre
        usuario.apellidos = apellidos
        db.session.commit()

    def delete_usuario(uid: int):
        usuario = Usuarios.query.get(uid)
        db.session.delete(usuario)
        db.session.commit()

    def list_usuarios() -> list[Usuarios]:
        usuarios = Usuarios.query.all()
        return [usuario for usuario in usuarios]



    # create_all es un método de Flask-alchemy que crea la tabla con sus campos
    db.create_all()

    return {
    	# estos alias serán usados para llamar a los métodos de la clase, por ejemplo db_access["create"]
    	# invoca al método create_contact
        "read_gundam": read_gundam,
        "list_gundams": list_gundams,
        "create_usuario": create_usuario,
        "read_usuario": read_usuario,
        "update_usuario": update_usuario,    
        "delete_usuario": delete_usuario,
        "list_usuarios": list_usuarios,
    }

