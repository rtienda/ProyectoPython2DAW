from typing import Callable

from flask_sqlalchemy import SQLAlchemy

def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    class Gundams(db.Model):
        __tablename__ = "Gundams"

        uid = db.Column("id",db.Integer, primary_key=True)
        nombre = db.Column(db.String(255))
        serie = db.Column(db.String(255))
        precio_euros = db.Column(db.Integer())
        tipo_gunpla = db.Column(db.String(128))
        estado = db.Column(db.String(128)) #pendiente o comprado


    db.create_all()
    return {}