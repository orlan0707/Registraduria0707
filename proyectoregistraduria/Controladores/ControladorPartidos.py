from Modelos.Partidos import Partidos
from Repositorios.RepositorioPartidos import RepositorioPartidos
class ControladorPartidos():
        def __init__(self):
            print("inicializar el controlador")


        def index(self):
            print("listar todos los candidato")
            unPartido={
                "_id": "123abs",
                "Nombre": "Conservador",
                "Lema": "la union hace la fuerza"
            }
            return [unPartido]

        def create(self,infoPartido):
            print("crear un Partido")
            elPartido = Partidos(infoPartido)
            return elPartido.__dict__

        def show(self,id):
            print("mostrar Partido")
            elPartido = {
                "_id": id,
                "Nombre": "Conservador",
                "Lema": "la union hace la fuerza"
            }
            return elPartido
        def update(self,id,infoPartido):
            print("Actualizando Partido don id",id)
            elPartido = Partidos(infoPartido)
            elPartido.nombre = infoPartido["nombre"]
            elPartido.lema = infoPartido["lema"]

            return elPartido.__dict__

        def delete(self,id):
            print("Eliminando Partido",id)
            return {"delecte count":1}