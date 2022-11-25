from Modelos.Partidos import Partidos
class ControladorPartidos():
        def __init__(self):
            print("inicializar el controlador")


        def index(self):
            print("listar todos los candidato")
            unCandidato={
                "_id": "123abs",
                "Cedula": "1130667101",
                "Nombre Candidato": "orlando",
                "Partido Politico": "Democratico"
            }
            return [unCandidato]

        def create(self,infoCandidato):
            print("crear un candidato")
            elCandidato = Candidatos(infoCandidato)
            return elCandidato.__dict__

        def show(self,id):
            print("mostrar candidato")
            elCandidato = {
                "_id": id,
                "Cedula": "1130667101",
                "Nombre Candidato": "orlando",
                "Partido Politico": "Democratico"
            }
            return elCandidato
        def update(self,id,infoCandidato):
            print("Actualizando Candidato don id",id)
            elCandidato = Candidatos(infoCandidato)
            return elCandidato.__dict__

        def delete(self,id):
            print("Eliminando Candidato",id)
            return {"delecte count":1}