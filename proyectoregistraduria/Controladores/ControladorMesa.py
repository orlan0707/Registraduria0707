from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa
class ControladorMesa():
        def __init__(self):
            print("inicializar el controlador")


        def index(self):
            print("listar todos los mesa")
            unaMesa={
                "numero": "1",
                "_cantidad inscritos": "4"

            }
            return [unaMesa]

        def create(self,infoMesa):
            print("crear un mesa")
            unaMesa = Mesa(infoMesa)
            return unaMesa.__dict__

        def show(self,numero):
            print("mostrar mesa")
            unaMesa = {
                "numero": "1",
                "_cantidad inscritos": "4"
            }
            return unaMesa
        def update(self,id,infoMesa):
            print("Actualizando mesa Con id")
            unaMesa = Mesa(infoMesa)
            unaMesa.numero = infoMesa["numero"]
            unaMesa.cantidadinscritos =infoMesa["cantidadinscritos"]
            return unaMesa.__dict__

        def delete(self,id):
            print("Eliminando Mesa",id)
            return {"delecte count":1}