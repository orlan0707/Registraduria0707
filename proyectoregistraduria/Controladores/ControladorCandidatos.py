from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidatos import Candidatos
class ControladorEstudiante():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidatos):
        nuevoCandidato=Candidatos(infoCandidatos)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidatos(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidatos):
        candidatoActual = Candidatos(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidatos["cedula"]
        candidatoActual.nombre = infoCandidatos["nombre"]
        candidatoActual.apellido = infoCandidatos["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

        def delete(self, id):
            return self.repositorioCandidato.delete(id)