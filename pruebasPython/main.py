import pymongo
import certifi

ca = certifi.where()


client = pymongo.MongoClient("mongodb+srv://orlandoizq0707:1234@registraduriaciclo4.sgs4ktl.mongodb.net/registraduriaciclo4?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)
basedatos = client ["registraduriaciclo4"]
print(basedatos.list_collection_names())
