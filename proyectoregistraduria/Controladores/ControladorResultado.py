from Modelos.Resultado import Resultado
from Repositorios.RepositorioResultado import RepositorioResultado
class ControladorResultado():
        def __init__(self):
            print("inicializar el controlador")


        def index(self):
            print("listar todos los candidato")
            unResultado={
                "_id": "123abs",
                "Numero mesa": "Democratica",
                "id_partido": "1"

            }
            return [unResultado]

        def create(self,infoResultado):
            print("crear un candidato")
            elResultado = Resultado(infoResultado)
            return elResultado.__dict__

        def show(self,id):
            print("mostrar candidato")
            elResultado = {
                "_id": id,
                "Numero mesa": "Democratica",
                "id_partido": "1"
            }
            return elResultado
        def update(self,id,infoResultado):
            print("Actualizando Candidato don id",id)
            elResultado = Resultado(infoResultado)
            elResultado.numeromesa = infoResultado["numero de mesa"]
            elResultado.idpartido = infoResultado["id del partido"]

            return elResultado.__dict__

        def delete(self,id):
            print("Eliminando resultado",id)
            return {"delecte count":1}