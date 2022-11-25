from Modelos.Mesa import Mesa
class ControladorMesa():
        def __init__(self):
            print("inicializar el controlador")


        def index(self):
            print("listar todos los candidato")
            unaMesa={
                "numero": "1",
                "_cantidad inscritos": "4"

            }
            return [unaMesa]

        def create(self,infoMesa):
            print("crear un candidato")
            unaMesa = Mesa(infoMesa)
            return unaMesa.__dict__

        def show(self,numero):
            print("mostrar candidato")
            unaMesa = {
                "numero": "1",
                "_cantidad inscritos": "4"
            }
            return unaMesa
        def update(self,id,infoMesa):
            print("Actualizando Candidato don id")
            unaMesa = Mesa(infoMesa)
            return unaMesa.__dict__

        def delete(self,id):
            print("Eliminando Candidato",id)
            return {"delecte count":1}