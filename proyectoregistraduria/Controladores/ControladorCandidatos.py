from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorEstudiante():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidatos):
        nuevoCandidato=Candidato(infoCandidatos)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidatos):
        candidatoActual = Candidato(self.RepositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidatos["cedula"]
        candidatoActual.cedula = infoCandidatos["Numero Resolusion"]
        candidatoActual.nombre = infoCandidatos["nombre"]
        candidatoActual.apellido = infoCandidatos["apellido"]
        return self.RepositorioCandidato.save(candidatoActual)

        def delete(self, id):
            return self.RepositorioCandidato.delete(id)
